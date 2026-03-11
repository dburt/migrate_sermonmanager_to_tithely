#!/usr/bin/env -S uv run --script
import pandas as pd
import json
import os

# --- File Paths ---
csv_sizes_path = 'csv_audio_sizes.csv'
json_index_path = 'sermon_index_2025-09-11.json'
# ------------------

def main():
    print("--- Analyzing Audio File Size Data ---")
    if not os.path.exists(csv_sizes_path):
        print(f"ERROR: CSV sizes file not found at {csv_sizes_path}")
        return
    if not os.path.exists(json_index_path):
        print(f"ERROR: JSON index file not found at {json_index_path}")
        return

    # Load data
    csv_df = pd.read_csv(csv_sizes_path)
    with open(json_index_path, 'r') as f:
        json_data = json.load(f)
    json_df = pd.DataFrame(json_data)

    # --- 1. Analyze Uniqueness in CSV data ---
    print("\n--- Analysis of CSV File Sizes ---")
    # Drop rows where file size is 0 (couldn't be fetched)
    csv_df_valid = csv_df[csv_df['audio_file_size'] > 0].copy()
    
    duplicates = csv_df_valid[csv_df_valid.duplicated(subset=['audio_file_size'], keep=False)]
    
    if duplicates.empty:
        print("✅ All audio file sizes in the CSV are unique.")
    else:
        print(f"⚠️ Found {len(duplicates)} sermons in the CSV that share a file size with at least one other sermon.")
        print("This means file size alone is not a perfect unique key for the CSV data.")
        print("Examples of non-unique sizes:")
        print(duplicates.sort_values(by='audio_file_size').head(10))

    # --- 2. Analyze Matches in Tithely data ---
    print("\n--- Analysis of CSV vs. Tithely Scrape ---")
    
    # Create a set of valid file sizes from the JSON for efficient lookup
    json_sizes = set(json_df[json_df['audio_file_size'].notna() & (json_df['audio_file_size'] > 0)]['audio_file_size'].astype(int))
    
    if not json_sizes:
        print("❌ No valid audio file sizes were found in the Tithely scrape data.")
        return

    # Check how many CSV entries have a match in the JSON data
    csv_df_valid['has_match'] = csv_df_valid['audio_file_size'].isin(json_sizes)
    
    matches = csv_df_valid['has_match'].sum()
    total_valid_csv = len(csv_df_valid)
    
    print(f"Found {matches} matches out of {total_valid_csv} valid sermons in the CSV.")
    print(f"This means {total_valid_csv - matches} sermons from the CSV do not have a file size match in the Tithely data.")

    if total_valid_csv - matches > 0:
        print("\nExamples of CSV sermons with no match in Tithely data:")
        print(csv_df_valid[~csv_df_valid['has_match']].head())


if __name__ == "__main__":
    main()
