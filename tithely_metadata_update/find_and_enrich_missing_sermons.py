#!/usr/bin/env -S uv run --script

# find_and_enrich_missing_sermons.py

import json
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.dirname(script_dir)

ENRICHED_PODCAST_INDEX_PATH = os.path.join(project_root, "sermon_index_enriched_20250926-125254.json")
MAIN_LISTING_INDEX_PATH = os.path.join(project_root, "sermon_index_2025-09-26-130148.json")
BASE_URL = "https://stalfreds.tithelysetup.com"

def get_sermon_details_from_html(html_content: str) -> dict:
    """Extracts Bible passage, description, and audio URL from sermon detail HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    details = {
        "bible_passage": "",
        "description": "",
        "audio_url": ""
    }

    # Scrape Bible Passage
    passage_container = soup.find("div", class_="py-3", string=lambda text: text and "Bible Passage" in text)
    if passage_container:
        for sibling in passage_container.find("h2").next_siblings:
            if isinstance(sibling, str) and sibling.strip():
                details["bible_passage"] = sibling.strip()
                break
            elif sibling.name == 'p' and sibling.get_text(strip=True):
                details["bible_passage"] = sibling.get_text(strip=True)
                break

    # Scrape Description
    description_container = soup.find("div", class_="article mt-3")
    if description_container:
        first_p = description_container.find("p")
        if first_p:
            details["description"] = first_p.get_text(strip=True)

    # Scrape Audio URL
    download_link = soup.find("a", class_="btn btn-link", href=lambda href: href and "cloudfront.net" in href)
    if download_link:
        details["audio_url"] = download_link.get("href")

    return details

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
    if not os.path.exists(ENRICHED_PODCAST_INDEX_PATH):
        print(f"❌ ERROR: Enriched podcast index file not found at {ENRICHED_PODCAST_INDEX_PATH}.")
        return
    if not os.path.exists(MAIN_LISTING_INDEX_PATH):
        print(f"❌ ERROR: Main listing index file not found at {MAIN_LISTING_INDEX_INDEX_PATH}.")
        return

    with open(ENRICHED_PODCAST_INDEX_PATH, 'r') as f:
        enriched_podcast_sermons = json.load(f)
    with open(MAIN_LISTING_INDEX_PATH, 'r') as f:
        main_listing_sermons = json.load(f)

    # Create a set of slugs from the enriched podcast sermons for quick lookup
    podcast_slugs = {sermon['slug'] for sermon in enriched_podcast_sermons}

    missing_sermons_to_enrich = []
    for sermon in main_listing_sermons:
        if sermon['slug'] not in podcast_slugs:
            missing_sermons_to_enrich.append(sermon)

    if not missing_sermons_to_enrich:
        print("No new sermons found in the main listing that are not in the podcast listing.")
        return

    print(f"Found {len(missing_sermons_to_enrich)} new sermons to enrich...")
    enriched_missing_sermons = []

    for sermon in tqdm(missing_sermons_to_enrich, desc="Enriching Missing Sermons"):
        full_detail_url = f"{BASE_URL}{sermon['detail_page_url']}"
        try:
            response = requests.get(full_detail_url, timeout=30)
            response.raise_for_status()
            details = get_sermon_details_from_html(response.text)
            sermon.update(details)
            
            if sermon.get('audio_url'):
                sermon['audio_file_size'] = get_file_size(sermon['audio_url'])

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching or processing {full_detail_url}: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred for {full_detail_url}: {e}")
        
        enriched_missing_sermons.append(sermon)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = os.path.join(project_root, f"sermon_index_missing_enriched_{timestamp}.json")
    
    with open(output_filename, "w") as f:
        json.dump(enriched_missing_sermons, f, indent=4)
    print(f"Enriched missing sermons saved to {output_filename}")

if __name__ == "__main__":
    main()
