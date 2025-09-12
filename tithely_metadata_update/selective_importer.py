#!/usr/bin/env -S uv run --script

# selective_importer.py

import json
import os
import sys
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
    parser.add_argument("--csv-sermons", default="sermons_cleaned_v2.csv", help="Path to the cleaned local sermons CSV file.")
    parser.add_argument("--create-index", action="store_true", help="Create a new sermon index from Tithe.ly.")
    parser.add_argument("--enrich", action="store_true", help="Enrich with details and audio URL from sermon pages.")
    parser.add_argument("--with-file-sizes", action="store_true", help="Fetch audio file sizes (requires --enrich).")
    parser.add_argument("--update", action="store_true", help="Update sermons in Tithe.ly with data from the local CSV.")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of sermons to process.")
    parser.add_argument("--headless", action="store_true", help="Run the browser in headless mode.")
    parser.add_argument("--debug", action="store_true", help="Open a browser in debug mode on a specific sermon.")
    parser.add_argument("--start-page", type=int, default=1, help="Page number to start sermon indexing from.")
    return parser.parse_args()

def main():
    """Main function to orchestrate the selective import."""
    args = parse_arguments()

    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    headless_mode = args.headless if not args.debug else False

    if args.create_index:
        print("Creating a new sermon index from Tithe.ly list pages...")
        with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, headless_mode) as manager:
            manager.login()
            sermon_index = manager.create_sermon_index(
                enrich_details=args.enrich,
                detail_scrape_limit=args.limit,
                with_file_sizes=args.with_file_sizes,
                start_page=args.start_page
            )
            
            datestamp = datetime.now().strftime("%Y-%m-%d")
            output_filename = f"sermon_index_{datestamp}.json"
            
            with open(output_filename, "w") as f:
                json.dump(sermon_index, f, indent=4)
            print(f"Sermon index with {len(sermon_index)} entries created at {output_filename}")
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