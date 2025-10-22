# TODO List for Sermon Manager CLI

This document outlines the current tasks and future plans for the `sermon_manager` command-line interface.

## Current Status

-   **Output Refactoring:** Implemented common output handling to `stdout` or file, with informational messages directed to `stderr`.
-   **Unique ID:** Switched to using audio file size in bytes as the unique identifier for sermons.
-   **Stdin Input:** `update` command now accepts sermon data from `stdin`.
-   **Full Update Functionality:** `update` command can now update multiple sermon fields (title, speaker, series, bible passage, description).
-   **WordPress Export Reading:** `get-wordpress-sermon` command can parse WordPress XML exports and extract sermon data by `post_id`.
-   **Local CSV Querying:** `list-local` command can now retrieve a single sermon from `sermons.csv` by `audio_file_size`.
-   **Audio File Size Caching:** `list-local` caches calculated audio file sizes to `sermons_with_sizes.csv` for faster subsequent access.
-   **`compare` command:** Basic implementation done.
-   **`update-title` command:** Implemented, but currently blocked by `TithelyManager` instantiation issues.

## Blocking Issue: `TithelyManager` Instantiation

The primary blocking issue is a recurring `TithelyManager() takes no arguments.` or `AttributeError: 'TithelyManager' object has no attribute 'get_sermon_by_audio_file_size'` error. This indicates a fundamental problem with how `TithelyManager` is being instantiated or how its methods are being accessed across different commands. This needs a systematic review and correction.

## Key Principles of the System

Our goal is to build a simple, flexible, and efficient CLI toolset with short, quick feedback loops. This means:

-   **Simplicity:** Each command should do one thing well. Avoid overly complex commands.
-   **Flexibility & Composability:** Commands should be designed to work together, ideally via standard Unix pipes (`|`), allowing users to combine them for complex workflows. Outputting structured data (JSON) to `stdout` and informational messages to `stderr` is crucial for this.
-   **Short, Quick Feedback Loops:** Operations should be fast and provide immediate, clear feedback. This is why we prioritize local data querying and efficient remote interactions.
-   **Responsibility-Based Design:** Logic is encapsulated in classes (e.g., `TithelyManager`, `WordpressParser`) with clear responsibilities.

## Next Steps (Prioritized)

1.  **Systematic Review and Fix of `TithelyManager` Instantiation:** Go through `sermon_manager.py` and `core.py` to ensure `TithelyManager` is always instantiated correctly with all required arguments (`email`, `password`, `headless`, `_echo`) and that its methods are called properly.
2.  **Implement Single-Field Updates (Remaining):** Add `update-speaker`, `update-series`, `update-bible-passage`, `update-description` commands, following the pattern of `update-title` once the blocking issue is resolved.
3.  **Refine `compare` command:** Improve the diffing output and handle cases where fields might be missing in one of the sermon objects.
4.  **Implement `search` command:** Develop a command to search local sermon data (e.g., by keywords in title, description, speaker, series).

## Available Tools (`sermon_manager/sermon_manager.py`)

*   `login [--headless]`: Authenticate with Tithely.
*   `list-remote [--page <int>] [--output <file|stdout>] [--podcast-slug <slug>] [--headless]`: List sermons from Tithely.
*   `list-local [--limit <int>] [--audio-file-size <int>] [--output <file|stdout>]`: List sermons from the local `sermons.csv`.
*   `get-remote <slug> [--output <file|stdout>] [--headless]`: Get details for a single sermon from Tithely.
*   `update <audio_file_size> [--from-file <file>] [--from-stdin] [--page <int>] [--headless]`: Update a sermon on Tithely.
*   `get-file-size <url>`: Get the size of an audio file from a URL.
*   `get-wordpress-sermon <xml_file> <post_id> [--output <file|stdout>]`: Get a single sermon from a WordPress XML export by `post_id`.
*   `compare [--local-file <file>] [--remote-file <file>] [--local-stdin] [--remote-stdin]`: Compare two sermon data objects.
*   `update-title <audio_file_size> <new_title> [--page <int>] [--headless]`: Update the title of a sermon on Tithely.
