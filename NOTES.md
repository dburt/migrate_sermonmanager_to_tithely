### Project Goal

Synchronize the local `sermons.json` (our canonical local data) with the Tithely sermon database, ensuring data consistency and accuracy.

## Current Task List

- [x] Identify and delete duplicate sermons on Tithely. (This was part of the old workflow, assuming it's done or will be re-evaluated)
- [x] Refresh the index to prepare for updating metadata. (Achieved through new scraping process)
- [x] Analyse the differences between local data and Tithely. (Achieved through `generate_update_report.py`)
- [ ] Run the updater script to synchronize metadata from local data to Tithely.
- [x] Refactor the `tithely_metadata_update` scripts to improve robustness and error handling. (Achieved by separating scraping and enrichment)
- [x] Update the `README.md` to reflect the current state of the project and the new workflow.

### Challenges & Discoveries

- The `README.md` was outdated regarding the Tithely update process.
- Initial attempts at full detail scraping using browser automation (`playwright`) were prone to crashes.
- A more robust approach was developed by separating the initial listing scraping (using `playwright`) from the detail enrichment (using `requests` and `BeautifulSoup` for direct HTTP calls).
- Matching sermons between local and online data is best done using `audio_file_size` for accuracy.

### Current Status & Plan

1.  **Robust Indexing Pipeline Implemented:** A new pipeline has been established for creating and enriching the sermon index:
    *   `selective_importer.py` is used to create basic indexes from either the main listing or podcast listings.
    *   `enrich_sermon_details.py` enriches basic indexes with full sermon details (description, bible passage, audio URL, file size) using direct HTTP requests.
    *   `find_and_enrich_missing_sermons.py` identifies and enriches sermons present in the main listing but not in the podcast.
    *   `merge_enriched_indexes.py` combines all enriched sermon data into a single, comprehensive `sermon_index_combined_enriched_*.json` file.
2.  **Discrepancy Reporting Tool Developed:** `generate_update_report.py` has been created to compare the local `sermons.json` (merged with `csv_audio_sizes.csv` for audio file sizes) against the comprehensive online index (`sermon_index_combined_enriched_*.json`). It identifies:
    *   Sermons with discrepancies in fields like speaker, series, and bible passage.
    *   Sermons only present in local data or only online.
    *   Specific issues like `[post_id=X]` patterns in online sermon series and descriptions.
3.  **Performance Bottleneck Identified:** The `generate_update_report.py` script is currently experiencing significant performance issues (taking hours to run).

### Next Steps

1.  **Diagnose Performance Bottleneck:** Add detailed logging to `generate_update_report.py` to pinpoint the exact section causing the extreme slowness.
2.  **Optimize `generate_update_report.py`:** Based on logging, optimize the script for faster execution.
3.  **Implement Update Script:** Modify `tithely_metadata_update/run_updater.py` (or create a new script) to consume the generated `tithely_update_report_*.json` and apply the necessary updates to Tithely. This includes:
    *   Removing `[post_id=X]` patterns from online sermon series and descriptions.
    *   Updating speaker, series, and bible passage fields based on local data.
    *   Handling sermons that are only local (potentially creating them on Tithely) or only online (potentially deleting them or flagging for review).
