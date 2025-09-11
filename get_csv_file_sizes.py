#!/usr/bin/env -S uv run --script
import pandas as pd
import requests
import os
from tqdm import tqdm

# --- Configuration ---
INPUT_CSV_PATH = 'sermons_cleaned_2025-08-28_23-29-06.csv'
OUTPUT_CSV_PATH = 'csv_audio_sizes.csv'
# ---------------------

def get_file_size(url: str) -> int:
    """Gets the file size in bytes from a URL using a HEAD request."""
    if not isinstance(url, str) or not url.startswith('http'):
        return 0
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        response.raise_for_status()
        file_size = response.headers.get('Content-Length')
        if file_size:
            return int(file_size)
    except requests.exceptions.RequestException as e:
        # print(f"Could not get file size for {url}: {e}")
        pass
    return 0

def main():
    print(f"--- Reading audio URLs from {INPUT_CSV_PATH} ---")
    if not os.path.exists(INPUT_CSV_PATH):
        print(f"ERROR: Input file not found at {INPUT_CSV_PATH}")
        return

    df = pd.read_csv(INPUT_CSV_PATH, usecols=['post_id', 'audio_url'])
    df.dropna(subset=['audio_url'], inplace=True)
    
    print(f"Found {len(df)} sermons with audio URLs.")
    
    tqdm.pandas(desc="Fetching file sizes")
    df['audio_file_size'] = df['audio_url'].progress_apply(get_file_size)

    df_successful = df[df['audio_file_size'] > 0]
    print(f"Successfully fetched sizes for {len(df_successful)} audio files.")

    print(f"--- Saving results to {OUTPUT_CSV_PATH} ---")
    df_successful.to_csv(OUTPUT_CSV_PATH, index=False)
    print("Done.")

if __name__ == "__main__":
    main()
