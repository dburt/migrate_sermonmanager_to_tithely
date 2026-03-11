#!/usr/bin/env -S uv run --script
import pandas as pd
import json
import os

# --- File Paths ---
sermons_csv_path = 'sermons_cleaned_2025-08-28_23-29-06.csv'
csv_sizes_path = 'csv_audio_sizes.csv'
json_index_path = 'sermon_index_2025-09-11.json'
# ------------------

def normalize_title(title):
    """Basic normalization for matching titles."""
    if not isinstance(title, str):
        return ""
    return title.lower().strip().replace('...', '').strip()

def get_title_key(title):
    """Creates a key from the first 12 chars of a normalized title."""
    return normalize_title(title)[:12]

def main():
    print("--- Starting Strict Comparison ---")
    # --- Load Data ---
    print("Loading data sources...")
    csv_main_df = pd.read_csv(sermons_csv_path)
    csv_sizes_df = pd.read_csv(csv_sizes_path)
    with open(json_index_path, 'r') as f:
        json_data = json.load(f)
    remote_df = pd.DataFrame(json_data)

    # --- Prepare Local (CSV) Data ---
    # Coerce post_id to numeric, dropping rows with invalid IDs
    csv_main_df['post_id'] = pd.to_numeric(csv_main_df['post_id'], errors='coerce')
    csv_main_df.dropna(subset=['post_id'], inplace=True)
    csv_sizes_df['post_id'] = pd.to_numeric(csv_sizes_df['post_id'], errors='coerce')
    csv_sizes_df.dropna(subset=['post_id'], inplace=True)

    # Now safely convert to int
    csv_main_df['post_id'] = csv_main_df['post_id'].astype(int)
    csv_sizes_df['post_id'] = csv_sizes_df['post_id'].astype(int)

    local_df = pd.merge(csv_main_df, csv_sizes_df, on='post_id')
    local_df = local_df[local_df['audio_file_size'] > 0].copy()
    local_df['audio_file_size'] = local_df['audio_file_size'].astype(int)
    local_df['date_csv'] = pd.to_datetime(local_df['melbourne_time']).dt.date
    local_df['title_key'] = local_df['title'].apply(get_title_key)

    # --- Prepare Remote (JSON) Data ---
    remote_df = remote_df[remote_df['audio_file_size'].notna() & (remote_df['audio_file_size'] > 0)].copy()
    remote_df['audio_file_size'] = remote_df['audio_file_size'].astype(int)
    remote_df['date_json'] = pd.to_datetime(remote_df['date'])
    # Handle potential errors in date conversion
    remote_df['date_json'] = remote_df['date_json'].dt.date
    remote_df['title_key'] = remote_df['title'].apply(get_title_key)

    # --- Primary Merge on File Size ---
    merged_df = pd.merge(
        local_df, 
        remote_df, 
        on='audio_file_size', 
        how='outer', 
        suffixes=['_csv', '_json'], 
        indicator=True
    )

    # --- Secondary Validation ---
    confirmed_indices = []
    mismatched_indices = []
    size_matches = merged_df[merged_df['_merge'] == 'both']

    for index, row in size_matches.iterrows():
        date_matches = row['date_csv'] == row['date_json']
        title_key_matches = row['title_key_csv'] == row['title_key_json']
        
        if date_matches or title_key_matches:
            confirmed_indices.append(index)
        else:
            mismatched_indices.append(index)

    confirmed_df = merged_df.loc[confirmed_indices]
    mismatched_df = merged_df.loc[mismatched_indices]
    csv_only_df = merged_df[merged_df['_merge'] == 'left_only']
    json_only_df = merged_df[merged_df['_merge'] == 'right_only']

    # --- Reporting ---
    print("\n--- Strict Comparison Summary ---")
    print(f"Confirmed Matches (Size + Date/Title): {len(confirmed_df)}")
    print(f"Potential Mismatches (Size matched, but Date/Title did not): {len(mismatched_df)}")
    print(f"Sermons found only in local CSV: {len(csv_only_df)}")
    print(f"Sermons found only in Tithely scrape: {len(json_only_df)}")

    if not mismatched_df.empty:
        print("\n--- Examples of Potential Mismatches ---")
        for _, row in mismatched_df.head().iterrows():
            print(f"- Size: {row['audio_file_size']}")
            print(f"  CSV:  '{row['title_csv']}' (Date: {row['date_csv']}, Key: '{row['title_key_csv']}')")
            print(f"  JSON: '{row['title_json']}' (Date: {row['date_json']}, Key: '{row['title_key_json']}')")

    if not csv_only_df.empty:
        print("\n--- Examples of Sermons Only in CSV ---")
        for _, row in csv_only_df.head().iterrows():
            print(f"- {row['title_csv']} (Size: {row['audio_file_size']})")

if __name__ == "__main__":
    main()
