#!/usr/bin/env -S uv run --script

# tithely_manager.py

import json
import os
import re
import sys
import pandas as pd
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright, Page, expect
from dotenv import load_dotenv
from collections import defaultdict
from tqdm import tqdm

load_dotenv()

class TithelyManager:
    def __init__(self, email, password, brave_executable_path, headless=False):
        self.email = email
        self.password = password
        self.brave_executable_path = brave_executable_path
        self.headless = headless
        self.base_url = "https://stalfreds.tithelysetup.com"
        self.playwright = None
        self.browser = None
        self.page = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            executable_path=self.brave_executable_path,
            headless=self.headless,
            slow_mo=50
        )
        self.page = self.browser.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def login(self):
        """Navigates to the login page and logs in with provided credentials."""
        print("Navigating to login page...")
        self.page.goto(f"{self.base_url}/login")
        self.page.locator('input[name="user[email]"]').fill(self.email)
        self.page.locator('input[name="user[password]"]').fill(self.password)
        self.page.locator('button[type="submit"]').click()
        print("Login submitted. Waiting for dashboard...")
        expect(self.page.locator("text=You are now logged in")).to_be_visible(timeout=15000)
        print("Login successful!")

    def create_sermon_index(self, listing_url="/media/listing", enrich_details=False, detail_scrape_limit=None, with_file_sizes=False):
        """Creates an index of all sermons, optionally enriching it with details from each sermon's page."""
        self.page.goto(f"{self.base_url}{listing_url}")
        
        sermon_data_list = []
        current_page = 1
        previous_url = ""
        while True:
            if self.page.url == previous_url:
                print("URL has not changed, assuming end of pagination.")
                break
            previous_url = self.page.url

            print(f"Processing page {current_page} ({self.page.url})...")
            self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)
            sermon_rows = self.page.locator("table.table-hover.table-align-middle.table-nowrap tr")
            
            if sermon_rows.count() <= 1:
                print("No more sermons found on this page.")
                break
            
            for row in sermon_rows.all()[1:]:
                title_link = row.locator("td.table-item-name a").first
                href = title_link.get_attribute("href")
                slug_match = re.search(r'/media/([^/]+)', href)
                slug = slug_match.group(1) if slug_match else "Unknown Slug"
                edit_link = row.locator("a.js-sermon-form-link").first
                edit_url = edit_link.get_attribute("href")
                
                podcast_slug = None
                if "?podcast=" in edit_url:
                    podcast_slug = edit_url.split("?podcast=")[-1]

                sermon_data = {
                    "slug": slug,
                    "page": current_page,
                    "page_url": self.page.url,
                    "edit_url": edit_url,
                    "title": title_link.inner_text().strip(),
                    "speaker": row.locator("td").nth(2).inner_text().strip(),
                    "date": row.locator("td").first.inner_text().strip(),
                    "sermon_series": row.locator("td").nth(3).get_attribute("title"),
                    "media_type": row.locator("td").nth(4).inner_text().strip(),
                    "podcast_slug": podcast_slug,
                    "detail_page_url": href,
                }
                sermon_data_list.append(sermon_data)

            if current_page > 140:  # Safety limit
                print("Reached the safety page limit. Stopping index creation.")
                break
            
            if enrich_details and detail_scrape_limit is not None and len(sermon_data_list) >= detail_scrape_limit:
                print(f"Collected {len(sermon_data_list)} sermons, stopping pagination to begin enrichment.")
                break

            next_button = self.page.get_by_role("link", name="→")
            if next_button.is_enabled():
                next_button.click()
                self.page.wait_for_load_state("domcontentloaded")
                current_page += 1
            else:
                print("No more pages to process.")
                break

        sermons_to_process = sermon_data_list
        if detail_scrape_limit is not None:
            sermons_to_process = sermon_data_list[:detail_scrape_limit]

        if enrich_details:
            print(f"Enriching details for {len(sermons_to_process)} sermons...")
            for sermon_data in tqdm(sermons_to_process, desc="Enriching Sermons"):
                enriched_data = self.get_sermon_details_and_audio(sermon_data['detail_page_url'], sermon_data['slug'])
                sermon_data.update(enriched_data)

        if with_file_sizes:
            print(f"Fetching file sizes for {len(sermons_to_process)} sermons...")
            for sermon_data in tqdm(sermons_to_process, desc="Fetching File Sizes"):
                if sermon_data.get('audio_url') and 'audio_file_size' not in sermon_data:
                    sermon_data['audio_file_size'] = self.get_file_size(sermon_data['audio_url'])
        
        return sermon_data_list

    def get_sermon_details_and_audio(self, sermon_url: str, slug: str) -> dict:
        """
        Visits a sermon detail page once to get description, Bible passage, and audio URL.
        Saves the DOM for reference.
        """
        enriched_data = {
            "bible_passage": "",
            "description": "",
            "audio_url": ""
        }
        try:
            # print(f"Processing detail page: {sermon_url}") # Too noisy for full run
            self.page.goto(f"{self.base_url}{sermon_url}", timeout=30000)
            self.page.wait_for_selector(".article.mt-3", state="attached", timeout=15000)

            # Scrape Bible Passage
            passage_container_locator = self.page.locator("div.py-3:has(h2:text-is('Bible Passage'))")
            if passage_container_locator.count() > 0:
                enriched_data["bible_passage"] = passage_container_locator.evaluate(
                    """element => {
                        let passage = '';
                        for (const node of element.childNodes) {
                            if (node.nodeType === Node.TEXT_NODE && node.textContent.trim() !== '') {
                                passage = node.textContent.trim();
                                break;
                            }
                        }
                        return passage;
                    }"""
                )

            # Scrape Description
            description_locator = self.page.locator(".article.mt-3")
            if description_locator.count() > 0:
                enriched_data["description"] = description_locator.locator("p").first.inner_text().strip()

            # Scrape Audio URL
            download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
            if download_link.count() > 0:
                enriched_data["audio_url"] = download_link.first.get_attribute("href")

        except Exception as e:
            print(f"❌ Could not process page {sermon_url}. Error: {e}")
        
        return enriched_data

    def get_file_size(self, url: str) -> int:
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

    def fill_and_submit_sermon_form(self, sermon_data: dict):
        """Fills and submits the sermon form after the modal is opened."""
        form_locator = self.page.locator("form[id^='edit_sermon_']")
        expect(form_locator).to_be_visible(timeout=10000)
        print("Form is visible. Filling details...")
        form_locator.locator("#sermon_title").fill(sermon_data.get("title", ""))
        form_locator.locator("#sermon_subtitle").fill("")
        speaker_name = sermon_data.get("preacher", "Guest Speaker")
        speaker_select = form_locator.locator("#sermon_speaker_id")
        try:
            speaker_select.select_option(label=speaker_name, timeout=2000)
        except Exception:
            speaker_select.select_option(label="Guest Speaker")
        form_locator.locator("#sermon_podcast_id").select_option(value="5")
        series_name = sermon_data.get("sermon_series", "")
        series_select = form_locator.locator("#sermon_series_id")
        if series_select:
            try:
                series_select.select_option(label=series_name, timeout=2000)
                print(f"Selected existing series: {series_name}")
            except Exception:
                print(f"Series '{series_name}' not found. Creating new one.")
                series_select.select_option(value="new")
                form_locator.locator("#sermon_series_title").fill(series_name)
        form_locator.locator('[name="sermon[passages]"]').fill(sermon_data.get("bible_passage", ""))
        print("Submitting the form...")
        save_button = form_locator.locator("button[type='submit']:has-text('Save Sermon')")
        save_button.click()
        try:
            expect(self.page.locator("text=Updated Sermon")).to_be_visible(timeout=20000)
            print(f"✅ Successfully updated: {sermon_data.get('title')}")
        except Exception:
            print("❌ ERROR: Could not confirm successful update. Check if the form was submitted correctly.")
            return


if __name__ == "__main__":
    print("This is a library and should not be run directly.")
    print("Use run_updater.py or run_analyzer.py instead.")
    sys.exit(1)