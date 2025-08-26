#!/usr/bin/env -S uv run --script

# run_analyzer.py

import json
from collections import defaultdict
from tithely_manager import TithelyManager
import os

# --- CONFIGURATION ---
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
JSON_FILE_PATH = "sermons.json"
SERMON_INDEX_PATH = "sermon_index.json"
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
HEADLESS_MODE = False
# ---------------------

def main():
    """Analyzes the sermon data to identify discrepancies."""
    with open(JSON_FILE_PATH, 'r') as f:
        local_sermons = json.load(f)

    with open(SERMON_INDEX_PATH, 'r') as f:
        online_sermons = json.load(f)

    local_sermons_by_title = defaultdict(list)
    for s in local_sermons:
        local_sermons_by_title[s['title']].append(s)

    online_sermons_by_title = defaultdict(list)
    for s in online_sermons:
        online_sermons_by_title[s['title']].append(s)

    discrepancies = []
    local_only = []
    online_only = set(s['title'] for s in online_sermons)

    with TithelyManager(TITHELY_EMAIL, TITHELY_PASSWORD, BRAVE_EXECUTABLE_PATH, HEADLESS_MODE) as manager:
        manager.login()

        for title, local_sermon_list in local_sermons_by_title.items():
            if title in online_sermons_by_title:
                online_sermon_list = online_sermons_by_title[title]
                online_only.discard(title)

                if len(local_sermon_list) > 1 or len(online_sermon_list) > 1:
                    for local_sermon in local_sermon_list:
                        found_match = False
                        for online_sermon in online_sermon_list:
                            online_audio_url = manager.get_audio_download_url(online_sermon['edit_url'])
                            online_file_size = manager.get_file_size(online_audio_url)
                            
                            if local_sermon.get('file_size_bytes') == online_file_size:
                                # Found a match, now compare fields
                                sermon_discrepancies = []
                                if local_sermon.get("preacher") != online_sermon.get("speaker"):
                                    sermon_discrepancies.append(f"  - Speaker: Local('{local_sermon.get('preacher')}') != Online('{online_sermon.get('speaker')}')")
                                if local_sermon.get("sermon_series") != online_sermon.get("sermon_series"):
                                    sermon_discrepancies.append(f"  - Series: Local('{local_sermon.get('sermon_series')}') != Online('{online_sermon.get('sermon_series')}')")
                                if local_sermon.get("bible_passage") != online_sermon.get("bible_passage"):
                                    sermon_discrepancies.append(f"  - Passage: Local('{local_sermon.get('bible_passage')}') != Online('{online_sermon.get('bible_passage')}')")

                                if sermon_discrepancies:
                                    discrepancies.append(f"Sermon: {local_sermon['title']}\n" + "\n".join(sermon_discrepancies))
                                found_match = True
                                online_only.discard(online_sermon['title'])
                                break
                        if not found_match:
                            local_only.append(local_sermon['title'])
                else:
                    # Only one sermon with this title, so we can compare directly
                    local_sermon = local_sermon_list[0]
                    online_sermon = online_sermon_list[0]
                    sermon_discrepancies = []
                    if local_sermon.get("preacher") != online_sermon.get("speaker"):
                        sermon_discrepancies.append(f"  - Speaker: Local('{local_sermon.get('preacher')}') != Online('{online_sermon.get('speaker')}')")
                    if local_sermon.get("sermon_series") != online_sermon.get("sermon_series"):
                        sermon_discrepancies.append(f"  - Series: Local('{local_sermon.get('sermon_series')}') != Online('{online_sermon.get('sermon_series')}')")
                    if local_sermon.get("bible_passage") != online_sermon.get("bible_passage"):
                        sermon_discrepancies.append(f"  - Passage: Local('{local_sermon.get('bible_passage')}') != Online('{online_sermon.get('bible_passage')}')")

                    if sermon_discrepancies:
                        discrepancies.append(f"Sermon: {local_sermon['title']}\n" + "\n".join(sermon_discrepancies))
                    online_only.discard(online_sermon['title'])
            else:
                local_only.append(title)

    print("--- Sermon Data Gap Analysis ---")

    if discrepancies:
        print(f"\n--- {len(discrepancies)} Sermons with Discrepancies ---")
        for d in discrepancies:
            print(d)
    else:
        print("\n--- No Discrepancies Found ---")

    if local_only:
        print(f"\n--- {len(local_only)} Sermons in local sermons.json but not in online index ---")
        for title in local_only:
            print(f"  - {title}")
    else:
        print("\n--- No Sermons Found Only in local sermons.json ---")

    if online_only:
        print(f"\n--- {len(online_only)} Sermons in online index but not in local sermons.json ---")
        for title in online_only:
            print(f"  - {title}")
    else:
        print("\n--- No Sermons Found Only in Online Index ---")

if __name__ == "__main__":
    main()
