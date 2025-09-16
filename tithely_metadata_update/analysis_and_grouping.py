
import pandas as pd
import json
from collections import defaultdict

def find_sermons_to_update(sermons_csv_path, csv_audio_sizes_path, sermon_index_path):
    """
    Compares local sermon data with Tithely data and identifies sermons to be updated.
    """
    print("--- Loading Data for Comparison ---")
    sermons_df = pd.read_csv(sermons_csv_path)
    sizes_df = pd.read_csv(csv_audio_sizes_path)
    with open(sermon_index_path, 'r') as f:
        sermon_index = json.load(f)
    index_df = pd.DataFrame(sermon_index)

    print("--- Preparing Data ---")
    # Merge local data
    local_df = pd.merge(sermons_df, sizes_df, on='post_id')

    # Clean and prepare for merge
    local_df.dropna(subset=['audio_file_size'], inplace=True)
    index_df.dropna(subset=['audio_file_size'], inplace=True)
    local_df['audio_file_size'] = local_df['audio_file_size'].astype(int)
    index_df['audio_file_size'] = index_df['audio_file_size'].astype(int)
    local_df = local_df[local_df['audio_file_size'] > 0]
    index_df = index_df[index_df['audio_file_size'] > 0]

    print("--- Matching Sermons by File Size ---")
    merged_df = pd.merge(
        local_df,
        index_df,
        on='audio_file_size',
        how='inner', # We only care about sermons that are in both
        suffixes=('_local', '_online')
    )

    print("--- Identifying Discrepancies ---")
    sermons_to_update = []
    for _, row in merged_df.iterrows():
        discrepancies = []
        # Compare preacher/speaker
        if str(row['preacher']).lower() != str(row['speaker']).lower():
            discrepancies.append('speaker')
        # Compare series
        if str(row.get('sermon_series_local', '')).lower() != str(row.get('sermon_series_online', '')).lower():
            discrepancies.append('series')
        # Compare bible_passage
        if str(row.get('bible_passage', '')).lower() != str(row.get('bible_passage_online', '')).lower():
            discrepancies.append('passage')

        if discrepancies:
            sermon_data = row.to_dict()
            sermon_data['discrepancies'] = discrepancies
            sermons_to_update.append(sermon_data)

    print(f"Found {len(sermons_to_update)} sermons with discrepancies to update.")

    # Identify sermons that are only in the local CSV
    outer_merged_df = pd.merge(local_df, index_df, on='audio_file_size', how='outer', indicator=True)
    local_only_df = outer_merged_df[outer_merged_df['_merge'] == 'left_only']
    if not local_only_df.empty:
        print(f"--- Found {len(local_only_df)} sermons that exist locally but not on Tithely. ---")
        print("These sermons need to be created manually on Tithely.")
        for _, row in local_only_df.head().iterrows():
            print(f"  - {row['title']}")

    print("--- Grouping Sermons by Page URL for Updater ---")
    updates_by_page = defaultdict(list)
    for sermon in sermons_to_update:
        page_url = sermon.get('page_url')
        if page_url:
            updates_by_page[page_url].append(sermon)

    return updates_by_page
