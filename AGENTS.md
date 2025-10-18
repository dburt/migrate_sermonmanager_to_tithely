# Agent-Based Sermon Management Workflow

This document outlines a new, interactive approach for managing sermon data between the local project and the Tithely platform. The goal is to move from large, monolithic scripts to a suite of small, single-responsibility command-line tools. This allows for a more interactive, testable, and reliable workflow, suitable for both manual use and AI agent orchestration.

## Core Principles

- **Single Responsibility:** Each tool does one thing and does it well.
- **Interactivity:** Tools are designed to be used in an interactive shell, providing immediate feedback.
- **Testability:** Smaller, focused tools are easier to test in isolation.
- **Composability:** The tools can be chained together in scripts or used by an agent to perform complex tasks.
- **State in Files:** The state will be managed in simple JSON or CSV files, rather than in memory in a long-running process.

## Proposed Toolset (`sermon_manager/`)

The new toolset will be located in the `sermon_manager/` directory. Each tool will be a standalone Python script.

### 1. `sermon_manager.py` - The Main CLI

A central CLI tool using a library like `click` or `argparse` to provide access to all the functionality.

**Example Usage:**

```bash
./sermon_manager.py login --test
./sermon_manager.py list-remote --page 2 --output results/remote_sermons_page_2.json
./sermon_manager.py get-remote-sermon <slug> --output results/sermon.json
./sermon_manager.py update-sermon <slug> --from-file local_sermon.json
./sermon_manager.py compare --remote-file remote_sermons.json --local-file local_sermons.json
```

### 2. Core Library (`sermon_manager/src/`)

The core logic for interacting with Tithely will be encapsulated in a library within the `sermon_manager` directory. This will be a refactored and improved version of the existing `TithelyManager`.

- **`client.py`:** A class responsible for Playwright browser management, login, and logout.
- **`scraper.py`:** Functions for scraping sermon listings and individual sermon pages.
- **`editor.py`:** Functions for updating sermons.
- **`models.py`:** Pydantic models for sermon data for validation and type safety.

## Development Plan

1.  **Setup:** Create the `sermon_manager` directory with a `README.md` and a basic `pyproject.toml` for managing dependencies with `uv`.
2.  **Login:** Implement the `login` command. This will be the first and most important tool to build, as it's the entry point for all other interactions. It will store the browser state (cookies, etc.) in a file to be reused by other commands.
3.  **List Remote:** Implement the `list-remote` command to fetch a list of sermons from Tithely.
4.  **Get Remote Sermon:** Implement `get-remote-sermon` to fetch details for a single sermon.
5.  **Update Sermon:** Implement `update-sermon`.
6.  **Compare:** Implement a `compare` tool to show differences between local and remote data.
7.  **Iterate:** Continue to build out the toolset, adding features and refining the workflow as needed.