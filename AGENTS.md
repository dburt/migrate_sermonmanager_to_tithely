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
