#!/usr/bin/env -S uv run --script

# run_add_file_sizes.py

import json
import os
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
JSON_FILE_PATH = "../sermons.json"
# ---------------------

def main():
    """Adds the file size in bytes to each sermon in sermons.json."""
    with open(JSON_FILE_PATH, 'r') as f:
        sermons = json.load(f)

    with TithelyManager(os.environ.get("TITHELY_EMAIL"), os.environ.get("TITHELY_PASSWORD"), "/usr/bin/brave-browser", True) as manager:
        for sermon in sermons:
            audio_url = sermon.get("audio_url")
            if audio_url:
                file_size = manager.get_file_size(audio_url)
                if file_size:
                    sermon['file_size_bytes'] = file_size
                    print(f"Got file size for {sermon['title']}: {file_size} bytes")
                else:
                    print(f"Could not get file size for {sermon['title']}")

    with open(JSON_FILE_PATH, "w") as f:
        json.dump(sermons, f, indent=4)

if __name__ == "__main__":
    main()