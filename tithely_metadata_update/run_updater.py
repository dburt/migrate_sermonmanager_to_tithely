#!/usr/bin/env -S uv run --script

# run_updater.py

import os
import sys
import json
import argparse
import pandas as pd
from datetime import datetime
from tithely_manager import TithelyManager
from analysis_and_grouping import find_sermons_to_update

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.dirname(script_dir)

SERMONS_CSV_PATH = os.path.join(project_root, "sermons.csv")
CSV_AUDIO_SIZES_PATH = os.path.join(project_root, "csv_audio_sizes.csv")
SERMON_INDEX_PATH = os.path.join(project_root, "sermon_index.json")

BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
HEADLESS_MODE = False
# ---------------------

def main():
    """Main function to orchestrate the browser automation."""
    parser = argparse.ArgumentParser(description="Update Tithely sermon metadata.")
    parser.add_argument("--index-only", action="store_true", help="Only create the sermon index.")
    parser.add_argument("--full-details", action="store_true", help="Enrich the index with full details.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the update process without making changes.")
    parser.add_argument("--limit", type=int, help="Limit the number of sermons to process.")
    args = parser.parse_args()

    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
        manager.login()

        if args.index_only or not os.path.exists(SERMON_INDEX_PATH):
            print("Creating sermon index...")
            sermon_index = manager.create_sermon_index(full_details=args.full_details, with_audio_urls=args.full_details)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            timestamped_index_path = os.path.join(project_root, f"sermon_index_{timestamp}.json")
            
            with open(timestamped_index_path, "w") as index_file:
                json.dump(sermon_index, index_file, indent=4)
            print(f"Sermon index saved to {timestamped_index_path}")

            if os.path.exists(SERMON_INDEX_PATH) or os.path.islink(SERMON_INDEX_PATH):
                os.remove(SERMON_INDEX_PATH)
            os.symlink(os.path.basename(timestamped_index_path), SERMON_INDEX_PATH)
            print(f"Symlink sermon_index.json updated to point to the latest index file.")
            print(f"Found {len(sermon_index)} sermons in the index.")
            if args.index_only:
                return
        else:
            print("Sermon index found. Skipping index creation.")

        updates_by_page = find_sermons_to_update(SERMONS_CSV_PATH, CSV_AUDIO_SIZES_PATH, SERMON_INDEX_PATH)
        
        if not updates_by_page:
            print("No sermons need updating.")
            return

        total_sermons_to_update = sum(len(s) for s in updates_by_page.values())
        print(f"Found {total_sermons_to_update} sermons to update across {len(updates_by_page)} pages.")

        processed_count = 0
        for page_url, sermons_to_update in updates_by_page.items():
            if args.limit and processed_count >= args.limit:
                break

            for sermon in sermons_to_update:
                if args.limit and processed_count >= args.limit:
                    break
                
                print(f"Processing sermon: {sermon['title_local']}")
                if args.dry_run:
                    print("  [DRY RUN] Would update the following fields:")
                    for discrepancy in sermon.get('discrepancies', []):
                        field_map = {
                            'speaker': 'preacher',
                            'series': 'sermon_series_local',
                            'passage': 'bible_passage_local'
                        }
                        local_key = field_map.get(discrepancy, discrepancy + '_local')
                        value = sermon.get(local_key)
                        display_value = value if pd.notna(value) else "(empty)"
                        print(f"    - {discrepancy}: '{display_value}'")
                else:
                    try:
                        manager.update_sermon(sermon)
                    except Exception as e:
                        print(f"❌ An error occurred while processing '{sermon.get('title_local', 'Unknown Sermon')}': {e}")
                        print("Reloading the page to recover...")
                        manager.page.reload()
                        print(f"Current URL: {manager.page.url}")
                
                processed_count += 1

        print(f"\n🎉 {processed_count} sermons have been processed.")

if __name__ == "__main__":
    main()
