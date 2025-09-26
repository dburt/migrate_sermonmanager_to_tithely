#!/usr/bin/env -S uv run --script

# enrich_local_sermons_with_audio_size.py

import json
import os
import requests
from tqdm import tqdm

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.dirname(script_dir)

LOCAL_SERMONS_INPUT_PATH = os.path.join(project_root, "sermons.json")
LOCAL_SERMONS_OUTPUT_PATH = os.path.join(project_root, "sermons_with_audio_size.json")

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
    except requests.exceptions.RequestException:
        pass
    return 0

def main():
    if not os.path.exists(LOCAL_SERMONS_INPUT_PATH):
        print(f"❌ ERROR: Local sermons input file not found at {LOCAL_SERMONS_INPUT_PATH}.")
        return

    with open(LOCAL_SERMONS_INPUT_PATH, 'r') as f:
        local_sermons = json.load(f)

    print(f"Enriching {len(local_sermons)} local sermons with audio file sizes...")
    
    for sermon in tqdm(local_sermons, desc="Fetching Audio File Sizes"):
        if 'audio_url' in sermon and 'audio_file_size' not in sermon:
            sermon['audio_file_size'] = get_file_size(sermon['audio_url'])
        elif 'audio_url' not in sermon:
            sermon['audio_file_size'] = 0 # Assign 0 if no audio_url

    with open(LOCAL_SERMONS_OUTPUT_PATH, "w") as f:
        json.dump(local_sermons, f, indent=4)
    print(f"Enriched local sermons saved to {LOCAL_SERMONS_OUTPUT_PATH}")

if __name__ == "__main__":
    main()
