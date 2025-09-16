#!/usr/bin/env -S uv run --script

# find_duplicates.py

import json
import pandas as pd
from collections import defaultdict

JSON_FILE_PATH = "sermon_index.json"
OUTPUT_FILE_PATH = "duplicates_to_delete.json"

def main():
    """Finds duplicate sermons based on file_size_bytes."""
    with open(JSON_FILE_PATH, 'r') as f:
        sermons = json.load(f)

    df = pd.DataFrame(sermons)
    df.dropna(subset=['file_size_bytes'], inplace=True)
    df['file_size_bytes'] = df['file_size_bytes'].astype(int)
    df = df[df['file_size_bytes'] > 0]

    duplicates = df[df.duplicated(subset=['file_size_bytes'], keep=False)]

    if duplicates.empty:
        print("No duplicate sermons found.")
        return

    print(f"Found {len(duplicates)} duplicate sermons.")

    # Sort by file size to group duplicates together
    duplicates = duplicates.sort_values(by=['file_size_bytes', 'date'])

    # We want to keep the oldest sermon and delete the rest
    to_delete = duplicates.groupby('file_size_bytes').apply(lambda x: x.iloc[1:]).reset_index(drop=True)

    if to_delete.empty:
        print("No duplicates need to be deleted (only one sermon per file size).")
        return

    print(f"Identified {len(to_delete)} sermons to delete.")

    print("\n--- Sermons to Delete ---")
    for _, row in to_delete.iterrows():
        print(f"- Title: {row['title']}, Date: {row['date']}, Size: {row['file_size_bytes']}")

    # Save the list of sermons to delete to a file
    to_delete.to_json(OUTPUT_FILE_PATH, orient='records', indent=4)
    print(f"\nSaved list of sermons to delete to {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()