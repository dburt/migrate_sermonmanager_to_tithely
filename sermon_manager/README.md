# Sermon Manager

This directory contains a new, interactive toolset for managing sermon data on the Tithely platform.

## Goal

The purpose of this toolset is to provide a reliable, testable, and interactive way to manage sermon data. It is designed to be used either manually from the command line or orchestrated by an AI agent.

## Tools

The primary entrypoint will be `sermon_manager.py`, a command-line interface (CLI) that will provide subcommands for various actions.

### Planned Commands

- `login`: Authenticate with Tithely and save the session state.
- `list-remote`: List sermons from a Tithely media or podcast page.
- `get-remote`: Get the details of a specific sermon from Tithely.
- `update`: Update a sermon on Tithely with local data.
- `compare`: Compare local and remote sermon data to identify discrepancies.

## Getting Started

1.  **Install Dependencies:**
    ```bash
    uv sync
    ```
2.  **Run the tools:**
    ```bash
    ./sermon_manager.py --help
    ```
