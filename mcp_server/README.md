# MCP Server

The MCP (Master Control Program) Server provides a FastAPI-based API to interact with and manage the St. Alfred's sermon data pipeline. It acts as a bridge between the local data (`sermons.csv`) and the live Tithely platform, allowing for controlled, step-by-step data management tasks.

## Setup and Running

1.  **Environment Variables:** Ensure you have a `.env` file in the project root with your Tithely credentials:
    ```
    TITHELY_EMAIL=your_email@example.com
    TITHELY_PASSWORD=your_password
    ```

2.  **Install Dependencies:**
    ```bash
    uv sync
    ```

3.  **Run the Server:**
    ```bash
    uvicorn mcp_server.main:app --reload
    ```
    The server will be available at `http://127.0.0.1:8000`.

## API Endpoints

The API is designed to be granular and provide quick feedback.

*   `GET /`: Welcome message.
*   `GET /local-sermons`: Get a paginated list of sermons from the local `sermons.csv` file.
*   `POST /explore`: A low-level tool to perform a series of Playwright actions on a given URL for exploration and debugging.
*   ... (More endpoints to be added)

---

# Next Steps

This document outlines potential future work for the MCP server, focusing on simplification, consolidation, testing, and expansion.

## 1. Simplification and Consolidation

*   **Shared Data Module:** Create a shared data loading module (e.g., `data_loader.py`) that handles loading and preparing the `sermons.csv` DataFrame. This can be used by the MCP server and other scripts in the project to ensure consistency and reduce code duplication.
*   **Refactor `TithelyManager`:** As it grows, consider breaking down the `TithelyManager` into smaller, more focused classes. For example, a `SermonScraper` class could handle reading data, while a `SermonEditor` class could handle updates and deletions.
*   **Configuration Management:** Centralize configuration (like file paths, URLs, and selectors) into a single configuration file (e.g., `config.yaml`) instead of hardcoding them in scripts.

## 2. Testing

Implementing a robust testing strategy is crucial for ensuring the reliability of the data pipeline, especially since it interacts with a live website.

*   **Introduce `pytest`:** Add `pytest` to the project for writing and running tests.
*   **Unit Tests:**
    *   Write unit tests for the API endpoints in `main.py`. Use mocking (e.g., `unittest.mock.patch`) to isolate the server logic from the `TithelyManager`.
    *   Write unit tests for individual functions within `TithelyManager`, such as the logic for parsing sermon details from a saved HTML file.
*   **Integration Tests:**
    *   **Fixture-Based Scraping Tests:** Use the saved HTML files in `dom_captures/` as fixtures. Create tests that run the scraping logic from `TithelyManager` against these static files. This allows you to test the selectors and data extraction logic without hitting the live Tithely site, making tests fast and reliable.
    *   **Live "Read-Only" Tests:** Create a small suite of tests that perform read-only operations on the live Tithely site (e.g., logging in and fetching the title of the first sermon). These can be run manually or in a separate CI/CD step to verify that the core interaction with the live site is still working.

## 3. Expansion

*   **Interactive Web UI:** Create a simple, single-page web application (e.g., using vanilla JavaScript or a lightweight framework like Vue.js) that acts as a frontend for the MCP Server API. This UI could:
    *   Display local and online sermons side-by-side.
    *   Show a "diff" of the changes to be applied.
    *   Allow the user to trigger updates for individual sermons with the click of a button.
*   **WebSocket Logging:** For longer-running processes, implement a WebSocket endpoint (`/ws/logs`) that streams log messages in real-time to a connected client (like the web UI). This provides immediate feedback without waiting for a request to complete.
*   **Full Pipeline Integration:** Expand the API to cover other parts of the data pipeline, such as:
    *   An endpoint to trigger the transcription of a sermon's audio file.
    *   An endpoint to regenerate the static `sermon-archive` website.
    *   An endpoint to generate and validate the podcast RSS feed.
