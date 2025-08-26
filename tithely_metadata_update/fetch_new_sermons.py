#!/usr/bin/env -S uv run --script

# fetch_new_sermons.py

import json
import os
import boto3
import requests
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
JSON_FILE_PATH = "sermons.json"
SERMON_INDEX_PATH = "sermon_index.json"
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
HEADLESS_MODE = False
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
# ---------------------

def main():
    """Identifies new sermons on Tithely, fetches their metadata, and uploads their audio to S3."""
    if not all([TITHELY_EMAIL, TITHELY_PASSWORD, S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY]):
        print("❌ ERROR: Please provide all necessary environment variables.")
        return

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
        manager.login()

        print("Creating sermon index...")
        online_sermons = manager.create_sermon_index()
        with open(SERMON_INDEX_PATH, "w") as index_file:
            json.dump(online_sermons, index_file, indent=4)
        print(f"Found {len(online_sermons)} sermons in the index.")

        with open(JSON_FILE_PATH, 'r') as f:
            local_sermons = json.load(f)
        
        local_slugs = {s['slug'] for s in local_sermons}
        new_sermons = [s for s in online_sermons if s['slug'] not in local_slugs]

        if not new_sermons:
            print("No new sermons found.")
            return

        print(f"Found {len(new_sermons)} new sermons.")

        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

        new_sermons_data = []
        for sermon in new_sermons:
            audio_url = manager.get_audio_download_url(sermon['edit_url'])
            if not audio_url:
                print(f"Could not get audio URL for {sermon['title']}. Skipping.")
                continue

            file_name = os.path.basename(audio_url)
            print(f"Downloading {file_name}...")
            response = requests.get(audio_url, stream=True)
            response.raise_for_status()

            print(f"Uploading {file_name} to S3...")
            s3.upload_fileobj(response.raw, S3_BUCKET_NAME, file_name)

            sermon['audio_url'] = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
            new_sermons_data.append(sermon)

        with open("new_sermons.json", "w") as f:
            json.dump(new_sermons_data, f, indent=4)
        
        print("\n🎉 Finished fetching new sermons.")

if __name__ == "__main__":
    main()
