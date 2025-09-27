#!/usr/bin/env -S uv run --script

# run_updater.py

import os
import sys
import json
import time
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
    parser.add_argument("--start-page", type=int, default=1, help="Page number to start processing from.")
    parser.add_argument("--max-retries", type=int, default=3, help="Maximum number of retries for a single sermon.")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay in seconds between processing each sermon.")
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

        # Convert to list for slicing
        pages_to_process = list(updates_by_page.items())

        # Implement Resume Logic
        if args.start_page > 1:
            start_index = -1
            for i, (page_url, _) in enumerate(pages_to_process):
                if f"page={args.start_page}" in page_url:
                    start_index = i
                    break
            if start_index != -1:
                print(f"--- Resuming from page {args.start_page} ---")
                pages_to_process = pages_to_process[start_index:]
            else:
                print(f"⚠️ Warning: Could not find start page {args.start_page}. Starting from the beginning.")

        processed_count = 0
        for page_url, sermons_to_update in pages_to_process:
            if args.limit and processed_count >= args.limit:
                break

            for sermon in sermons_to_update:
                if args.limit and processed_count >= args.limit:
                    break
                
                sermon_title = sermon.get('title_local', 'Unknown Sermon')
                
                # Implement Retry Logic
                for attempt in range(args.max_retries):
                    try:
                        print(f"[{datetime.now()}] Processing sermon: {sermon_title} (Attempt {attempt + 1}/{args.max_retries})")
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
                            manager.update_sermon(sermon)
                        
                        # Success, break the retry loop
                        break

                    except Exception as e:
                        print(f"❌ An error occurred while processing '{sermon_title}': {e}")
                        if attempt < args.max_retries - 1:
                            print("Attempting to recover and retry...")
                            try:
                                # A more robust recovery: navigate to a known good page
                                manager.page.goto("https://stalfreds.tithelysetup.com/media/listing", wait_until="domcontentloaded")
                                print("Recovery successful.")
                            except Exception as recovery_e:
                                print(f"❌ CRITICAL: Recovery failed: {recovery_e}")
                                print("Aborting script to prevent further errors.")
                                raise  # Re-raise the exception to stop the script
                        else:
                            print(f"❌ Failed to process sermon '{sermon_title}' after {args.max_retries} attempts. Skipping.")

                processed_count += 1
                if args.delay > 0 and not args.dry_run:
                    # print(f"--- Delaying for {args.delay} second(s) ---")
                    time.sleep(args.delay)

        print(f"\n🎉 {processed_count} sermons have been processed.")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
