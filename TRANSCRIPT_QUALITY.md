# Transcript Quality — Findings and Plan

_Status: not started. Written 2026-10-09._

## Decisions (locked)
- Plan doc lives at **`TRANSCRIPT_QUALITY.md`** (repo root).
- Phase 2 scope is the **full corpus**, not just flagged transcripts — with a
  backup/versioning step so nothing is destroyed irreversibly.

## Goal
Improve accuracy and readability of the archive transcripts, and make future quality
changes measurable rather than guessed.

## Current pipeline
Two paths; **cron uses the remote/GPU one.**

| Path | Entry | Model | Call site |
|------|-------|-------|-----------|
| Remote (cron) | `sermon_manager.py transcribe-remote` | `medium` (via `meta.json`) | `hyperion_worker.py:70` |
| Local (manual) | `sermon_manager.py transcribe` | `medium`, `int8`, CPU | `transcriber.py:81` |

- `WhisperModel(model_name, device="cuda", compute_type="auto")` — `hyperion_worker.py:50`.
- Decode: `beam_size=5`, `language="en"`, `initial_prompt` only. **No VAD, no temperature
  fallback, `condition_on_previous_text` left at default `True`.**
- Prompt: `bible_prompt.build_sermon_prompt` (`bible_prompt.py:213`) = metadata + NIV
  passage (≤1,000 chars), NIV cached in `bible_niv_cache.json`.
- Output flattened with `" ".join(seg.text …)`; stored in `transcriptions` (text +
  word count only — `db.py:425`); exported to `sermon-archive/transcripts/<slug>.json`.
- Hardware: Hyperion RTX 4060 Ti, **8GB VRAM**, faster-whisper 1.2.1 (local venv 1.2.0).

## Evidence
- **12 / 1414** transcripts contain an immediate 5-gram repeated ≥3× (loop signature):

  | × | slug | phrase |
  |---|------|--------|
  | 7 | `2015-04-16-risen-and-ascended-6pm` | `no no no no no` |
  | 6 | `2023-10-01-gospel-glory` | `we'd been to the church` |
  | 5 | `2012-09-02-farewell-to-kieran` | `na na na na na` |
  | 4 | `2019-07-15-building-a-secure-future` | `is the final statement which` |
  | 4 | `2010-07-23-women-s-weekend-eternity-5` | `question question question question question` |
  | 3 | `2023-06-25-don-t-let-wealth-be-your-god` | `it's a very prosperous country` |
  | 3 | `2018-02-04-is-jesus-demon-possessed` | `they're not getting any older` |
  | 3 | `2017-11-19-a-new-start-10am` | `peter do you love me` |
  | 3 | `2015-07-30-loving-others` | `were the parents and we` |
  | 3 | `2011-04-10-conversation-ready-promoting-the-gospel-in-daily-conversation` | `do not fear their threats` |
  | 3 | `2010-07-23-women-s-weekend-eternity-1` | `mm mm mm mm mm` |
  | 3 | `2008-02-24-how-to-manage-your-mouth` | `please please please please please` |

  (Musical ones — `na`/`no`/`mm` — need listening before being called bugs.)
- **`St. Alves`** — church's own name mis-transcribed **23×** (`St Alfred'` correct 714×).
- Boilerplate hallucination: 1× each of "thanks for watching/listening".
- **Mirror gap: 1457 sermons have audio, only 1414 files on the mirror (~43 missing).**

## Options
Impact/effort H/M/L. Pointers are the remote/cron path.

**A. Decoding** — 1. `condition_on_previous_text=False` (H/L, `hyperion_worker.py:70`, `transcriber.py:81`); 2. temperature fallback `(0.0…1.0)` (H/L); 3. tune `no_speech_threshold`/`log_prob_threshold` (M/L).

**B. Model** — 4. `medium → distil-large-v3` (H/M, best 8GB fit); 5. or `large-v3` @ `int8_float16` (H/M); 6. record model+params per transcript (M/L).

**C. Audio** — 7. VAD `vad_filter=True` (M/L); 8. ffmpeg mono/16k/loudness (M/M); 9. trim intro/outro music (M/M).

**D. Domain** — 10. Bible-verse normalisation vs cached NIV (H/M); 11. proper-noun fixer, `St. Alves → St Alfred's` (H/L); 12. richer `initial_prompt` glossary (M/L); 13. LLM proofread, guarded (M/H).

**E. Measurement** — 14. QA scorer + `transcript_quality` table (`avg_logprob`, `no_speech_prob`, `compression_ratio`, loop score) (H/M); 15. escalated re-transcription (H/M); 16. hand-corrected gold set → WER, on `compare_data.py`/`test_offline.py` (H/M).

**F. Adjacent** — 17. diarization (`pyannote`) (M/H); 18. keep segment structure (L/L).

## Sequenced plan

**Phase 0 — measure first (no model changes)**
- Add the loop detector (below) as a script; store baseline.
- Build the 5–10 sermon **gold set** (needs a hand-corrector — see Open questions).
- Record throughput via `monitor.py` (already computes transcripts/hour) to size Phase 2.

**Phase 1 — decoding cluster (1 afternoon)**
- Options 1+2+7 in `hyperion_worker.py`, mirrored in `transcriber.py`.
- Re-run the 12 flagged transcripts as a **smoke test** (this is a preview, not the full pass).
- Land Options 6 + 14 first so the effect is recorded.

**Phase 2 — full-corpus re-transcription (committed)**
- **Prerequisite — reconcile audio:** re-run the mirror step
  (`sermon_manager.py mirror-audio-db-cmd`) so all ~1457 audio files are on Hyperion;
  verify mirror count == DB count. 34 sermons have no audio — out of scope.
- **Prerequisite — safety:** back up `sermons.db`; add model/params columns (Option 6) and
  a **generation** marker so the new pass is stored/tagged rather than silently overwriting,
  making rollback possible.
- Run Option 4 (`distil-large-v3`) across the corpus; escalate any still-flagged via Option 15.
- Size from Phase 0 throughput — order of **days of GPU time** (estimate; replace with measured).
- Re-export + deploy via the normal pipeline (`sermon-archive/deploy.bash`).

**Phase 3 — domain wins**
- Option 11 → 10 → 12; re-export + deploy.

## Verification
- Gold-set WER before/after each phase.
- Corpus loop count (detector) — target 0 clear loops.
- `rg --no-ignore -c 'St. Alves'` — target 0.
- Spot-listen 2–3 musical ones to separate repetition from hallucination.

## Reusable loop detector
```python
import json, glob, re
def consecutive_repeats(words, n=5):
    worst, seq, i = 0, None, 0
    while i < len(words) - n:
        g = tuple(words[i:i+n]); k, j = 1, i+n
        while j+n <= len(words) and tuple(words[j:j+n]) == g:
            k += 1; j += n
        if k > worst: worst, seq = k, " ".join(g)
        i = j if k > 1 else i + 1
    return worst, seq
for f in glob.glob("sermon-archive/transcripts/*.json"):
    t = json.load(open(f, encoding="utf-8")).get("transcript") or ""
    w = re.findall(r"[a-z']+", t.lower())
    k, seq = consecutive_repeats(w)
    if k >= 3:
        print(k, f.split("/")[-1], seq)
```

## Risks / notes
- Full-corpus Phase 2 rewrites **all** transcripts — backup + generation tagging is mandatory.
- Audio is incomplete on the mirror (~43); Phase 2 cannot start until reconciled.
- The 1,000-char prompt cap may truncate long passages — check before Option 10 relies on it.
- `stalfreds-sermons.html` renders transcript text; Option 18 must not break it.

## Open questions for the next session
1. Who hand-corrects the gold set, and how many sermons?
2. LLM proofread (Option 13) in scope? Local-on-Hyperion vs API?
3. Keep Whisper segment structure (Option 18)? Front-end impact to confirm.
4. Link this doc from `NOTES.md`?
