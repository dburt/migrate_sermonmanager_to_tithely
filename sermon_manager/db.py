"""SQLite database layer for the St Alfred's sermon mirror.

Two source tables (wordpress archive + tithely live mirror) are merged by a
pure SQL view (v_sermons). Transcriptions attach to whichever source owns the
sermon via nullable foreign keys (exactly one non-null).
"""

import json
import os
import re
import sqlite3
from datetime import datetime
from pathlib import Path

DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sermons.db")

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS wordpress_sermons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wordpress_post_id TEXT,
    title TEXT NOT NULL,
    post_date_gmt TEXT,
    permalink TEXT,
    content_text TEXT,
    preacher TEXT,
    sermon_series TEXT,
    bible_passage TEXT,
    bible_book TEXT,
    sermon_topics TEXT,
    service_type TEXT,
    view_count INTEGER,
    audio_url TEXT,
    audio_file_size INTEGER,
    melbourne_time TEXT
);

CREATE TABLE IF NOT EXISTS tithely_sermons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    speaker TEXT,
    date TEXT,
    date_gmt TEXT,
    sermon_series TEXT,
    bible_passage TEXT,
    description TEXT,
    audio_url TEXT,
    audio_file_size INTEGER,
    local_audio_path TEXT,
    last_seen_at TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transcriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tithely_sermon_id INTEGER REFERENCES tithely_sermons(id) ON DELETE CASCADE,
    wordpress_sermon_id INTEGER REFERENCES wordpress_sermons(id) ON DELETE CASCADE,
    transcript_text TEXT NOT NULL,
    word_count INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    CHECK (tithely_sermon_id IS NOT NULL OR wordpress_sermon_id IS NOT NULL)
);

CREATE INDEX IF NOT EXISTS idx_wp_audio_size ON wordpress_sermons(audio_file_size);
CREATE INDEX IF NOT EXISTS idx_wp_date ON wordpress_sermons(post_date_gmt);
CREATE INDEX IF NOT EXISTS idx_tithely_audio_size ON tithely_sermons(audio_file_size);
CREATE INDEX IF NOT EXISTS idx_tithely_date ON tithely_sermons(date_gmt);
CREATE INDEX IF NOT EXISTS idx_tr_tithely ON transcriptions(tithely_sermon_id);
CREATE INDEX IF NOT EXISTS idx_tr_wordpress ON transcriptions(wordpress_sermon_id);

CREATE VIRTUAL TABLE IF NOT EXISTS sermons_fts USING fts5(
    title,
    speaker,
    sermon_series,
    bible_passage,
    topics,
    description,
    content_text,
    transcript_text,
    sermon_key UNINDEXED
);
"""


def connect(db_path=DEFAULT_DB_PATH):
    """Open (creating if needed) the sermon mirror database."""
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA busy_timeout = 10000")
    return conn


def init_db(conn):
    """Create tables/views if needed; rebuild the derived v_sermons view."""
    conn.executescript(SCHEMA)
    _migrate_transcriptions_check(conn)
    conn.execute("DROP VIEW IF EXISTS v_sermons")
    conn.executescript(CREATE_VIEW)


def _migrate_transcriptions_check(conn):
    """Rebuild `transcriptions` if it still has the old exactly-one-source CHECK."""
    row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='transcriptions'"
    ).fetchone()
    if row and "wordpress_sermon_id IS NULL" in (row["sql"] or ""):
        conn.executescript("""
            PRAGMA foreign_keys = OFF;
            BEGIN;
            CREATE TABLE _transcriptions_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tithely_sermon_id INTEGER REFERENCES tithely_sermons(id) ON DELETE CASCADE,
                wordpress_sermon_id INTEGER REFERENCES wordpress_sermons(id) ON DELETE CASCADE,
                transcript_text TEXT NOT NULL,
                word_count INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                CHECK (tithely_sermon_id IS NOT NULL OR wordpress_sermon_id IS NOT NULL)
            );
            INSERT INTO _transcriptions_new SELECT * FROM transcriptions;
            DROP TABLE transcriptions;
            ALTER TABLE _transcriptions_new RENAME TO transcriptions;
            COMMIT;
            PRAGMA foreign_keys = ON;
            CREATE INDEX IF NOT EXISTS idx_tr_tithely ON transcriptions(tithely_sermon_id);
            CREATE INDEX IF NOT EXISTS idx_tr_wordpress ON transcriptions(wordpress_sermon_id);
        """)

# --- View: merged canonical record -------------------------------------------------

CREATE_VIEW = """
CREATE VIEW IF NOT EXISTS v_sermons AS
SELECT
    tithely_sermon_id, wordpress_sermon_id, audio_file_size, slug, title, speaker, preacher,
    sermon_series, bible_passage, date, post_date_gmt, sermon_topics, topics, description,
    content_text, service_type, wordpress_post_id, view_count, audio_url, local_audio_path,
    permalink, melbourne_time
FROM (
    -- 1. Matched on audio_file_size
    SELECT
        t.id AS tithely_sermon_id,
        w.id AS wordpress_sermon_id,
        t.audio_file_size AS audio_file_size,
        t.slug AS slug,
        COALESCE(t.title, w.title) AS title,
        COALESCE(t.speaker, w.preacher) AS speaker,
        COALESCE(w.preacher, t.speaker) AS preacher,
        COALESCE(t.sermon_series, w.sermon_series) AS sermon_series,
        COALESCE(NULLIF(t.bible_passage, ''), w.bible_passage) AS bible_passage,
        t.date AS date,
        COALESCE(w.post_date_gmt, t.date_gmt) AS post_date_gmt,
        COALESCE(w.sermon_topics, '') AS sermon_topics,
        COALESCE(w.sermon_topics, '') AS topics,
        COALESCE(t.description, w.content_text) AS description,
        COALESCE(w.content_text, t.description) AS content_text,
        COALESCE(w.service_type, '') AS service_type,
        COALESCE(w.wordpress_post_id, '') AS wordpress_post_id,
        COALESCE(w.view_count, 0) AS view_count,
        COALESCE(t.audio_url, w.audio_url) AS audio_url,
        COALESCE(t.local_audio_path, '') AS local_audio_path,
        COALESCE(w.permalink, '') AS permalink,
        COALESCE(w.melbourne_time, '') AS melbourne_time
    FROM tithely_sermons t
    JOIN wordpress_sermons w ON w.audio_file_size = t.audio_file_size AND t.audio_file_size != 0

    UNION ALL

    -- 2. Tithely-only
    SELECT
        t.id AS tithely_sermon_id,
        NULL AS wordpress_sermon_id,
        t.audio_file_size AS audio_file_size,
        t.slug AS slug,
        t.title AS title,
        t.speaker AS speaker,
        t.speaker AS preacher,
        t.sermon_series AS sermon_series,
        t.bible_passage AS bible_passage,
        t.date AS date,
        t.date_gmt AS post_date_gmt,
        '' AS sermon_topics,
        '' AS topics,
        t.description AS description,
        t.description AS content_text,
        '' AS service_type,
        '' AS wordpress_post_id,
        0 AS view_count,
        t.audio_url AS audio_url,
        t.local_audio_path AS local_audio_path,
        '' AS permalink,
        '' AS melbourne_time
    FROM tithely_sermons t
    LEFT JOIN wordpress_sermons w ON w.audio_file_size = t.audio_file_size AND t.audio_file_size != 0
    WHERE w.id IS NULL

    UNION ALL

    -- 3. WordPress-only
    SELECT
        NULL AS tithely_sermon_id,
        w.id AS wordpress_sermon_id,
        w.audio_file_size AS audio_file_size,
        NULL AS slug,
        w.title AS title,
        w.preacher AS speaker,
        w.preacher AS preacher,
        w.sermon_series AS sermon_series,
        w.bible_passage AS bible_passage,
        NULL AS date,
        w.post_date_gmt AS post_date_gmt,
        w.sermon_topics AS sermon_topics,
        w.sermon_topics AS topics,
        w.content_text AS description,
        w.content_text AS content_text,
        w.service_type AS service_type,
        w.wordpress_post_id AS wordpress_post_id,
        w.view_count AS view_count,
        w.audio_url AS audio_url,
        '' AS local_audio_path,
        w.permalink AS permalink,
        w.melbourne_time AS melbourne_time
    FROM wordpress_sermons w
    LEFT JOIN tithely_sermons t ON t.audio_file_size = w.audio_file_size AND w.audio_file_size != 0
    WHERE t.id IS NULL
);
"""

# --- Helpers --------------------------------------------------------------------------

TITHELY_MONTHS = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12',
}


def parse_tithely_date(date_str):
    """Convert a Tithely date like 'Mar 1, 2026' to '2026-03-01 00:00:00'.

    Returns empty string if the format is unrecognised.
    """
    if not date_str:
        return ''
    m = re.match(r'^\s*([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2}),\s+(\d{4})', date_str)
    if not m:
        return ''
    month, day, year = m.groups()
    month_num = TITHELY_MONTHS.get(month.capitalize())
    if not month_num:
        return ''
    return f"{year}-{month_num}-{int(day):02d} 00:00:00"


def _normalize_int(value):
    try:
        return int(float(value or 0))
    except (ValueError, TypeError):
        return 0


def upsert_wordpress(conn, rows):
    """Insert (or replace) WordPress sermon records. Returns number written."""
    cur = conn.cursor()
    written = 0
    for r in rows:
        size = _normalize_int(r.get('audio_file_size'))
        cur.execute("""
            INSERT INTO wordpress_sermons (
                wordpress_post_id, title, post_date_gmt, permalink, content_text, preacher,
                sermon_series, bible_passage, bible_book, sermon_topics, service_type,
                view_count, audio_url, audio_file_size, melbourne_time)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            r.get('post_id') or '',
            r.get('title') or '',
            r.get('post_date_gmt') or '',
            r.get('permalink') or '',
            r.get('content_text') or '',
            r.get('preacher') or '',
            r.get('sermon_series') or '',
            r.get('bible_passage') or '',
            r.get('bible_book') or '',
            r.get('sermon_topics') or '',
            r.get('service_type') or '',
            _normalize_int(r.get('view_count')),
            r.get('audio_url') or '',
            size,
            r.get('melbourne_time') or '',
        ))
        written += 1
    conn.commit()
    return written


def upsert_tithely(conn, sermons):
    """Upsert Tithely sermon records keyed by slug.

    Returns dict {new, updated, unchanged}. New/changed rows are written;
    existing rows are compared on a subset of meaningful fields.
    """
    cur = conn.cursor()
    new = updated = unchanged = 0

    for s in sermons:
        slug = s.get('slug') or ''
        if not slug:
            continue
        date_gmt = parse_tithely_date(s.get('date'))
        existing = cur.execute(
            "SELECT * FROM tithely_sermons WHERE slug = ?", (slug,)
        ).fetchone()

        fields = (
            s.get('title', ''),
            s.get('speaker', ''),
            s.get('date', ''),
            date_gmt,
            s.get('sermon_series', ''),
            s.get('bible_passage', ''),
            s.get('description', ''),
            s.get('audio_url', ''),
            _normalize_int(s.get('audio_file_size')),
        )

        if existing is None:
            cur.execute("""
                INSERT INTO tithely_sermons (
                    slug, title, speaker, date, date_gmt, sermon_series, bible_passage,
                    description, audio_url, audio_file_size, last_seen_at, updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (slug, *fields))
            new += 1
        else:
            changed = (
                existing['title'] != fields[0]
                or (existing['speaker'] or '') != (fields[1] or '')
                or (existing['date'] or '') != (fields[2] or '')
                or (existing['sermon_series'] or '') != (fields[3] or '')
                or (existing['bible_passage'] or '') != (fields[4] or '')
                or (existing['description'] or '') != (fields[5] or '')
                or (existing['audio_url'] or '') != (fields[6] or '')
                or (existing['audio_file_size'] or 0) != fields[7]
            )
            if changed:
                cur.execute("""
                    UPDATE tithely_sermons SET
                        title = ?, speaker = ?, date = ?, date_gmt = ?, sermon_series = ?,
                        bible_passage = ?, description = ?, audio_url = ?, audio_file_size = ?,
                        last_seen_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP
                    WHERE slug = ?
                """, (*fields, slug))
                updated += 1
            else:
                cur.execute(
                    "UPDATE tithely_sermons SET last_seen_at = CURRENT_TIMESTAMP WHERE slug = ?",
                    (slug,),
                )
                unchanged += 1

    conn.commit()
    return {'new': new, 'updated': updated, 'unchanged': unchanged}


def get_tithely_slugs(conn):
    """Return the set of slugs currently in the tithely table."""
    rows = conn.execute("SELECT slug FROM tithely_sermons").fetchall()
    return {r['slug'] for r in rows}


def get_merged_sermons(conn):
    """Return all merged sermon records from the v_sermons view, newest first."""
    rows = conn.execute("""
        SELECT * FROM v_sermons
        ORDER BY (post_date_gmt = '' OR post_date_gmt IS NULL) DESC, post_date_gmt DESC
    """).fetchall()
    return [dict(r) for r in rows]


def get_sermon_by_slug(conn, slug):
    row = conn.execute("SELECT * FROM v_sermons WHERE slug = ?", (slug,)).fetchone()
    return dict(row) if row else None


def get_sermons_with_transcripts(conn):
    """Merged sermons, each including a `transcript` field when available."""
    sermons = get_merged_sermons(conn)
    tr_by_tid = {
        r['tithely_sermon_id']: r['transcript_text']
        for r in conn.execute(
            "SELECT tithely_sermon_id, transcript_text FROM transcriptions WHERE tithely_sermon_id IS NOT NULL"
        )
    }
    tr_by_wid = {
        r['wordpress_sermon_id']: r['transcript_text']
        for r in conn.execute(
            "SELECT wordpress_sermon_id, transcript_text FROM transcriptions WHERE wordpress_sermon_id IS NOT NULL"
        )
    }
    for m in sermons:
        txt = ''
        if m.get('tithely_sermon_id') and m['tithely_sermon_id'] in tr_by_tid:
            txt = tr_by_tid[m['tithely_sermon_id']]
        elif m.get('wordpress_sermon_id') and m['wordpress_sermon_id'] in tr_by_wid:
            txt = tr_by_wid[m['wordpress_sermon_id']]
        m['transcript'] = txt
    return sermons


# --- Transcriptions --------------------------------------------------------------------

def get_merged_transcripts(conn):
    """Return transcriptions joined to the merged record, keyed by source ids."""
    rows = conn.execute("""
        SELECT tr.*, s.slug AS slug
        FROM transcriptions tr
        LEFT JOIN tithely_sermons s ON s.id = tr.tithely_sermon_id
        ORDER BY tr.id
    """).fetchall()
    return [dict(r) for r in rows]


def add_transcription(conn, transcript_text, tithely_sermon_id=None, wordpress_sermon_id=None):
    """Add a transcription attached to at least one source sermon.

    A merged sermon (same audio on both legacy and Tithely) may set both ids.
    """
    if not (tithely_sermon_id or wordpress_sermon_id):
        raise ValueError("At least one of tithely_sermon_id or wordpress_sermon_id is required")
    word_count = len(re.findall(r"\b\w+\b", transcript_text or ""))
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO transcriptions (tithely_sermon_id, wordpress_sermon_id, transcript_text, word_count)
        VALUES (?,?,?,?)
    """, (tithely_sermon_id, wordpress_sermon_id, transcript_text, word_count))
    conn.commit()
    return cur.lastrowid


def get_pending_transcriptions(conn):
    """Sermons (merged) that have an audio source but no transcription yet.

    Uses NOT EXISTS so tithely-only rows (wordpress_sermon_id NULL) are not
    silently dropped by a NULL `NOT IN` comparison.
    """
    rows = conn.execute("""
        SELECT v.* FROM v_sermons v
        WHERE v.audio_url != ''
          AND NOT EXISTS (SELECT 1 FROM transcriptions x WHERE x.tithely_sermon_id = v.tithely_sermon_id)
          AND NOT EXISTS (SELECT 1 FROM transcriptions x WHERE x.wordpress_sermon_id = v.wordpress_sermon_id)
        ORDER BY v.post_date_gmt DESC
    """).fetchall()
    return [dict(r) for r in rows]


# --- Audio mirror -----------------------------------------------------------------------

def get_pending_audio(conn):
    """Merged sermons with an audio URL but no local_audio_path yet."""

    # NOTE: the view emits the raw (possibly NULL) local_audio_path for
    # tithely-only rows, so compare with COALESCE, not `= ''`.
    rows = conn.execute("""
        SELECT * FROM v_sermons
        WHERE audio_url != '' AND COALESCE(local_audio_path, '') = ''
        ORDER BY post_date_gmt DESC
    """).fetchall()
    return [dict(r) for r in rows]


def get_audio_mirrored(conn):
    """Count of sermons with a local audio path."""
    return conn.execute(
        "SELECT COUNT(*) AS c FROM tithely_sermons WHERE local_audio_path IS NOT NULL AND local_audio_path != ''"
    ).fetchone()['c']


def record_local_audio(conn, slug, path):
    """Record that a sermon's audio now lives at the given local path."""
    conn.execute("UPDATE tithely_sermons SET local_audio_path = ? WHERE slug = ?", (path, slug))
    conn.commit()


# --- Seeding ----------------------------------------------------------------------------

def _load_csv(csv_path):
    import csv
    with open(csv_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _load_index(json_path):
    with open(json_path, encoding='utf-8') as f:
        return json.load(f)


def _normalize_title(title):
    s = title or ''
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    return s


def seed_from_files(conn, csv_path, tithely_index_path, transcripts_dir=None, _echo=print):
    """Bootstrap the database from sermons_with_sizes.csv and tithely_index.json.

    Returns a summary dict.
    """
    init_db(conn)

    summary = {}

    if os.path.exists(csv_path):
        rows = _load_csv(csv_path)
        n = upsert_wordpress(conn, rows)
        summary['wordpress'] = n
    else:
        _echo(f"WARNING: WordPress CSV not found at {csv_path}")

    if os.path.exists(tithely_index_path):
        sermons = _load_index(tithely_index_path)
        res = upsert_tithely(conn, sermons)
        summary['tithely'] = res
    else:
        _echo(f"WARNING: Tithely index not found at {tithely_index_path}")

    if transcripts_dir and os.path.isdir(transcripts_dir):
        summary['transcripts'] = _import_transcripts(conn, transcripts_dir, _echo=_echo)

    summary['fts_rows'] = refresh_fts(conn)
    return summary


def _import_transcripts(conn, transcripts_dir, _echo=print):
    """Import transcript .txt files, linking each to a sermon by date+title."""
    imported = 0
    unmatched = []
    for path in sorted(Path(transcripts_dir).glob('*.txt')):
        stem = path.stem
        m = re.match(r'^(\d{4}-\d{2}-\d{2})_(.+)$', stem)
        if not m:
            _echo(f"  SKIP (no date in name): {path.name}")
            continue
        fdate, ftitle = m.groups()
        ftitle = _normalize_title(ftitle)

        # Candidate matches by date (wordpress first - transcripts are legacy sermons)
        w = [(row['id'], row['title']) for row in conn.execute("""
            SELECT id, title FROM wordpress_sermons WHERE post_date_gmt LIKE ? ORDER BY id
        """, (fdate + '%',)).fetchall()]
        t = [(row['id'], row['title']) for row in conn.execute("""
            SELECT id, title FROM tithely_sermons WHERE date_gmt LIKE ? ORDER BY id
        """, (fdate + '%',)).fetchall()]

        def find_in(cands):
            for (cand_id, cand_title) in cands:
                if _normalize_title(cand_title) == ftitle:
                    return cand_id
            return None

        table = sid = None
        wid = find_in(w)
        tid = find_in(t)
        if wid is not None:  # prefer wordpress for legacy transcripts
            table, sid = 'wordpress', wid
        elif tid is not None:
            table, sid = 'tithely', tid
        elif len(w + t) == 1:
            table = 'wordpress' if len(w) == 1 else 'tithely'
            sid = (w + t)[0][0]
        else:
            _echo(f"  UNMATCHED: {path.name} ({fdate}, '{ftitle}')")
            unmatched.append(path.name)
            continue

        if table == 'wordpress':
            add_transcription(conn, path.read_text(encoding='utf-8'), wordpress_sermon_id=sid)
        else:
            add_transcription(conn, path.read_text(encoding='utf-8'), tithely_sermon_id=sid)
        imported += 1
        _echo(f"  imported {path.name}")

    return {'imported': imported, 'unmatched': unmatched}


def counts(conn):
    c = conn.execute("SELECT COUNT(*) AS c FROM wordpress_sermons").fetchone()['c']
    t = conn.execute("SELECT COUNT(*) AS c FROM tithely_sermons").fetchone()['c']
    tr = conn.execute("SELECT COUNT(*) AS c FROM transcriptions").fetchone()['c']
    m = conn.execute("SELECT COUNT(*) AS c FROM v_sermons").fetchone()['c']
    return {'wordpress': c, 'tithely': t, 'transcriptions': tr, 'merged': m}


# --- Full-text search ------------------------------------------------------------------

def _sermon_key(row):
    """Stable signed integer key for a merged sermon record (positive = tithely)."""
    if row.get('tithely_sermon_id'):
        return int(row['tithely_sermon_id'])
    return -int(row['wordpress_sermon_id'] or 0)


def refresh_fts(conn):
    """Rebuild the FTS index from the merged view + transcriptions."""
    conn.execute("DELETE FROM sermons_fts")
    rows = []
    for m in get_merged_sermons(conn):
        key = _sermon_key(m)
        r = conn.execute("""
            SELECT transcript_text FROM transcriptions
            WHERE (tithely_sermon_id IS NOT NULL AND tithely_sermon_id = ?)
               OR (wordpress_sermon_id IS NOT NULL AND wordpress_sermon_id = ?)
            ORDER BY id LIMIT 1
        """, (m.get('tithely_sermon_id'), m.get('wordpress_sermon_id'))).fetchone()
        rows.append((
            m.get('title') or '',
            m.get('speaker') or '',
            m.get('sermon_series') or '',
            m.get('bible_passage') or '',
            m.get('topics') or '',
            m.get('description') or '',
            m.get('content_text') or '',
            r['transcript_text'] if r else '',
            key,
        ))
    conn.executemany(
        "INSERT INTO sermons_fts (title, speaker, sermon_series, bible_passage, topics, description, content_text, transcript_text, sermon_key) VALUES (?,?,?,?,?,?,?,?,?)",
        rows,
    )
    conn.commit()
    return len(rows)


def build_search_db(conn, search_path):
    """Create a standalone read-only FTS database for server-side transcript search.

    Mirrors sermons_fts but also stores each sermon's `slug`, so the PHP search
    endpoint can return results the static page can join against sermons.json.
    """
    import sqlite3
    import os as _os

    if _os.path.exists(search_path):
        _os.remove(search_path)
    dest = sqlite3.connect(search_path)
    dest.execute(
        "CREATE VIRTUAL TABLE sermons_fts USING fts5("
        "title, speaker, sermon_series, bible_passage, topics, description, "
        "content_text, transcript_text, sermon_key UNINDEXED, slug UNINDEXED)"
    )
    rows = []
    for m in get_sermons_with_transcripts(conn):
        rows.append((
            m.get('title') or '', m.get('speaker') or '',
            m.get('sermon_series') or '', m.get('bible_passage') or '',
            m.get('sermon_topics') or m.get('topics') or '',
            m.get('description') or '', m.get('content_text') or '',
            m.get('transcript') or '', _sermon_key(m), m.get('slug') or '',
        ))
    dest.executemany(
        "INSERT INTO sermons_fts (title, speaker, sermon_series, bible_passage, topics, "
        "description, content_text, transcript_text, sermon_key, slug) "
        "VALUES (?,?,?,?,?,?,?,?,?,?)", rows)
    dest.commit()
    dest.execute("INSERT INTO sermons_fts(sermons_fts) VALUES('optimize')")
    dest.close()
    return len(rows)


def search_fts(conn, query, limit=50):
    """Full-text search over sermons (incl. transcripts).

    Returns list of merged sermon dicts, best matches first.
    """
    try:
        hits = conn.execute("""
            SELECT sermon_key FROM sermons_fts
            WHERE sermons_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (query, limit)).fetchall()
    except sqlite3.OperationalError:
        return []
    by_key = {}
    for m in get_merged_sermons(conn):
        by_key[_sermon_key(m)] = m
    return [by_key[int(h['sermon_key'])] for h in hits if int(h['sermon_key']) in by_key]