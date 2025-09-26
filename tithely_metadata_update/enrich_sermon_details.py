#!/usr/bin/env -S uv run --script

# enrich_sermon_details.py

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

SERMON_INDEX_PATH = os.path.join(project_root, "sermon_index.json")
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
        # Find the actual text node after the H2 tag
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
    if not os.path.exists(SERMON_INDEX_PATH):
        print(f"❌ ERROR: Sermon index file not found at {SERMON_INDEX_PATH}. Please create it first.")
        return

    with open(SERMON_INDEX_PATH, 'r') as f:
        sermon_index = json.load(f)

    print(f"Enriching details for {len(sermon_index)} sermons...")
    enriched_sermons = []
    
    for sermon in tqdm(sermon_index, desc="Enriching Sermons"):
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
        
        enriched_sermons.append(sermon)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = os.path.join(project_root, f"sermon_index_enriched_{timestamp}.json")
    
    with open(output_filename, "w") as f:
        json.dump(enriched_sermons, f, indent=4)
    print(f"Enriched sermon index saved to {output_filename}")

if __name__ == "__main__":
    main()
