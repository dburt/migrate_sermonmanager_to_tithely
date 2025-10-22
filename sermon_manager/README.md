# Sermon Manager

This directory contains a new, interactive toolset for managing sermon data on the Tithely platform.

## Goal

The purpose of this toolset is to provide a reliable, testable, and interactive way to manage sermon data. It is designed to be used either manually from the command line or orchestrated by an AI agent.

## Key Principles

Our goal is to build a simple, flexible, and efficient CLI toolset with short, quick feedback loops. This means:

-   **Simplicity:** Each command should do one thing well. Avoid overly complex commands.
-   **Flexibility & Composability:** Commands are designed to work together, ideally via standard Unix pipes (`|`), allowing users to combine them for complex workflows. Outputting structured data (JSON) to `stdout` and informational messages to `stderr` is crucial for this.
-   **Short, Quick Feedback Loops:** Operations should be fast and provide immediate, clear feedback. This is why we prioritize local data querying and efficient remote interactions.
-   **Responsibility-Based Design:** Logic is encapsulated in classes (e.g., `TithelyManager`, `WordpressParser`) with clear responsibilities.

## Tools

The primary entrypoint will be `sermon_manager.py`, a command-line interface (CLI) that will provide subcommands for various actions.

### Implemented Commands

-   `login [--headless]`: Authenticate with Tithely.
-   `list-remote [--page <int>] [--output <file|stdout>] [--podcast-slug <slug>] [--headless]`: List sermons from Tithely.
-   `list-local [--limit <int>] [--audio-file-size <int>] [--output <file|stdout>]`: List sermons from the local `sermons.csv`.
-   `get-remote <slug> [--output <file|stdout>] [--headless]`: Get details for a single sermon from Tithely.
-   `update <audio_file_size> [--from-file <file>] [--from-stdin] [--page <int>] [--headless]`: Update a sermon on Tithely.
-   `get-file-size <url>`: Get the size of an audio file from a URL.
-   `get-wordpress-sermon <xml_file> <post_id> [--output <file|stdout>]`: Get a single sermon from a WordPress XML export by `post_id`.
-   `compare [--local-file <file>] [--remote-file <file>] [--local-stdin] [--remote-stdin]`: Compare two sermon data objects.
-   `update-title <audio_file_size> <new_title> [--page <int>] [--headless]`: Update the title of a sermon on Tithely.

### Planned Commands

-   `update-speaker <audio_file_size> <new_speaker> [--page <int>] [--headless]`
-   `update-series <audio_file_size> <new_series> [--page <int>] [--headless]`
-   `update-bible-passage <audio_file_size> <new_passage> [--page <int>] [--headless]`
-   `update-description <audio_file_size> <new_description> [--page <int>] [--headless]`
-   `search <query> [--local] [--remote] [--output <file|stdout>]`: Search for sermons.

## Getting Started

1.  **Install Dependencies:**
    ```bash
    uv sync
    ```
2.  **Run the tools:**
    ```bash
    ./sermon_manager.py --help
    ```