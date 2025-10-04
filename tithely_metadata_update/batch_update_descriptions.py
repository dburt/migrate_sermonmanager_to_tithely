#!/usr/bin/env -S uv run --script

import os
import argparse
import time
from collections import defaultdict
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
# ---------------------

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Batch update sermon descriptions in Tithe.ly.")
    parser.add_argument("--start-page", type=int, default=1, help="Page number to start from.")
    parser.add_argument("--end-page", type=int, default=None, help="Page number to stop at.")
    parser.add_argument("--headless", action="store_true", help="Run the browser in headless mode.")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay in seconds between processing each sermon.")
    return parser.parse_args()

def main():
    """Main function to orchestrate the batch update."""
    args = parse_arguments()

    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, args.headless) as manager:
        manager.login()

        # Get the full list of sermons
        all_sermons = manager.create_main_listing_index(
            start_page=args.start_page,
            end_page=args.end_page
        )

        print(f"Found {len(all_sermons)} sermons to check across pages {args.start_page} to {args.end_page or 'last'}.")

        if not all_sermons:
            print("No sermons found to update.")
            return

        # Group by page to process them efficiently
        sermons_by_page = defaultdict(list)
        for sermon in all_sermons:
            sermons_by_page[sermon['page_url']].append(sermon)

        for page_url, sermons_on_page in sorted(sermons_by_page.items()):
            print(f"--- Processing Page: {page_url} ---")
            # Navigate to the page once
            manager.page.goto(page_url)
            manager.page.wait_for_load_state("networkidle")

            for sermon_data in sermons_on_page:
                success = manager.edit_sermon_description_in_place(sermon_data)
                if not success:
                    print(f"❌ Failed to update sermon: {sermon_data['title']}")
                
                if args.delay > 0:
                    time.sleep(args.delay)

    print("\n🎉 Batch description update process has finished.")

if __name__ == "__main__":
    main()
