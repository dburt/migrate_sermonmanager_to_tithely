#!/usr/bin/env -S uv run --script

# run_updater.py

import os
import sys
import json
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
JSON_FILE_PATH = "sermons.json"
SERMON_INDEX_PATH = "sermon_index.json"
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
HEADLESS_MODE = False
# ---------------------

def main():
    """Main function to orchestrate the browser automation."""
    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    index_only = len(sys.argv) > 1 and sys.argv[1] == '--index-only'

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
        manager.login()

        if index_only or not os.path.exists(SERMON_INDEX_PATH):
            print("Creating sermon index...")
            sermon_index = manager.create_sermon_index()
            with open(SERMON_INDEX_PATH, "w") as index_file:
                json.dump(sermon_index, index_file, indent=4)
            print(f"Found {len(sermon_index)} sermons in the index.")
            if index_only:
                exit(0)
        else:
            print("Sermon index found. Skipping index creation.")

        updates_by_page = compare_and_group_sermons(manager.page, JSON_FILE_PATH, SERMON_INDEX_PATH)
        
        if not updates_by_page:
            print("No sermons need updating.")
            return

        print(f"Found {sum(len(s) for s in updates_by_page.values())} sermons to update across {len(updates_by_page)} pages.")

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

if __name__ == "__main__":
    main()