#!/usr/bin/env -S uv run --script

# selective_importer.py

import json
import os
import sys
import argparse
from collections import defaultdict
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
HEADLESS_MODE = False
# ---------------------

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Selectively import and update sermons in Tithe.ly.")
    parser.add_argument("--local-sermons", default="sermons.json", help="Path to the local sermons JSON file.")
    parser.add_argument("--sermon-index", default="sermon_index.json", help="Path to the sermon index JSON file.")
    parser.add_argument("--create-index", action="store_true", help="Create a new sermon index from Tithe.ly.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making any changes.")
    return parser.parse_args()

def main():
    """Main function to orchestrate the selective import."""
    args = parse_arguments()

    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    if args.create_index:
        print("Creating a new sermon index from Tithe.ly...")
        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
            manager.login()
            sermon_index = manager.create_sermon_index(with_audio_urls=True)
            with open(args.sermon_index, "w") as f:
                json.dump(sermon_index, f, indent=4)
            print(f"Sermon index with {len(sermon_index)} entries created at {args.sermon_index}")
        return

    if not os.path.exists(args.local_sermons):
        print(f"❌ ERROR: Local sermons file not found at {args.local_sermons}")
        return

    if not os.path.exists(args.sermon_index):
        print(f"❌ ERROR: Sermon index file not found at {args.sermon_index}. Use --create-index to create it.")
        return

    with open(args.local_sermons, 'r') as f:
        local_sermons = json.load(f)

    with open(args.sermon_index, 'r') as f:
        online_sermons = json.load(f)

    print(f"Loaded {len(local_sermons)} local sermons and {len(online_sermons)} online sermons.")

    # --- Comparison Logic ---
    local_sermons_by_title = defaultdict(list)
    for s in local_sermons:
        local_sermons_by_title[s['title']].append(s)

    online_sermons_by_title = defaultdict(list)
    for s in online_sermons:
        online_sermons_by_title[s['title']].append(s)

    needs_update = []
    local_only = []
    online_only = set(s['title'] for s in online_sermons)

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
        for title, local_sermon_list in local_sermons_by_title.items():
            if title in online_sermons_by_title:
                online_sermon_list = online_sermons_by_title[title]
                online_only.discard(title)

                if len(local_sermon_list) > 1 or len(online_sermon_list) > 1:
                    # Handle duplicates with file size matching
                    for local_sermon in local_sermon_list:
                        found_match = False
                        for online_sermon in online_sermon_list:
                            if 'file_size_bytes' not in online_sermon:
                                online_sermon['file_size_bytes'] = manager.get_file_size(online_sermon['audio_url'])
                            
                            if local_sermon.get('file_size_bytes') == online_sermon.get('file_size_bytes'):
                                if needs_update_check(local_sermon, online_sermon):
                                    needs_update.append((local_sermon, online_sermon))
                                found_match = True
                                break
                        if not found_match:
                            local_only.append(local_sermon)
                else:
                    # Only one sermon with this title, compare directly
                    local_sermon = local_sermon_list[0]
                    online_sermon = online_sermon_list[0]
                    if needs_update_check(local_sermon, online_sermon):
                        needs_update.append((local_sermon, online_sermon))
            else:
                local_only.extend(local_sermon_list)

    print("\n--- Comparison Report ---")
    print(f"{len(needs_update)} sermons need updating.")
    print(f"{len(local_only)} sermons are local-only.")
    print(f"{len(online_only)} sermons are online-only.")

    if args.dry_run:
        print("\nDry run complete. No changes were made.")
        return

    # --- Update Logic ---
    if needs_update and not args.dry_run:
        print("\nUpdating sermons...")
        updates_by_page = defaultdict(list)
        for local_sermon, online_sermon in needs_update:
            update_data = {**local_sermon, **online_sermon}
            updates_by_page[online_sermon['page_url']].append(update_data)

        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
            manager.login()
            for page_url, sermons_to_update in updates_by_page.items():
                print(f"\n--- Navigating to page: {page_url} ---")
                manager.page.goto(page_url)
                for sermon in sermons_to_update:
                    try:
                        print(f"Processing sermon: {sermon['title']}")
                        edit_button = manager.page.locator(f"a.js-sermon-form-link[href^='{sermon['edit_url']}/edit']")
                        edit_button.click()
                        
                        manager.fill_and_submit_sermon_form(sermon)
                        
                        manager.page.goto(page_url)

                    except Exception as e:
                        print(f"❌ An error occurred while processing '{sermon.get('title', 'Unknown Sermon')}': {e}")
                        print("Reloading the page to recover...")
                        manager.page.reload()
                        print(f"Current URL: {manager.page.url}")

        print("\n🎉 All sermons have been processed.")

def needs_update_check(local_sermon, online_sermon):
    """Checks if an online sermon needs to be updated based on local data."""
    return (
        local_sermon.get("preacher") != online_sermon.get("speaker") or
        local_sermon.get("sermon_series") != online_sermon.get("sermon_series") or
        local_sermon.get("bible_passage") != online_sermon.get("bible_passage")
    )


if __name__ == "__main__":
    main()
