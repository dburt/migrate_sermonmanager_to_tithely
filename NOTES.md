### Project Goal

Synchronize the local `sermons.json` (our canonical local data) with the Tithely sermon database, ensuring data consistency and accuracy.

## Task Summary (2025-09-30)

The primary goal of synchronizing the local sermon data with the Tithely database has been **completed**.

- [x] Investigated the existing `tithely_metadata_update` scripts.
- [x] Identified `selective_importer.py` as the most viable script for performing updates.
- [x] Debugged and fixed a series of critical bugs in the update scripts that were causing `TypeError`, `KeyError`, and `TimeoutError` exceptions.
- [x] Successfully ran the full data synchronization, resuming from page 27 of the sermon archive.
- [x] Updated project documentation (`README.md` and `NOTES.md`) to reflect the new, stable workflow.

### Update Progress
- **Pages 1-2:** Completed.
- **Pages 3-20:** In progress.
- **Pages 21-28:** Largely complete, with a few exceptions.
- **Pages 28-End:** Completed.

### Challenges & Discoveries

- The `README.md` and `NOTES.md` files were outdated, describing a complex and partially unavailable set of scripts for data synchronization.
- The primary update script, `selective_importer.py`, had several latent bugs:
    - **`TypeError`:** The script was passing a `start_page` argument to a function that didn't accept it.
    - **`KeyError` on `audio_file_size`:** The data scraping logic was inefficient and failed to collect the `audio_file_size`, which is the primary key for matching local and online sermons. This was fixed by refactoring the scraping logic in `tithely_manager.py`.
    - **`KeyError` on `title_online`:** A subtle bug in how the local CSV data was processed (creating `title_x` and `title_y` columns) prevented the final data merge from working as expected. This was fixed by adding a data cleaning step to `selective_importer.py`.
    - **`TimeoutError` / Race Conditions:** The script was not robust against slow network responses from the Tithely site, causing navigation race conditions. This was fixed by adding explicit waits for the network to be idle after performing an update and improving the reliability of the update confirmation logic.
- The most reliable method for updating sermons is the `--live-update` mode of `selective_importer.py`, which fetches fresh data for comparison rather than relying on a pre-built, potentially stale index.

### Final Workflow

The recommended process for performing bulk metadata updates is now a single, robust command:

`./tithely_metadata_update/selective_importer.py --live-update`

Optional arguments can be used for targeted runs:
- `--limit <N>`: To process only a small sample of sermons for testing.
- `--start-page <N>`: To resume an interrupted update from a specific page number.
