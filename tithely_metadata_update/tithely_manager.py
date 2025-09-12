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

    def create_sermon_index(self, listing_url="/media/listing", enrich_details=False, detail_scrape_limit=None, with_file_sizes=False, start_page=1):
        """Creates an index of all sermons, optionally enriching it with details from each sermon's page."""
        if start_page > 1:
            print(f"Jumping to page {start_page}...")
            self.page.goto(f"{self.base_url}{listing_url}?page={start_page}")
        else:
            self.page.goto(f"{self.base_url}{listing_url}")
        
        sermon_data_list = []
        current_page = start_page
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

        post_id = sermon_data.get("post_id")
        post_id_tag = f"[post_id={post_id}]" if post_id else ""

        # Fill title
        form_locator.locator("#sermon_title").fill(sermon_data.get("title", ""))
        
        # Fill subtitle with post_id tag
        if post_id_tag:
            form_locator.locator("#sermon_subtitle").fill(post_id_tag)

        # Fill speaker
        speaker_name = sermon_data.get("preacher", "Guest Speaker")
        speaker_select = form_locator.locator("#sermon_speaker_id")
        try:
            speaker_select.select_option(label=speaker_name, timeout=2000)
        except Exception:
            speaker_select.select_option(label="Guest Speaker")

        # Fill podcast
        form_locator.locator("#sermon_podcast_id").select_option(value="5")

        # Fill series
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

        # Fill bible passage
        bible_passage = sermon_data.get('bible_passage')
        if bible_passage and pd.notna(bible_passage):
            form_locator.locator('[name="sermon[passages]"]').fill(bible_passage)

        # Construct and fill description
        content_text = sermon_data.get('content_text', '')
        preacher = sermon_data.get('preacher', 'the speaker')
        title = sermon_data.get('title', 'the sermon')
        sermon_series = sermon_data.get('sermon_series', 'this series')
        
        description_parts = []
        if content_text and pd.notna(content_text):
            description_parts.append(str(content_text))
            
        description_parts.append(f"In this sermon, {preacher} speaks on the theme of '{title}' as part of the series '{sermon_series}'.")
        if bible_passage and pd.notna(bible_passage):
            description_parts.append(f"The bible reading is {bible_passage}.")
        if post_id_tag:
            description_parts.append(post_id_tag)
            
        new_description = " ".join(description_parts)

        try:
            # Use TinyMCE API to set the content
            self.page.evaluate("""
                (newContent) => {
                    var editor = tinymce.get('sermon_topic');
                    editor.setContent('<p>' + newContent.replace(/\\n/g, '<br>') + '</p>');
                }
            """, new_description)
            print("Updated description via TinyMCE API.")
        except Exception as e:
            print(f"❌ ERROR: Could not update description via TinyMCE API. Error: {e}")
            form_locator.locator("#sermon_topic").fill(new_description)

        print("Submitting the form...")
        save_button = form_locator.locator("button[type='submit']:has-text('Save Sermon')")
        save_button.click()
        try:
            expect(self.page.locator("text=Updated Sermon")).to_be_visible(timeout=10000)
            print(f"✅ Successfully updated: {sermon_data.get('title')}")
        except Exception:
            print("❌ ERROR: Could not confirm successful update. Check if the form was submitted correctly.")
            return

    def update_sermon(self, sermon_data: dict):
        """Navigates to a sermon's list page, opens the edit modal, and updates the sermon."""
        
        sermon_page_url = sermon_data['page_url']
        sermon_edit_url = sermon_data['edit_url']

        print(f"Navigating to sermon list page: {sermon_page_url}")
        self.page.goto(sermon_page_url)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)

        print("Finding sermon row...")
        sermon_row_selector = f"tr:has(a.js-sermon-form-link[href^='{sermon_edit_url}'])"
        sermon_row = self.page.locator(sermon_row_selector)
        
        if sermon_row.count() == 0:
            print(f"❌ Could not find the sermon row on page {sermon_page_url}.")
            return False

        print("Hovering over sermon row to reveal actions...")
        sermon_row.hover()

        print("Finding and clicking the 'More' button for the sermon...")
        more_button_selector = "button[data-toggle='dropdown'][title='More']"
        more_button = sermon_row.locator(more_button_selector)
        
        if more_button.count() == 0:
            print("❌ Could not find the 'More' button in the sermon row.")
            return False
            
        more_button.click()

        print("Finding and clicking the edit button...")
        edit_selector = f"a.js-sermon-form-link[href^='{sermon_edit_url}']"
        edit_button = self.page.locator(edit_selector)
        
        if edit_button.count() == 0:
            print("❌ Could not find the edit button after clicking 'More'.")
            return False

        edit_button.click()
        
        self.fill_and_submit_sermon_form(sermon_data)
        return True

    def debug_sermon_page(self, sermon_page_url: str, sermon_edit_url: str):
        """Navigates to a sermon's list page, opens the edit modal, and saves the DOM."""
        print("--- Starting Debug Mode ---")
        self.login()
        
        print(f"Navigating to sermon list page: {sermon_page_url}")
        self.page.goto(sermon_page_url)
        self.page.wait_for_load_state("networkidle")

        print("Finding sermon row...")
        sermon_row_selector = f"tr:has(a.js-sermon-form-link[href^='{sermon_edit_url}'])"
        sermon_row = self.page.locator(sermon_row_selector)
        
        if sermon_row.count() == 0:
            print("❌ Could not find the sermon row on the page.")
            return

        print("Hovering over sermon row to reveal actions...")
        sermon_row.hover()

        print("Finding and clicking the 'More' button for the sermon...")
        more_button_selector = "button[data-toggle='dropdown'][title='More']"
        more_button = sermon_row.locator(more_button_selector)
        
        if more_button.count() == 0:
            print("❌ Could not find the 'More' button in the sermon row.")
            return
            
        more_button.click()

        print("Finding and clicking the edit button...")
        edit_selector = f"a.js-sermon-form-link[href^='{sermon_edit_url}']"
        edit_button = self.page.locator(edit_selector)
        
        if edit_button.count() == 0:
            print("❌ Could not find the edit button after clicking 'More'.")
            return

        edit_button.click()
        
        print("Waiting for edit modal to load...")
        form_locator = self.page.locator("form[id^='edit_sermon_']")
        expect(form_locator).to_be_visible(timeout=10000)
        
        print("Dumping DOM to disk...")
        os.makedirs("dom_captures", exist_ok=True)
        with open("dom_captures/edit_modal.html", "w") as f:
            f.write(self.page.content())
        
        print("DOM saved to dom_captures/edit_modal.html")
        print("Quitting browser.")


if __name__ == "__main__":
    print("This is a library and should not be run directly.")
    print("Use run_updater.py or run_analyzer.py instead.")
    sys.exit(1)