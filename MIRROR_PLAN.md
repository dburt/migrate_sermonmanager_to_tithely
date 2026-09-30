# Tithely Data Mirror Plan

## Goal

Maintain a local mirror of the Tithely sermon data as new sermons are added, including
metadata, audio, and transcriptions. Serve the content from a static site
(`dave.burt.id.au/stalfreds-sermons.html`) and lay the groundwork for a future
server that adds full-text transcript search.

## Architecture

```
sermons_with_sizes.csv ──▶ wordpress_sermons (immutable archive)
tithely scrape (sync) ──▶ tithely_sermons   (live mirror, upserted by sync)
                              │                 ▲
                              │                 │ FK
                              ▼                 │
                       v_sermons VIEW ────► transcriptions
                         │                     (nullable FKs to either source)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   sermons.json     podcast_feed.xml    FTS5 (title, series, speaker,
   (static site)    (RSS)                  passage, topics, transcript)
```

- Two source tables keep data provenance clean: `wordpress_sermons` is a preserved,
  immutable legacy archive; `tithely_sermons` is a genuine mirror that the sync
  command owns exclusively.
- A pure SQL `VIEW` (`v_sermons`) is the canonical current/merged record read by
  the site, exports, and FTS. Nothing is materialized.
- Transcriptions attach to whichever source owns the sermon (nullable FK to each
  source table, exactly one non-null).

## Decision summary

| Decision | Choice |
|---|---|
| Audio storage | Mirror audio to D: on Hyperion (via rclone `hyperion:` remote / Tailscale) |
| Sync triggering | Periodic cron job |
| Data merge | Split tables: WordPress legacy + Tithely live, joined by view |
| Serving | Static JSON + HTML first; server for transcript search later |
| Merged record | Pure `VIEW`, not materialized |
| Transcription linkage | FK to source tables |

## Phase 1 — SQLite schema & bootstrap (`sermon_manager/db.py`)

Tables:

- **`wordpress_sermons`** — seeded once from `sermons_with_sizes.csv`. Columns mirror
  the CSV: `id, wordpress_post_id, title, post_date_gmt, permalink, content_text,
  preacher, sermon_series, bible_passage, bible_book, sermon_topics, service_type,
  view_count, audio_url, audio_file_size, melbourne_time`.
- **`tithely_sermons`** — mirrors `tithely_index.json`:
  `id, slug (UNIQUE), title, speaker, date, sermon_series, bible_passage,
  description, audio_url, audio_file_size, local_audio_path, last_seen_at,
  created_at, updated_at`.
- **`transcriptions`** — `id, tithely_sermon_id (nullable FK), wordpress_sermon_id
  (nullable FK), transcript_text, word_count, created_at`. CHECK constraint:
  exactly one FK non-null.
- **`v_sermons` VIEW** — joins on `audio_file_size`. Join quality:
  - Remote: 1412 entries, 1381 with non-zero size, 2 duplicate sizes
    (15164094, 26493722).
  - Local: 1389 entries, 21 with zero size.
  - 1344/1380 remote non-zero sizes match local.
  - Fallback match (title + date) for the 21 zero-size and 2 duplicate-size cases.
  - Tithely wins for shared fields (title, date, series, passage, description,
    audio_url); WordPress fills fields Tithely cannot represent (topics,
    service_type, view_count, post_id, content_text).
- **FTS5 index** over the view's searchable fields + `transcript_text`, joinable
  via the view. Foundation for future full-text transcript search on a server.

Bootstrap also imports the existing 5 `transcripts/*.txt` into `transcriptions`
(linked via the merge).

## Phase 2 — `sync` command (`sermon_manager.py`)

- **`sync`** (default): incremental — paginate the Tithely general listing until the
  first page with zero new/unknown slugs, fetch details/sizes for new ones (reuses
  `TithelyManager` from `core.py`), upsert into `tithely_sermons`, stamp
  `last_seen_at`. Reports `{new, updated, unchanged}`.
- **`sync --full`**: full re-scrape of all pages + details (replacement for the
  current `scrape-index`).
- Merge logic lives only in the seed/export layer — never in sync. Sync owns
  `tithely_sermons` exclusively.

## Phase 3 — `export` command

Generates from `v_sermons`:

- `sermon-archive/sermons.json` (existing client JS shape, for HTML backward
  compatibility).
- `podcast_feed.xml`.

~500KB–1MB JSON, ~150KB gzipped — the existing client-side filter page handles this
scale. When the transcript-search server is added later, FTS5 + the view make it a
read-only query.

## Phase 4 — HTML site update

`stalfreds-sermons.html`:

- Add transcript expand-on-click when a transcription exists.
- Reconcile field naming (speaker/preacher, content_text/description/topics).
- Deploy via rsync as today.

## Phase 5 — Audio mirror → Hyperion via rclone

Extend `audio_mirror.py` to read pending sermons from the DB and use the configured
rclone remote:

- Download to a staging dir, then `rclone copy` to `hyperion:/D:/stalfreds_audio/`
  (SFTP over Tailscale, host `100.91.35.72`, user `dave`, already configured).
- Update `tithely_sermons.local_audio_path` on success; retain manifest/resume
  behaviour.

## Phase 6 — Transcription integration

Extend `transcribe.py`:

- Pull audio for sermons lacking transcripts (local path if present, else CDN URL).
- Run faster-whisper (existing code).
- Store in `transcriptions`; refresh FTS.

## Phase 7 — Cron job

Script run periodically (this machine or Hyperion):

1. `uv run python sermon_manager.py sync`
2. `uv run python sermon_manager.py mirror-audio` → rclone to Hyperion D:
3. `uv run python sermon_manager.py transcribe` (new sermons only)
4. `uv run python sermon_manager.py export`
5. rsync `sermon-archive/` → `dave.burt.id.au`

## Implementation order

1. `db.py` + seed (bootstrap, view, FTS) — foundation
2. `sync` command — makes the mirror live
3. `export` command + HTML site update — minimum viable serving
4. Audio mirror via rclone — resilience on Hyperion
5. Transcription — enable search later
6. Cron — run unattended

## Key facts from current codebase

- 1412 sermons on Tithely (dates Dec 4, 2005 – Mar 1, 2026), 20 speakers,
  161 sermon series, 1381 entries with `audio_file_size`.
- WordPress CSVs: `sermons.csv` (1,389 sermons), `sermons_with_sizes.csv` (adds
  `audio_file_size`).
- Existing join key: `audio_file_size` (from `sermon_manager/gap_analysis.py`).
- Deployment: static rsync to `illuminu@burt.id.au:dave.burt.id.au/`; site at
  `dave.burt.id.au/stalfreds-sermons.html`.
- Hyperion: reachable as rclone remote `hyperion:` (sftp, Tailscale
  `100.91.35.72`, user `dave`) and as Tailscale host `hyperion`. Drives C: and D:
  visible; target `hyperion:/D:/`.
- Existing transcription flow: `transcribe.py` (faster-whisper, medium model,
  CPU), 5 sample transcripts in `transcripts/`.