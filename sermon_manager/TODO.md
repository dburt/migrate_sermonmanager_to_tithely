# TODO List for Sermon Manager CLI

This document outlines the current tasks and future plans for the `sermon_manager` command-line interface.

## Current Tasks

1.  **Fix `get-remote` output:** Ensure `get-remote` only outputs JSON when `--output stdout` is used, without extra `click.echo` statements.
2.  **Verify `jq` output:** Re-run the `jq` command to modify sermon data and print to `stdout` (after fixing `get-remote`).
3.  **Update sermon with `stdin`:** Use the verified `jq` output (piped to `stdin`) to update a sermon.
4.  **Verify update:** Fetch sermon details again to confirm changes.
5.  **Revert changes:** Revert the sermon to its original state.

## Future Enhancements

1.  **Implement WordPress export reading:** Add functionality to read sermon data directly from the WordPress XML export.
2.  **Implement `compare` command:** Develop a command to compare local and remote sermon data.
3.  **Implement `get-local` command:** Create a command to retrieve a single sermon from local data by audio file size.
4.  **Implement Single-Field Updates:** Add specific commands for updating individual sermon fields (e.g., `update-title`, `update-speaker`).
5.  **Implement `search` command:** Develop a command to search local sermon data.

## Available Tools (`sermon_manager/sermon_manager.py`)

*   `login [--headless]`: Authenticate with Tithely.
*   `list-remote [--page <int>] [--output <file|stdout>] [--podcast-slug <slug>] [--headless]`: List sermons from Tithely.
*   `list-local [--limit <int>] [--output <file|stdout>]`: List sermons from the local `sermons.csv`.
*   `get-remote <slug> [--output <file|stdout>] [--headless]`: Get details for a single sermon from Tithely.
*   `update <audio_file_size> [--from-file <file>] [--from-stdin] [--page <int>] [--headless]`: Update a sermon on Tithely.
*   `get-file-size <url>`: Get the size of an audio file from a URL.
