#!/usr/bin/env -S uv run --script

# merge_enriched_indexes.py

import json
import os
from datetime import datetime

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.dirname(script_dir)

ENRICHED_PODCAST_INDEX_PATH = os.path.join(project_root, "sermon_index_enriched_20250926-125254.json")
ENRICHED_MISSING_INDEX_PATH = os.path.join(project_root, "sermon_index_missing_enriched_20250926-150106.json")

def main():
    if not os.path.exists(ENRICHED_PODCAST_INDEX_PATH):
        print(f"❌ ERROR: Enriched podcast index file not found at {ENRICHED_PODCAST_INDEX_PATH}.")
        return
    if not os.path.exists(ENRICHED_MISSING_INDEX_PATH):
        print(f"❌ ERROR: Enriched missing index file not found at {ENRICHED_MISSING_INDEX_PATH}.")
        return

    with open(ENRICHED_PODCAST_INDEX_PATH, 'r') as f:
        podcast_sermons = json.load(f)
    with open(ENRICHED_MISSING_INDEX_PATH, 'r') as f:
        missing_sermons = json.load(f)

    # Merge the two lists. Since missing_sermons were explicitly identified as not in podcast_sermons,
    # there should be no duplicates by slug. However, to be safe, we can use a dictionary for merging.
    combined_sermons_map = {sermon['slug']: sermon for sermon in podcast_sermons}
    for sermon in missing_sermons:
        combined_sermons_map[sermon['slug']] = sermon

    combined_sermons = list(combined_sermons_map.values())

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = os.path.join(project_root, f"sermon_index_combined_enriched_{timestamp}.json")
    
    with open(output_filename, "w") as f:
        json.dump(combined_sermons, f, indent=4)
    print(f"Combined enriched sermon index saved to {output_filename}")
    print(f"Total sermons in combined index: {len(combined_sermons)}")

if __name__ == "__main__":
    main()
