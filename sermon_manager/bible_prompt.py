"""Priming prompts for sermon transcription.

Builds a faster-whisper `initial_prompt` from sermon metadata plus the NIV
text of the sermon's bible passage (fetched from Bible Gateway and cached
locally). Prime text is trimmed to whisper's ~224-token priming budget.
"""

import json
import os
import re
import urllib.parse

import requests
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_PATH = os.path.join(PROJECT_ROOT, "bible_niv_cache.json")

# Canonical NIV book names, in canonical order (used for name resolution).
BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua",
    "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings",
    "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job",
    "Psalms", "Proverbs", "Ecclesiastes", "Song of Songs", "Isaiah",
    "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai",
    "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
    "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation",
]

# Aliases map -> canonical book name.
BOOK_ALIASES = {
    "ps": "Psalms",
    "psa": "Psalms",
    "psalm": "Psalms",
    "eccl": "Ecclesiastes",
    "song": "Song of Songs",
    "song of solomon": "Song of Songs",
    "1 cor": "1 Corinthians",
    "2 cor": "2 Corinthians",
    "1 thess": "1 Thessalonians",
    "2 thess": "2 Thessalonians",
    "1 tim": "1 Timothy",
    "2 tim": "2 Timothy",
    "1 pet": "1 Peter",
    "2 pet": "2 Peter",
    "1 jn": "1 John",
    "2 jn": "2 John",
    "3 jn": "3 John",
    "rev": "Revelation",
}

_SEARCHABLE = {b.lower(): b for b in BOOKS}
_SEARCHABLE.update(BOOK_ALIASES)
# Fallback: alias where 's' already handled, plus plural forms.
for _b in BOOKS:
    if _b.lower() not in _SEARCHABLE:
        _SEARCHABLE[_b.lower()] = _b
    if _b.lower().endswith("s") and _b.lower()[:-1] not in _SEARCHABLE:
        _SEARCHABLE[_b.lower()[:-1]] = _b


def _canonical_book(name):
    cleaned = re.sub(r"[^a-z0-9 ]", "", (name or "").lower().strip())
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return _SEARCHABLE.get(cleaned.strip())


def _parse_verses(verses, chapter):
    """Parse a verse spec like '5-11', '23-11:1', or None (whole chapter)."""
    if not verses:
        return None, None
    verses = verses.replace("\u2013", "-").replace("\u2014", "-")
    parts = re.split(r"\s*-\s*", verses)
    start = int(re.match(r"\d+", parts[0]).group())
    if len(parts) == 1:
        return start, start
    end_ch, end_v = parts[1].split(":") if ":" in parts[1] else (chapter, parts[1])
    end_v = int(re.match(r"\d+", end_v).group())
    if int(end_ch) > chapter:
        return start, (int(end_ch), end_v)
    return start, end_v


def parse_passage(ref):
    """Split a passage reference into structured segments.

    Handles '1 Corinthians 12:1-14, Galatians 5:16-26' and continuation chunks
    like '1 Corinthians 14:1-5, 26-33a'. Returns list of
    {book, chapter, verse_start, verse_end} dicts (verse_end may be (chapter, v)).
    """
    segments = []
    current = None
    for chunk in re.split(r"[,;]", ref or ""):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.match(
            r"^((?:\d{1,2}\s+)?[a-z][a-z .]*?)\s*(\d{1,3})(?::([\d.:a-cA-C\u2013\u2014-]+))?$",
            chunk.lower(),
        )
        if m:
            name, chapter, verses = m.groups()
            book = _canonical_book(name)
            chapter = int(chapter)
            if book:
                vstart, vend = _parse_verses(verses, chapter)
                current = {"book": book, "chapter": chapter,
                           "verse_start": vstart, "verse_end": vend}
                segments.append(current)
                continue
        if current is not None:  # continuation chunk (missing book name)
            vm = re.fullmatch(r"[\d:]+(?:-[\d:]+)?[a-cA-C]?", chunk)
            if vm:
                spec = vm.group(0)
                parts = re.split(r"-", spec)
                start = parts[0]
                end = parts[1] if len(parts) > 1 else start
                end_ch = end.split(":")[0] if ":" in end else current["chapter"]
                end_v = int(re.match(r"\d+", end).group())
                cur_end = current["verse_end"]
                cur_hi = (current["chapter"], cur_end[1]) if isinstance(cur_end, tuple) else (current["chapter"], cur_end or 1)
                new_end = (int(end_ch), end_v)
                if new_end > cur_hi:
                    current["verse_end"] = new_end
    return segments


# --- NIV fetching ------------------------------------------------------------------

_cache = None


def _load_cache():
    global _cache
    if _cache is None:
        if os.path.exists(CACHE_PATH):
            with open(CACHE_PATH, encoding="utf-8") as f:
                _cache = json.load(f)
        else:
            _cache = {}
    return _cache


def _save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(_cache, f, ensure_ascii=False)


def _fetch_bible_gateway(ref):
    """Fetch NIV text for a single textual reference from Bible Gateway."""
    url = ("https://www.biblegateway.com/passage/?version=NIV&search="
           + urllib.parse.quote_plus(ref))
    resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    html = resp.text.replace("<br/>", "\n").replace("<br>", "\n")
    doc = BeautifulSoup(html, "html.parser")
    passage = doc.select_one(".passage-text")
    if not passage:
        return ""
    for tag in passage.select(
        "h1, h3, h4, sup, .chapternum, .footnotes, .crossrefs, "
        ".publisher-info-bottom, .footnote, .crossrefs"
    ):
        tag.decompose()
    text = passage.get_text(separator=" ", strip=True)
    text = re.split(r"\s*Read full chapter\b", text, maxsplit=1)[0]
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_passage_text(ref):
    """Return NIV text for a passage reference (cached, graceful on failure)."""
    key = re.sub(r"\s+", " ", (ref or "").strip().lower())
    if not key or key == "-":
        return ""
    cache = _load_cache()
    if key in cache:
        return cache[key]
    segments = parse_passage(ref)
    if not segments:
        return ""

    texts = []
    for seg in segments:
        seg_ref = seg["book"]
        if seg["verse_start"]:
            end_part = seg["verse_end"]
            if isinstance(end_part, tuple):
                seg_ref += (" %d:%d-%d:%d" % (seg["chapter"], seg["verse_start"],
                                              end_part[0], end_part[1]))
            elif end_part and end_part > seg["verse_start"]:
                seg_ref += " %d:%d-%d" % (seg["chapter"], seg["verse_start"], end_part)
            else:
                seg_ref += " %d:%d" % (seg["chapter"], seg["verse_start"])
        else:
            seg_ref += " %d" % seg["chapter"]
        try:
            texts.append(_fetch_bible_gateway(seg_ref))
        except Exception:
            texts.append("")
    text = " ".join(t for t in texts if t)
    cache[key] = text
    _save_cache()
    return text


# --- Prompt building -----------------------------------------------------------------

def build_sermon_prompt(sermon, max_chars=1000):
    """Initial prompt combining sermon metadata with NIV passage text."""
    lines = [f"The sermon title is: {sermon.get('title') or ''}."]
    if sermon.get('sermon_series'):
        lines.append(f"Sermon series: {sermon['sermon_series']}.")
    if sermon.get('speaker'):
        lines.append(f"Preacher: {sermon['speaker']}.")
    passage = sermon.get('bible_passage') or ''
    if passage:
        lines.append(f"Bible passage: {passage}.")
    prompt = " ".join(lines)

    if passage:
        nicv = get_passage_text(passage)
        if nicv:
            prompt += f"\nNIV {passage}: {nicv}"

    if len(prompt) > max_chars:
        prompt = prompt[:max_chars].rsplit(" ", 1)[0]
    return prompt