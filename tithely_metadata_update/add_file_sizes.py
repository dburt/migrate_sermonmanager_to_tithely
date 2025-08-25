#!/usr/bin/env -S uv run --script

# add_file_sizes.py

import json
import requests

def main():
    """Adds the file size in bytes to each sermon in sermons.json."""
    with open("../sermons.json", 'r') as f:
        sermons = json.load(f)

    for sermon in sermons:
        audio_url = sermon.get("audio_url")
        if audio_url:
            try:
                response = requests.head(audio_url, timeout=10)
                response.raise_for_status()
                file_size = response.headers.get('Content-Length')
                if file_size:
                    sermon['file_size_bytes'] = int(file_size)
                    print(f"Got file size for {sermon['title']}: {file_size} bytes")
                else:
                    print(f"Could not get file size for {sermon['title']}")
            except requests.exceptions.RequestException as e:
                print(f"Error getting file size for {sermon['title']}: {e}")

    with open("../sermons.json", "w") as f:
        json.dump(sermons, f, indent=4)

if __name__ == "__main__":
    main()
