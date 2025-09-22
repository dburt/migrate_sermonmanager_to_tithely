#!/usr/bin/env -S uv run --script

import subprocess
import pandas as pd
import re
import json
import os

def generate_missing_sermons_feed():
    """
    Generates an RSS feed for sermons that are only present in the local CSV.
    """
    print("Running compare_data.py to find missing sermons...")
    try:
        result = subprocess.run([
            'python',
            'compare_data.py'
        ], capture_output=True, text=True, check=True)
        stdout = result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error running compare_data.py: {e}")
        if isinstance(e, subprocess.CalledProcessError):
            print(f"Stderr: {e.stderr}")
        return

    print("Parsing output to find missing sermon titles...")
    try:
        missing_sermons_section = stdout.split("--- Sermons Only in Local CSV (To Be Created on Tithely) ---")[1]
        missing_titles = re.findall(r"- (.*) \(Size: [\d.]+\)", missing_sermons_section)
        missing_titles = [title.strip() for title in missing_titles]
    except IndexError:
        print("No 'Sermons Only in Local CSV' section found in the output. Nothing to do.")
        return

    if not missing_titles:
        print("No missing sermons found. The RSS feed will not be generated.")
        return

    print(f"Found {len(missing_titles)} missing sermons.")

    print("Filtering sermons.csv...")
    sermons_df = pd.read_csv('sermons.csv')
    missing_sermons_df = sermons_df[sermons_df['title'].isin(missing_titles)]

    temp_json_path = 'missing_sermons.json'
    print(f"Converting filtered data to {temp_json_path}...")
    missing_sermons_df.to_json(temp_json_path, orient='records', indent=4)

    output_rss_path = 'tithely_import_feed.xml'
    print(f"Generating RSS feed at {output_rss_path}...")
    try:
        subprocess.run([
            'python',
            'generate_rss_feed.py',
            temp_json_path,
            output_rss_path
        ], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error running generate_rss_feed.py: {e}")
        if isinstance(e, subprocess.CalledProcessError):
            print(f"Stderr: {e.stderr}")
        # Clean up the temp file even if there is an error
        os.remove(temp_json_path)
        return

    print("Cleaning up temporary files...")
    os.remove(temp_json_path)

    print(f"\n✅ Successfully created {output_rss_path} for the {len(missing_titles)} missing sermons.")

if __name__ == "__main__":
    generate_missing_sermons_feed()
