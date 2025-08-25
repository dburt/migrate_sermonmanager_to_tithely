#!/usr/bin/env -S uv run --script

# analyze_updates.py

import json
import requests
from collections import defaultdict
from playwright.sync_api import sync_playwright, Page

JSON_FILE_PATH = "../sermons.json"
SERMON_INDEX_PATH = "sermon_index.json"
BASE_URL = "https://stalfreds.tithelysetup.com"

def get_audio_download_url(page: Page, sermon_url: str) -> str:
    """Gets the audio download URL from a sermon detail page."""
    print(f"Getting audio download URL from: {sermon_url}")
    page.goto(f"{BASE_URL}{sermon_url}")
    download_link = page.locator("a.btn.btn-link[href*='cloudfront.net']")
    if download_link.count() > 0:
        return download_link.first.get_attribute("href")
    return ""

def get_file_size(url: str) -> int:
    """Gets the file size in bytes from a URL using a HEAD request."""
    try:
        response = requests.head(url, timeout=10)
        response.raise_for_status()
        file_size = response.headers.get('Content-Length')
        if file_size:
            return int(file_size)
    except requests.exceptions.RequestException as e:
        print(f"Error getting file size for {url}: {e}")
    return 0

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

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for title, local_sermon_list in local_sermons_by_title.items():
            if title in online_sermons_by_title:
                online_sermon_list = online_sermons_by_title[title]
                online_only.discard(title)

                if len(local_sermon_list) > 1 or len(online_sermon_list) > 1:
                    for local_sermon in local_sermon_list:
                        found_match = False
                        for online_sermon in online_sermon_list:
                            online_audio_url = get_audio_download_url(page, online_sermon['edit_url'])
                            online_file_size = get_file_size(online_audio_url)
                            
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