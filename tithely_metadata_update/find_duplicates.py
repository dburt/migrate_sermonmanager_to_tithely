#!/usr/bin/env -S uv run --script

# find_duplicates.py

import json
import os
import pandas as pd
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
JSON_FILE_PATH = os.path.join(project_root, "sermon_index.json")
OUTPUT_FILE_PATH = os.path.join(project_root, "duplicates_to_delete.json")

def main():
    """Finds duplicate sermons based on audio_file_size."""
    with open(JSON_FILE_PATH, 'r') as f:
        sermons = json.load(f)

    df = pd.DataFrame(sermons)
    df.dropna(subset=['audio_file_size'], inplace=True)
    df['audio_file_size'] = df['audio_file_size'].astype(int)
    df = df[df['audio_file_size'] > 0]

    duplicates = df[df.duplicated(subset=['audio_file_size'], keep=False)]

    if duplicates.empty:
        print("No duplicate sermons found.")
        return

    print(f"Found {len(duplicates)} duplicate sermons.")

    # Sort by file size to group duplicates together
    duplicates = duplicates.sort_values(by=['audio_file_size', 'date'])

    # We want to keep the oldest sermon and delete the rest
    to_delete = duplicates.groupby('audio_file_size').apply(lambda x: x.iloc[1:]).reset_index(drop=True)

    if to_delete.empty:
        print("No duplicates need to be deleted (only one sermon per file size).")
        return

    print(f"Identified {len(to_delete)} sermons to delete.")

    print("\n--- Sermons to Delete ---")
    for _, row in to_delete.iterrows():
        print(f"- Title: {row['title']}, Date: {row['date']}, Size: {row['audio_file_size']}")

    # Sort by page number in descending order
    to_delete = to_delete.sort_values(by=['page'], ascending=False)

    # Save the list of sermons to delete to a file
    to_delete.to_json(OUTPUT_FILE_PATH, orient='records', indent=4)
    print(f"\nSaved list of sermons to delete to {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()