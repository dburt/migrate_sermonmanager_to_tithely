### Project Goal

Synchronize the local `sermons.csv` with the Tithely sermon database.

## Current Task List

- [x] Identify and delete duplicate sermons on Tithely.
- [x] Refresh the index to prepare for updating metadata.
- [ ] Analyse the differences between sermons.csv and Tithely.
- [ ] Run the updater script to synchronize metadata from `sermons.csv` to Tithely.
- [ ] Refactor the `tithely_metadata_update` scripts to improve robustness and error handling.
- [ ] Update the `README.md` to reflect the current state of the project and the new workflow.

### Challenges & Discoveries

- The `README.md` is outdated regarding the Tithely update process.
- The modern update mechanism uses browser automation via scripts in the `tithely_metadata_update/` directory, primarily `run_updater.py` and `tithely_manager.py`.

### Current Status & Plan

1.  **Analysis Script Created:** A new script, `analysis_and_grouping.py`, has been written. It reliably matches local (`sermons.csv`) and Tithely (`sermon_index.json`) sermons using audio file size and identifies metadata discrepancies.
2.  **Updater Integrated:** The main `run_updater.py` script has been successfully modified to use the new analysis function.
3.  **Local Cache Updated:** The local audio file size cache (`csv_audio_sizes.csv`) has been refreshed by running `./get_csv_file_sizes.py`.
4.  Duplicate sermons have been identified and removed.
5.  `sermon_index` has been updated.

### Next Steps

