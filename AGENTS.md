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

1.  **Systematic Review and Fix of `TithelyManager` Instantiation:** Address the recurring `TithelyManager() takes no arguments.` or `AttributeError: 'TithelyManager' object has no attribute 'get_sermon_by_audio_file_size'` errors by ensuring `TithelyManager` is always instantiated correctly with all required arguments (`email`, `password`, `headless`, `_echo`) and that its methods are called properly across all commands.
2.  **Implement Single-Field Updates (Remaining):** Add `update-speaker`, `update-series`, `update-bible-passage`, `update-description` commands, following the pattern of `update-title` once the blocking issue is resolved.
3.  **Refine `compare` command:** Improve the diffing output and handle cases where fields might be missing in one of the sermon objects.
4.  **Implement `search` command:** Develop a command to search local sermon data (e.g., by keywords in title, description, speaker, series).

## Design System & Archive Frontend

The sermon archive web page (`sermon-archive/stalfreds-sermons.html`) is the public face of this project. It is **hand-maintained**: `sermon_manager.py export` regenerates only `sermons.json`, `podcast_feed.xml`, `transcripts/`, and `search.db` — it does **not** touch the HTML. Edit the HTML directly.

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

