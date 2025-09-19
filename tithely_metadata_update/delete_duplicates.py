#!/usr/bin/env -S uv run --script

# delete_duplicates.py

import os
import json
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
DUPLICATES_FILE_PATH = os.path.join(project_root, "duplicates_to_delete.json")
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
HEADLESS_MODE = False
# ---------------------

def main():
    """Main function to delete duplicate sermons."""
    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    if not os.path.exists(DUPLICATES_FILE_PATH):
        print(f"❌ ERROR: Duplicates file not found at {DUPLICATES_FILE_PATH}")
        return

    with open(DUPLICATES_FILE_PATH, 'r') as f:
        sermons_to_delete = json.load(f)

    if not sermons_to_delete:
        print("No sermons to delete.")
        return

    print(f"Found {len(sermons_to_delete)} sermons to delete.")

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
        manager.login()

        manager.page.on("dialog", lambda dialog: dialog.accept())

        for sermon in sermons_to_delete:
            try:
                manager.delete_sermon(sermon)
            except Exception as e:
                print(f"❌ An error occurred while deleting '{sermon.get('title', 'Unknown Sermon')}': {e}")
                print("Continuing to the next sermon...")

        print("\n🎉 All duplicate sermons have been processed.")

if __name__ == "__main__":
    main()
