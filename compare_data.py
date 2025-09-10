#!/usr/bin/env -S uv run --script
import pandas as pd
import json
import os

# --- File Paths ---
csv_path = 'sermons.csv'
json_path = 'sermon_index_2025-09-10.json'
# ------------------

def normalize_title(title):
    """Basic normalization for matching titles."""
    if not isinstance(title, str):
        return ""
    return title.lower().strip().replace('...', '').strip()

def main():
    print("--- Starting Comparison ---")
    if not os.path.exists(csv_path):
        print(f"ERROR: CSV file not found at {csv_path}")
        return
    if not os.path.exists(json_path):
        print(f"ERROR: JSON file not found at {json_path}")
        return

    # Load data
    print("Loading data from CSV and JSON...")
    csv_df = pd.read_csv(csv_path)
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    
    json_df = pd.DataFrame(json_data)
    
    print(f"Loaded {len(csv_df)} sermons from CSV.")
    print(f"Loaded {len(json_df)} sermons from JSON scrape.")

    # --- Data Normalization ---
    csv_df['norm_title'] = csv_df['title'].apply(normalize_title)
    json_df['norm_title'] = json_df['title'].apply(normalize_title)

    # --- Perform the Merge/Comparison ---
    merged_df = pd.merge(
        csv_df, 
        json_df, 
        on='norm_title', 
        how='outer', 
        suffixes=['_csv', '_json'],
        indicator=True
    )

    # --- Analyze the Results ---
    csv_only = merged_df[merged_df['_merge'] == 'left_only']
    json_only = merged_df[merged_df['_merge'] == 'right_only']
    in_both = merged_df[merged_df['_merge'] == 'both']

    print("\n--- Comparison Summary ---")
    print(f"Sermons found only in sermons.csv: {len(csv_only)}")
    print(f"Sermons found only in the Tithely scrape (JSON): {len(json_only)}")
    print(f"Sermons found in both sources: {len(in_both)}")

    # --- Find Discrepancies in Common Sermons ---
    discrepancies = []
    for _, row in in_both.iterrows():
        # Compare preacher/speaker
        if str(row['preacher']).lower() != str(row['speaker']).lower():
            discrepancies.append({
                'title': row['title_csv'],
                'field': 'Speaker',
                'csv_value': row['preacher'],
                'json_value': row['speaker']
            })
        # Compare series
        if str(row.get('sermon_series_csv','')).lower() != str(row.get('sermon_series_json','')).lower():
             discrepancies.append({
                'title': row['title_csv'],
                'field': 'Series',
                'csv_value': row.get('sermon_series_csv',''),
                'json_value': row.get('sermon_series_json','')
            })
        # Compare bible_passage
        passage_csv = str(row.get('bible_passage_csv', ''))
        passage_json = str(row.get('bible_passage_json', ''))
        desc_json = str(row.get('description', ''))
        if passage_csv and passage_csv not in passage_json and passage_csv not in desc_json:
            discrepancies.append({
                'title': row['title_csv'],
                'field': 'Bible Passage',
                'csv_value': passage_csv,
                'json_value': passage_json if passage_json else '(not found)'
            })

    print(f"\nFound {len(discrepancies)} potential discrepancies in sermons that are in both sources.")

    if not csv_only.empty:
        print("\n--- Examples of Sermons Only in CSV ---")
        for _, row in csv_only.head().iterrows():
            print(f"- {row['title_csv']} (Date: {row['post_date_gmt']})")

    if not json_only.empty:
        print("\n--- Examples of Sermons Only in Tithely Scrape ---")
        for _, row in json_only.head().iterrows():
            print(f"- {row['title_json']} (Date: {row['date']})")
            
    if discrepancies:
        print("\n--- Examples of Discrepancies ---")
        for d in discrepancies[:5]:
            print(f"- Title: {d['title']}")
            print(f"  Field: {d['field']}")
            print(f"  CSV Value:  '{d['csv_value']}'")
            print(f"  JSON Value: '{d['json_value']}'")


if __name__ == "__main__":
    main()