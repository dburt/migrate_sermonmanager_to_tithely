#!/usr/bin/env -S uv run --script

# selective_importer.py

import json
import os
import sys
import time
import argparse
import pandas as pd
from collections import defaultdict
from datetime import datetime
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
# ---------------------

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Selectively import and update sermons in Tithe.ly.")
    parser.add_argument("--sermon-index", default="sermon_index.json", help="Path to the sermon index JSON file.")
    parser.add_argument("--csv-sermons", default="sermons.csv", help="Path to the cleaned local sermons CSV file.")
    parser.add_argument("--create-index", action="store_true", help="Create a new sermon index from Tithe.ly.")
    parser.add_argument("--enrich", action="store_true", help="Enrich with details and audio URL from sermon pages.")
    parser.add_argument("--with-file-sizes", action="store_true", help="Fetch audio file sizes (requires --enrich).")
    parser.add_argument("--update", action="store_true", help="Update sermons in Tithe.ly with data from the local CSV, using a pre-built index.")
    parser.add_argument("--live-update", action="store_true", help="Update sermons by crawling the live site without a pre-built index.")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of sermons to process.")
    parser.add_argument("--headless", action="store_true", help="Run the browser in headless mode.")
    parser.add_argument("--debug", action="store_true", help="Open a browser in debug mode on a specific sermon.")
    parser.add_argument("--start-page", type=int, default=1, help="Page number to start sermon indexing from.")
    parser.add_argument("--listing-url", default="/media/listing", help="URL path for the sermon listing (e.g., /media/listing or /podcasts/your-podcast-slug).")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay in seconds between processing each sermon.")
    return parser.parse_args()

def main():
    """Main function to orchestrate the selective import."""
    args = parse_arguments()

    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    headless_mode = args.headless if not args.debug else False

    # New Live Update Mode
    if args.live_update:
        print("--- Starting Live Crawl and Update ---")
        
        csv_sermons_path = args.csv_sermons
        csv_audio_sizes_path = "csv_audio_sizes.csv"

        if not os.path.exists(csv_sermons_path):
            print(f"❌ ERROR: Local sermons CSV file not found at {csv_sermons_path}.")
            return
        if not os.path.exists(csv_audio_sizes_path):
            print(f"❌ ERROR: CSV audio sizes file not found at {csv_audio_sizes_path}.")
            return

        # Load local data once
        local_sermons_df = pd.read_csv(csv_sermons_path)
        csv_audio_sizes_df = pd.read_csv(csv_audio_sizes_path)
        local_sermons_df['post_id'] = local_sermons_df['post_id'].astype(int)
        csv_audio_sizes_df['post_id'] = csv_audio_sizes_df['post_id'].astype(int)
        local_sermons_df = pd.merge(local_sermons_df, csv_audio_sizes_df, on='post_id', how='left')

        # Clean up columns from the local merge that created _x and _y suffixes
        if 'title_x' in local_sermons_df.columns:
            local_sermons_df = local_sermons_df.rename(columns={'title_x': 'title'})
        if 'title_y' in local_sermons_df.columns:
            local_sermons_df = local_sermons_df.drop(columns=['title_y'])
        if 'audio_url_x' in local_sermons_df.columns:
            local_sermons_df = local_sermons_df.rename(columns={'audio_url_x': 'audio_url'})
        if 'audio_url_y' in local_sermons_df.columns:
            local_sermons_df = local_sermons_df.drop(columns=['audio_url_y'])

        print(f"Loaded {len(local_sermons_df)} local sermons for matching.")

        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, headless_mode) as manager:
            manager.login()

            # This logic is similar to create_index, but processes updates immediately
            online_sermons = manager.create_main_listing_index(
                listing_url=args.listing_url,
                full_details=True, # Must be true to get edit_url
                detail_scrape_limit=args.limit,
                with_audio_urls=True, # Must be true to get audio_file_size
                start_page=args.start_page
            )
            
            online_sermons_df = pd.DataFrame(online_sermons)
            
            # Merge with local data
            merged_df = pd.merge(
                online_sermons_df, 
                local_sermons_df, 
                left_on='audio_file_size', 
                right_on='audio_file_size',
                suffixes=('_online', '_local')
            )
            
            sermons_to_update = merged_df.to_dict('records')
            
            if args.limit:
                sermons_to_update = sermons_to_update[:args.limit]
                
            print(f"Found {len(sermons_to_update)} sermons with matching audio file sizes to check for updates.")

            if not sermons_to_update:
                return

            # Group by page to minimize navigation
            updates_by_page = defaultdict(list)
            for sermon in sermons_to_update:
                updates_by_page[sermon['page_url']].append(sermon)

            for page_url, sermons in sorted(updates_by_page.items()):
                print(f"--- Processing page: {page_url} ---")
                for sermon_data in sermons:
                    # Here you could add more sophisticated discrepancy checks if needed
                    print(f"Updating sermon: {sermon_data['title_online']} -> {sermon_data['title_local']}")
                    success = manager.update_sermon(sermon_data)
                    if not success:
                        print(f"❌ Failed to update sermon: {sermon_data['title_local']}")
                    
                    if args.delay > 0:
                        time.sleep(args.delay)

        print("\n🎉 Live update process has finished.")
        return

    if args.create_index:
        print("Creating a new sermon index from Tithe.ly list pages...")
        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, headless_mode) as manager:
            manager.login()
            
            if args.listing_url.startswith("/podcasts/"):
                print(f"Scraping podcast listing from: {args.listing_url}")
                sermon_index = manager.create_podcast_index(
                    listing_url=args.listing_url,
                    full_details=args.enrich,
                    detail_scrape_limit=args.limit,
                    with_audio_urls=args.with_file_sizes
                )
            else:
                print(f"Scraping main sermon listing from: {args.listing_url}")
                sermon_index = manager.create_main_listing_index(
                    listing_url=args.listing_url,
                    full_details=args.enrich,
                    detail_scrape_limit=args.limit,
                    with_audio_urls=args.with_file_sizes
                )
            
            datestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            output_filename = f"sermon_index_{datestamp}.json"
            
            with open(output_filename, "w") as f:
                json.dump(sermon_index, f, indent=4)
            print(f"Sermon index with {len(sermon_index)} entries created at {output_filename}")

            # Update symlink
            symlink_path = "sermon_index.json"
            if os.path.lexists(symlink_path):
                os.remove(symlink_path)
            os.symlink(output_filename, symlink_path)
            print(f"Updated symlink '{symlink_path}' to point to '{output_filename}'")
        return

    if args.debug:
        print("--- Running in Debug Mode ---")
        
        sermon_index_path = args.sermon_index
        csv_audio_sizes_path = "csv_audio_sizes.csv"

        if not os.path.exists(sermon_index_path):
            print(f"❌ ERROR: Sermon index file not found at {sermon_index_path}. Use --create-index to create it first.")
            return
        if not os.path.exists(csv_audio_sizes_path):
            print(f"❌ ERROR: CSV audio sizes file not found at {csv_audio_sizes_path}. Please generate it first.")
            return

        with open(sermon_index_path, 'r') as f:
            sermon_index = json.load(f)
        
        if not sermon_index:
            print("Sermon index is empty. Nothing to debug.")
            return

        csv_sizes_df = pd.read_csv(csv_audio_sizes_path)
        csv_audio_sizes = set(csv_sizes_df['audio_file_size'].dropna().astype(int))

        target_sermon = None
        for sermon in sermon_index:
            if sermon.get('audio_file_size') in csv_audio_sizes:
                target_sermon = sermon
                break
        
        if not target_sermon:
            print("❌ Could not find a sermon in the index that has a matching entry in the CSV audio sizes file.")
            return
            
        print(f"Targeting sermon: '{target_sermon['title']}' (Size: {target_sermon['audio_file_size']}) for debugging.")

        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, False) as manager:
            manager.debug_sermon_page(target_sermon['page_url'], target_sermon['edit_url'])
        return

    if args.update:
        print("--- Starting Sermon Update ---")
        
        sermon_index_path = args.sermon_index
        csv_sermons_path = args.csv_sermons
        csv_audio_sizes_path = "csv_audio_sizes.csv"

        if not os.path.exists(sermon_index_path):
            print(f"❌ ERROR: Sermon index file not found at {sermon_index_path}.")
            return
        if not os.path.exists(csv_sermons_path):
            print(f"❌ ERROR: Local sermons CSV file not found at {csv_sermons_path}.")
            return
        if not os.path.exists(csv_audio_sizes_path):
            print(f"❌ ERROR: CSV audio sizes file not found at {csv_audio_sizes_path}.")
            return

        # Load data
        online_sermons_df = pd.DataFrame(json.load(open(sermon_index_path)))
        local_sermons_df = pd.read_csv(csv_sermons_path)
        csv_audio_sizes_df = pd.read_csv(csv_audio_sizes_path)

        # Ensure post_id is of the same type before merging
        local_sermons_df['post_id'] = local_sermons_df['post_id'].astype(int)
        csv_audio_sizes_df['post_id'] = csv_audio_sizes_df['post_id'].astype(int)

        # Add audio_file_size to local_sermons_df
        local_sermons_df = pd.merge(
            local_sermons_df,
            csv_audio_sizes_df,
            on='post_id',
            how='left'
        )
        
        # Merge dataframes
        merged_df = pd.merge(
            online_sermons_df, 
            local_sermons_df, 
            left_on='audio_file_size', 
            right_on='audio_file_size',
            suffixes=('_online', '_local')
        )
        
        # Rename columns for clarity
        merged_df = merged_df.rename(columns={
            'title_local': 'title',
            'sermon_series_local': 'sermon_series',
            'bible_passage_local': 'bible_passage'
        })

        sermons_to_update = merged_df.to_dict('records')
        
        if args.limit:
            sermons_to_update = sermons_to_update[:args.limit]
            
        print(f"Found {len(sermons_to_update)} sermons to update.")

        if not sermons_to_update:
            return

        updates_by_page = defaultdict(list)
        for sermon in sermons_to_update:
            updates_by_page[sermon['page_url']].append(sermon)

        pages_to_process = sorted(updates_by_page.keys())
        
        if args.start_page > 1:
            sermon_index_path = args.sermon_index
            if os.path.exists(sermon_index_path):
                with open(sermon_index_path, 'r') as f:
                    sermon_index = json.load(f)
                
                start_page_url = None
                for sermon in sermon_index:
                    if sermon.get('page') == args.start_page:
                        start_page_url = sermon.get('page_url')
                        break
                
                if start_page_url and start_page_url in pages_to_process:
                    start_index = pages_to_process.index(start_page_url)
                    pages_to_process = pages_to_process[start_index:]
                    print(f"Starting update from page {args.start_page} ({start_page_url}).")
                else:
                    print(f"Warning: Page {args.start_page} URL not found in sermons to update.")
            else:
                print(f"Warning: Sermon index not found at {sermon_index_path}. Cannot start from page {args.start_page}.")

        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, headless_mode) as manager:
            manager.login()
            for page_url in pages_to_process:
                sermons = updates_by_page[page_url]
                print(f"--- Processing page: {page_url} ---")
                for sermon_data in sermons:
                    print(f"Updating sermon: {sermon_data['title']}")
                    print(f"Sermon data: {sermon_data}")
                    success = manager.update_sermon(sermon_data)
                    if not success:
                        print(f"❌ Failed to update sermon: {sermon_data['title']}")

        print("\n🎉 All sermons have been processed.")
        return

if __name__ == "__main__":
    main()
