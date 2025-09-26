import json
import os
import re
import pandas as pd
from collections import defaultdict
from datetime import datetime

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.dirname(script_dir)

COMBINED_ENRICHED_INDEX_PATH = os.path.join(project_root, "sermon_index_combined_enriched_20250926-152734.json")
LOCAL_SERMONS_PATH = os.path.join(project_root, "sermons.json") # Canonical local data
CSV_AUDIO_SIZES_PATH = os.path.join(project_root, "csv_audio_sizes.csv")

# Regex to find post IDs in subtitles, e.g., [post_id=1234]
POST_ID_REGEX = r"[post_id=\d+]"

def main():
    if not os.path.exists(COMBINED_ENRICHED_INDEX_PATH):
        print(f"❌ ERROR: Combined enriched index file not found at {COMBINED_ENRICHED_INDEX_PATH}.")
        return
    if not os.path.exists(LOCAL_SERMONS_PATH):
        print(f"❌ ERROR: Local sermons file not found at {LOCAL_SERMONS_PATH}.")
        return
    if not os.path.exists(CSV_AUDIO_SIZES_PATH):
        print(f"❌ ERROR: CSV audio sizes file not found at {CSV_AUDIO_SIZES_PATH}. Please run get_csv_file_sizes.py first.")
        return

    with open(COMBINED_ENRICHED_INDEX_PATH, 'r') as f:
        online_sermons = json.load(f)
    with open(LOCAL_SERMONS_PATH, 'r') as f:
        local_sermons_json = json.load(f)
    csv_audio_sizes_df = pd.read_csv(CSV_AUDIO_SIZES_PATH)

    # Convert local_sermons_json to DataFrame for easier merging
    local_sermons_df = pd.DataFrame(local_sermons_json)
    
    # Ensure post_id is of the same type for merging
    local_sermons_df['post_id'] = local_sermons_df['post_id'].astype(str)
    csv_audio_sizes_df['post_id'] = csv_audio_sizes_df['post_id'].astype(str)

    # Merge local sermons with their audio file sizes
    local_sermons_with_sizes_df = pd.merge(
        local_sermons_df,
        csv_audio_sizes_df[['post_id', 'audio_file_size']],
        on='post_id',
        how='left'
    )
    local_sermons_with_sizes_df.dropna(subset=['audio_file_size'], inplace=True)
    local_sermons_with_sizes_df['audio_file_size'] = local_sermons_with_sizes_df['audio_file_size'].astype(int)
    local_sermons_with_sizes = local_sermons_with_sizes_df.to_dict('records')

    # Index online sermons by audio_file_size for efficient lookup
    online_sermons_map = {sermon['audio_file_size']: sermon for sermon in online_sermons if 'audio_file_size' in sermon}

    update_report = {
        "sermons_to_update": [],
        "sermons_only_local": [],
        "sermons_only_online": [],
        "subtitle_post_id_issues": []
    }

    # Track audio_file_sizes from local_sermons to identify online_only sermons later
    local_audio_file_sizes = set()

    for local_sermon in local_sermons_with_sizes:
        local_audio_file_size = local_sermon.get('audio_file_size')
        if not local_audio_file_size:
            print(f"Warning: Local sermon missing audio_file_size for identification: {local_sermon.get('title')}")
            continue
        local_audio_file_sizes.add(local_audio_file_size)

        if local_audio_file_size in online_sermons_map:
            online_sermon = online_sermons_map[local_audio_file_size]
            discrepancies = []
            
            # Check for subtitle post ID issue in online sermon_series and description
            online_sermon_series = online_sermon.get('sermon_series', '')
            online_description = online_sermon.get('description', '')

            if re.search(POST_ID_REGEX, online_sermon_series):
                update_report["subtitle_post_id_issues"].append({
                    "type": "sermon_series",
                    "slug": online_sermon.get('slug'),
                    "title": online_sermon.get('title'),
                    "current_value": online_sermon_series,
                    "proposed_value": re.sub(POST_ID_REGEX, '', online_sermon_series).strip()
                })
            
            if re.search(POST_ID_REGEX, online_description):
                update_report["subtitle_post_id_issues"].append({
                    "type": "description",
                    "slug": online_sermon.get('slug'),
                    "title": online_sermon.get('title'),
                    "current_value": online_description,
                    "proposed_value": re.sub(POST_ID_REGEX, '', online_description).strip()
                })

            # Compare fields
            if local_sermon.get('preacher') != online_sermon.get('speaker'):
                discrepancies.append({
                    "field": "speaker",
                    "online_slug": online_sermon.get('slug'),
                    "title": online_sermon.get('title'),
                    "local_value": local_sermon.get('preacher'),
                    "online_value": online_sermon.get('speaker')
                })
            
            # Normalize sermon_series for comparison (remove post_id from online version if present)
            normalized_online_series = re.sub(POST_ID_REGEX, '', online_sermon_series).strip()
            if local_sermon.get('sermon_series') != normalized_online_series:
                discrepancies.append({
                    "field": "sermon_series",
                    "online_slug": online_sermon.get('slug'),
                    "title": online_sermon.get('title'),
                    "local_value": local_sermon.get('sermon_series'),
                    "online_value": normalized_online_series # Compare against normalized online value
                })

            if local_sermon.get('bible_passage') != online_sermon.get('bible_passage'):
                discrepancies.append({
                    "field": "bible_passage",
                    "online_slug": online_sermon.get('slug'),
                    "title": online_sermon.get('title'),
                    "local_value": local_sermon.get('bible_passage'),
                    "online_value": online_sermon.get('bible_passage')
                })
            
            # Add other fields for comparison as needed

            if discrepancies:
                update_report["sermons_to_update"].append({
                    "online_slug": online_sermon.get('slug'),
                    "title": online_sermon.get('title'),
                    "discrepancies": discrepancies
                })
        else:
            update_report["sermons_only_local"].append({
                "title": local_sermon.get('title'),
                "post_id": local_sermon.get('post_id'),
                "audio_file_size": local_audio_file_size
            })

    # Identify sermons only present online
    for online_sermon in online_sermons:
        online_audio_file_size = online_sermon.get('audio_file_size')
        if online_audio_file_size not in local_audio_file_sizes:
            update_report["sermons_only_online"].append({
                "slug": online_sermon.get('slug'),
                "title": online_sermon.get('title'),
                "audio_file_size": online_audio_file_size
            })

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = os.path.join(project_root, f"tithely_update_report_{timestamp}.json")
    
    with open(output_filename, "w") as f:
        json.dump(update_report, f, indent=4)
    print(f"Tithely update report generated: {output_filename}")

    # Print a summary
    print("\n--- Update Report Summary ---")
    print(f"Sermons with discrepancies: {len(update_report["sermons_to_update"])}")
    print(f"Sermons only in local data: {len(update_report["sermons_only_local"])}")
    print(f"Sermons only in online data: {len(update_report["sermons_only_online"])}")
    print(f"Subtitles/Descriptions with post ID issues: {len(update_report["subtitle_post_id_issues"])}")
