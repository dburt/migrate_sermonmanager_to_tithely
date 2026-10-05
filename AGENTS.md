# Agent-Based Sermon Management Workflow

This document outlines a new, interactive approach for managing sermon data between the local project and the Tithely platform. The goal is to move from large, monolithic scripts to a suite of small, single-responsibility command-line tools. This allows for a more interactive, testable, and reliable workflow, suitable for both manual use and AI agent orchestration.

## Core Principles

-   **Simplicity:** Each tool does one thing and does it well.
-   **Interactivity:** Tools are designed to be used in an interactive shell, providing immediate feedback.
-   **Testability:** Smaller, focused tools are easier to test in isolation.
-   **Composability:** The tools can be chained together in scripts or used by an AI agent to perform complex tasks. Outputting structured data (JSON) to `stdout` and informational messages to `stderr` is crucial for this.
-   **State in Files:** The state will be managed in simple JSON or CSV files, rather than in memory in a long-running process.
-   **Short, Quick Feedback Loops:** Operations should be fast and provide immediate, clear feedback, enabling rapid iteration and testing.

## Proposed Toolset (`sermon_manager/`)

The new toolset is located in the `sermon_manager/` directory. Each tool is a standalone Python script, orchestrated by a central CLI (`sermon_manager.py`).

### Current Capabilities (Implemented Commands)

-   `login`: Authenticate with Tithely.
-   `list-remote`: List sermons from Tithely (general or podcast-specific).
-   `list-local`: List sermons from the local `sermons.csv` (supports single sermon retrieval by audio file size).
-   `get-remote`: Get details for a single sermon from Tithely.
-   `update`: Update a sermon on Tithely using a full JSON object (supports `stdin` input).
-   `get-file-size`: Get the size of an audio file from a URL.
-   `get-wordpress-sermon`: Get a single sermon from a WordPress XML export by `post_id`.
-   `compare`: Compare two sermon data objects.
-   `update-title`: Update the title of a sermon on Tithely.

### Next Steps (Prioritized)

**Archive frontend** (`sermon-archive/`):

1.  ~~**Bring Harbour Cyan back into the resting page.**~~ **Done.** Cyan now marks four
    positions at rest, all on `#00739b` rather than `#0099ce`, because the marks read against
    the `#f4f4f4` canvas where Harbour Cyan is only 2.96:1: a 3px bar on an applied facet
    (with a weight change so the bar is never the sole carrier of state), a 2px rule on the
    sticky year heading, the filter chip's border, and the register row's hover tint
    (`#eaf7fd`). The masthead was left alone — cyan on `#00506c` is 2.73:1. See "The
    Accent-Legibility Rule" in `DESIGN.md`; keep "The One Accent Rule" (≤10% of any screen).
2.  ~~**Fix two measured defects in the normative docs.**~~ **Done.** `DESIGN.md`'s
    `button-primary` now states that a 15px label needs `#00739b` (5.35:1) because white on
    `#0099ce` is 3.26:1, and its Facet Rail entry now describes the built page — no cyan
    fill, no inverted count, and no panel.
3.  **Fix `::selection`.** White on `#0099ce` is 3.26:1 for selected body text; use a cyan
    tint with dark text instead.
4.  **Reduce index DOM weight.** The no-pagination index is one 143,584px document holding 1,489
    entry rows. Measure paint/layout cost, then try `content-visibility: auto` with
    `contain-intrinsic-size` on `.year-group`.
5.  ~~**Reconcile the transcript count.**~~ **Done by describing coverage, not counting it.**
    `PRODUCT.md` had 1,345 transcripts while `sermon-archive/transcripts/` held 1,412. The
    count was never reconcilable in a doc that also says the backlog "drains over days", so
    both figures were dropped in favour of "slightly fewer" and "coverage is incomplete". Do
    not reintroduce a hardcoded transcript count — it drifts by dozens per week. The same
    caution applies to the 1,489 sermon count in that bullet: it is correct today, but it is
    a snapshot.
6.  **Note a standing judgement call.** The ghost `.btn` border (`#e6e6e6` on canvas, 1.13:1)
    is below the 3:1 non-text floor. It is left alone on the judgement that the control is
    identified by its text label rather than its border. Revisit if an audit requires it.

**Sermon manager** (`sermon_manager/`):

7.  **Systematic Review and Fix of `TithelyManager` Instantiation:** Address the recurring `TithelyManager() takes no arguments.` or `AttributeError: 'TithelyManager' object has no attribute 'get_sermon_by_audio_file_size'` errors by ensuring `TithelyManager` is always instantiated correctly with all required arguments (`email`, `password`, `headless`, `_echo`) and that its methods are called properly across all commands.
8.  **Implement Single-Field Updates (Remaining):** Add `update-speaker`, `update-series`, `update-bible-passage`, `update-description` commands, following the pattern of `update-title` once the blocking issue is resolved.
9.  **Refine `compare` command:** Improve the diffing output and handle cases where fields might be missing in one of the sermon objects.
10.  **Implement `search` command:** Develop a command to search local sermon data (e.g., by keywords in title, description, speaker, series).

## Design System & Archive Frontend

The sermon archive web page (`sermon-archive/stalfreds-sermons.html`) is the public face of this project. It is **hand-maintained**: `sermon_manager.py export` regenerates only `sermons.json`, `manifest.json`, `podcast_feed.xml`, `transcripts/`, and `search.db` — it does **not** touch the HTML, CSS or JS. Edit `stalfreds-sermons.html`, `sermon-archive/stalfreds.css` and `sermon-archive/stalfreds.js` directly.

The page carries **its own stylesheet** (`sermon-archive/stalfreds.css`), built entirely from `DESIGN.md` tokens, and **its own script** (`sermon-archive/stalfreds.js`, `defer`, no inline script in the shell); the church's hosted theme stylesheet is no longer imported. Google Fonts (Montserrat, Roboto) is still loaded from its CDN, as are the CloudFront logo and favicon. There is no build step and no bundler: the CSS and JS are shipped as written. Both join `stalfreds-sermons.html` in the `.htaccess` revalidate list and in `deploy.bash`'s rsync list — a new static file must be added to **both**, or it will deploy without revalidating.

The page's shape is the back matter of a hymnal: a faceted, year-grouped index of all sermons (no pagination) that opens into a typeset reading view at `#<slug>`. Filters and the search term live in query params, the open sermon in the hash, so every view is linkable and Back restores scroll position.

Data assets are content-addressed: `export` writes `manifest.json` with a `sermons` and `transcripts` thumbprint (content hash), and the page fetches `sermons.json` and `transcripts/<slug>.json` with `?v=<thumbprint>`. This busts Apache's 2-day `mod_expires` cache while keeping each version cacheable. `search.php` sends `Cache-Control: no-store` itself, and `sermon-archive/.htaccess` sets `no-cache, must-revalidate` on the shell HTML, `stalfreds.css`, and `manifest.json` so deploys go live immediately (ETag makes revalidation a cheap 304).

### Source of Truth

-   **`DESIGN.md`** — the normative design system: palette tokens, typography, elevation, components, and named rules (e.g. "The No-Invented-Blue Rule"). Any visual change to the archive must conform to it; update `DESIGN.md` first if the system genuinely changes.
-   **`PRODUCT.md`** — product truth: who the archive is for and what it must do.
-   **`.impeccable/design.json`** — machine-readable sidecar (colors, ramps, components) consumed by the Impeccable detector. It is generated/gitignored; keep it in sync with `DESIGN.md` when tokens change.

### Tooling

-   **Impeccable skill** (`impeccable`) is the design linter/reviewer. Load it for any UI work.
-   Lint the archive page before committing:
    `npx --no-install impeccable detect --json sermon-archive/stalfreds-sermons.html`
-   Off-palette hex values (`#007bff`, `#0056b3`, `#dc3545`, `#ccc`, `#ddd`, `#eee`, ad-hoc radii) are defects. Map them to the nearest `DESIGN.md` token. The only expected warnings are `overused-font`/`single-font` for Roboto, which is the pinned church brand font.
-   The page must keep exactly one `<h1>` and semantic landmarks (`header`, `nav`, `main`).

### Deploy

Run `bash sermon-archive/deploy.bash` to `export` and rsync the archive to the live host (`illuminu@burt.id.au:dave.burt.id.au/`). Verify the deployed result at `https://dave.burt.id.au/stalfreds-sermons.html`.

