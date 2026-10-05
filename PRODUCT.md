# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Primary: the maintainer.** A single technical operator (the repository owner) running
`sermon_manager/sermon_manager.py` from their own machine. Their job is to keep the archive
truthful and keep running without babysitting: pull new sermons, mirror audio, transcribe,
export, deploy, and — when a record is wrong on Tithely — find it, compare it against every
other source, and correct it. They are the only user of the CLI, and they are comfortable with
SQLite, shell pipelines, and a long-running scrape.

**Secondary: the parish congregation and visitors.** They arrive at the public archive page
(later on) to find a particular sermon, filter by series/preacher/year/topic, read or listen to
it, and read its transcript. This audience is real but is served by the archive page, not the
toolset, and it is not the audience that product decisions are made for.

## Product Purpose

Hold a complete, trustworthy, locally-owned copy of St Alfred's Anglican Church's entire sermon
archive — every recording from December 2005 to the present — that does not depend on Tithely
remaining available or unchanged, and that can be queried and republished on demand.

Two things follow from that. First, the archive doubles as the migration record: Tithely's
sermon metadata was imported from WordPress and still diverges from the legacy source in places,
so the pipeline exists to reconcile it. Second, because Tithely offers neither export nor
full-text transcript search, this is the only place the whole archive — metadata plus
machine-generated transcripts — is queryable at once.

Success means: every field in every served record can be traced back to the source it came
from; the weekly pipeline completes unattended; and if Tithely disappeared tomorrow the archive
would still stand up and be searchable. The archive is **contingency first**. Tithely remains
the church's main production site with no change currently in view; the archive's deliberately
simple public page doubles as the place experimental features are built and tested.

## Positioning

The only durable, complete, source-attributed record of a 20-year sermon archive that exists
outside the vendor that holds it. A hosting platform that cannot export its own content is not a
backup target; this is. What a neighbouring product could not truthfully copy: the per-field
provenance across three sources of unequal quality, and full-text search over two decades of
transcribed speech — search that the incumbent production site structurally cannot offer.

## Operating Context

- **Unattended weekly run.** `sermon_manager/weekly.bash` is the cron entry point and runs
  `sync` → `mirror-audio-db` → `transcribe-remote` → `export` + deploy. Every stage is
  idempotent and skippable; a large transcription backlog may keep it busy for days, and
  `sermon-remote`/monitor commands exist to report progress. Non-zero exit on a failing stage.
- **A second machine, Hyperion.** Reachable over Tailscale (`100.91.35.72`) and as the rclone
  remote `hyperion:` (SFTP, user `dave`). It holds the mirrored audio on `D:` and runs the
  GPU Whisper transcription worker. Heavy work belongs there, not on the operator's machine.
- **Deployment is rsync.** `sermon-archive/deploy.bash` re-exports from the local DB and pushes
  `stalfreds-sermons.html`, `sermons.json`, `podcast_feed.xml`, `search.php`, `search.db`, and
  `transcripts/` to `illuminu@burt.id.au:dave.burt.id.au/`. There is no build step, no
  bundler, and no package install on the server.
- **Tithely has no usable API for this.** It is driven through Playwright against its own web
  UI, including authenticated edits. Login credentials and the WordPress admin URL live in
  `.env`. Network slowness and race conditions against that UI have been the dominant source of
  pipeline failures historically.
- **Provenance is layered.** `wordpress_sermons` is a seeded, immutable legacy archive;
  `tithely_sermons` is a live mirror owned exclusively by `sync`; the pure SQL view
  `v_sermons` is the canonical merged record that the site, exports, and FTS all read. Tithely
  wins shared fields; WordPress fills what Tithely cannot represent (topics, service type,
  view count, post ID, body text). Merge logic lives only in the seed/export layer, never in
  sync.
- **One historical AI-assisted step.** The first bulk clean of the WordPress CSV was done in
  Gemini in AI Studio (`sermons_cleaned_ai_studio.csv.bak`) and is part of the record's
  provenance. Later cleaning is deterministic Python.
- **Audio lives in three places.** Tithely's CloudFront (the large majority), legacy AWS S3
  buckets (`stamp3` and similar, roughly 43 sermons), and a local rclone mirror on Hyperion.

## Capabilities and Constraints

**Terminology.** Sermon; slug (the stable public key, date + title); series; speaker (Tithely's
field) / preacher (WordPress's field for the same thing — names are not yet reconciled);
Bible passage; service type (e.g. 6pm, 10am, all-age); topics; transcript; `audio_file_size`
in bytes, which is the cross-source join key; `v_sermons` (the canonical merged record).

**Binding constraints confirmed by the maintainer:**

- **Data clarity and consistency with every source.** Each of the legacy WordPress data, the
  AWS-hosted audio, and Tithely must remain individually legible and correctly reconciled. A
  record that silently blends sources is a defect, not a convenience.
- **Simplicity is an ongoing goal for the website.** The public page is the experiment surface;
  it stays simple. Complexity belongs in the pipeline.

**Current architecture facts:** Python 3.13 CLI via `uv`, SQLite (with FTS5) as the single
source of truth, faster-whisper for transcription, and a public surface of one static HTML file
with vanilla JS plus one PHP endpoint (`search.php`) that queries the read-only `search.db`.

**Known technical constraints:**

- Tithely's field set bounds what can be round-tripped back to it: title, speaker, series,
  Bible passage, description. Topics, service type, view count, and body text are
  WordPress-only and will not survive a write to Tithely.
- `audio_file_size` matching is imperfect by nature: some entries have zero size and a few
  sizes collide. Title + date is the established fallback.
- `sermons.json` currently carries no `image_url` or `preacher_image_url` field, although the
  page branches on both. No sermon or preacher imagery renders from the export today.
- The page styles itself with its own `stalfreds.css`, built from the church palette and
  typography in `DESIGN.md`, and loads Montserrat / Roboto from Google Fonts. Its appearance
  no longer depends on the church's hosted theme stylesheet, but still depends on that
  third-party font origin staying reachable.

**Undecided:** whether anything on the archive page moves beyond experiment. Experiments are in
progress; there is no roadmap and no commitment to change the production site.

## Brand Commitments

The archive is deliberately subordinate to the church's identity, not a separate brand. It
presents as "St Alfred's Sermons Archive" for St Alfred's Anglican Church and uses the church's
own assets — logo and favicon — plus the church's Montserrat / Roboto pairing, reproduced
in the archive's own stylesheet. It invents no visual or verbal identity of its own, and must not
imply it is an official second home for the church while Tithely is the production site.

## Evidence on Hand

Real content in this repository and deployed:

- **1,489 sermons** in `sermon-archive/sermons.json`, dated 2005-12-03 → 2026-09-20, spanning
  168 series and 32 preachers, with 1,455 audio URLs. Roughly 1,412 records carry Tithely
  audio, ~43 carry legacy AWS S3 audio.
- **slightly fewer machine-generated transcripts** in `sermon-archive/transcripts/<slug>.json`, each
  with `slug`, `title`, `transcript`, and `word_count`.
- **Live and verified:** `https://dave.burt.id.au/stalfreds-sermons.html`,
  `podcast_feed.xml`, and a working `search.php` FTS endpoint.
- **Source exports:** WordPress XML from 2025-08-05 and 2025-09-22, plus the original cleaned
  CSV (`sermons_with_sizes.csv`, 1,389 sermons). `tithely_index.json`, `gap_report.json`, and
  `bible_niv_cache.json` are working artifacts.
- **Scripture references** are NIV throughout, with a cached NIV corpus used to prime the
  transcription prompts and `ref.ly;niv` deep links used to cite passages.

**Absences future work must not paper over:**

- No sermon or preacher imagery exists in the data; the layout must not assume it will.
- Transcription is machine-generated and its accuracy has never been formally audited. It is a
  finding aid, not an authoritative text.
- There are no usage analytics, no audience research, no testimonials, and no benchmarks for
  the archive page. Any claim about how the congregation uses it would be invention.
- Transcription coverage is incomplete, and the backlog drains over days.

## Product Principles

1. **Provenance before convenience.** Every value must remain traceable to the source it came
   from. Never merge sources into a record that cannot explain itself.
2. **Data clarity is the product.** The maintainer's job is to see what differs between sources
   and why. When a field disagrees, the tool's job is to make the disagreement legible, not to
   resolve it silently.
3. **Simplicity is a standing goal, not a phase.** The public page stays simple on purpose; it
   is where experiments are tried, and the church's identity leads it. Put the complexity in the
   pipeline, where one operator can see all of it.
4. **Contingency means survivable.** The archive has to stand up with Tithely entirely gone.
   Anything that only makes sense while Tithely answers is a convenience, not the archive.
5. **Small tools, fast feedback, safe re-runs.** One job per command, JSON to stdout and
   messages to stderr, idempotent and resumable, and a long unattended run that fails loudly
   rather than halfway.

## Accessibility & Inclusion

No product-specific accessibility requirement has been established. Two facts bear on it and
should shape any future work: the transcripts are machine-generated and unverified, so they are
not a trustworthy substitute for the audio; and the public page carries an archive beginning in
2005 whose access needs were never specified.
