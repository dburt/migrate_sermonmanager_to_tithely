#!/usr/bin/env -S uv run --script
import pandas as pd
import json
import os
from collections import Counter

# --- File Paths ---
sermons_csv_path = 'sermons.csv'
audio_sizes_csv_path = 'csv_audio_sizes.csv'
json_path = 'sermon_index.json'
report_path = 'discrepancy_report.csv'
TITHELY_BASE_URL = "https://stalfreds.tithelysetup.com"
# ------------------

def normalize_text(text):
    """Basic normalization for matching text fields."""
    if not isinstance(text, str):
        return ""
    return text.lower().strip()

def main():
    print("--- Starting Detailed Comparison by Audio File Size ---")

    # --- Load Data ---
    print("Loading data from CSVs and JSON...")
    if not all(os.path.exists(p) for p in [sermons_csv_path, audio_sizes_csv_path, json_path]):
        print("ERROR: One or more required data files are missing.")
        return

    sermons_df = pd.read_csv(sermons_csv_path)
    audio_sizes_df = pd.read_csv(audio_sizes_csv_path)
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    json_df = pd.DataFrame(json_data)

    # --- Data Cleaning and Preparation ---
    local_df = pd.merge(sermons_df, audio_sizes_df[['post_id', 'audio_file_size']], on='post_id', how='left')

    local_df.dropna(subset=['audio_file_size'], inplace=True)
    json_df.dropna(subset=['audio_file_size'], inplace=True)
    
    local_df['audio_file_size'] = local_df['audio_file_size'].astype(int)
    json_df['audio_file_size'] = json_df['audio_file_size'].astype(int)

    local_df = local_df[local_df['audio_file_size'] > 0]
    json_df = json_df[json_df['audio_file_size'] > 0]

    # --- Perform the Merge/Comparison ---
    merged_df = pd.merge(
        local_df,
        json_df,
        on='audio_file_size',
        how='outer',
        suffixes=['_csv', '_json'],
        indicator=True
    )

    # --- Analyze the Results ---
    csv_only = merged_df[merged_df['_merge'] == 'left_only']
    json_only = merged_df[merged_df['_merge'] == 'right_only']
    in_both = merged_df[merged_df['_merge'] == 'both']

    print("\n--- Comparison Summary ---")
    print(f"Sermons found only in local CSV data: {len(csv_only)}")
    print(f"Sermons found only in Tithely scrape (JSON): {len(json_only)}")
    print(f"Sermons found in both sources (matched by file size): {len(in_both)}")

    # --- Detailed Discrepancy Analysis ---
    discrepancies = []
    discrepancy_counts = Counter()

    for _, row in in_both.iterrows():
        fields_to_check = {
            'title': ('title_csv', 'title_json'),
            'speaker': ('preacher', 'speaker'),
            'series': ('sermon_series_csv', 'sermon_series_json'),
            'passage': ('bible_passage_csv', 'bible_passage_json')
        }
        
        for field, (csv_col, json_col) in fields_to_check.items():
            csv_val = normalize_text(row.get(csv_col, ''))
            json_val = normalize_text(row.get(json_col, ''))
            
            if csv_val != json_val:
                discrepancy_counts[field] += 1
                discrepancies.append({
                    'audio_file_size': row['audio_file_size'],
                    'csv_title': row['title_csv'],
                    'json_title': row['title_json'],
                    'field_with_discrepancy': field,
                    'csv_value': row.get(csv_col, '[NOT FOUND]'),
                    'json_value': row.get(json_col, '[NOT FOUND]'),
                    'sermon_detail_link': f"{TITHELY_BASE_URL}{row.get('detail_page_url', '')}"
                })

    print(f"\n--- Discrepancy Breakdown ({len(discrepancies)} total) ---")
    for field, count in discrepancy_counts.items():
        print(f"- {count} sermons with mismatched '{field}' fields.")

    # --- Generate CSV Report ---
    if discrepancies:
        discrepancy_df = pd.DataFrame(discrepancies)
        discrepancy_df.to_csv(report_path, index=False)
        print(f"\n✅ Successfully generated a detailed discrepancy report at: {report_path}")

    if not csv_only.empty:
        print("\n--- Sermons Only in Local CSV (To Be Created on Tithely) ---")
        for _, row in csv_only.iterrows():
            print(f"- {row['title_csv']} (Size: {row['audio_file_size']})")

if __name__ == "__main__":
    main()