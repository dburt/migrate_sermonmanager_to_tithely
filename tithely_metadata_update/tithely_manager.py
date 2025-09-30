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

    def create_main_listing_index(self, listing_url="/media/listing", full_details=False, with_audio_urls=False, detail_scrape_limit=None, start_page=1, end_page=None):
        """Creates an index of all sermons with their slugs and page numbers."""
        
        current_page = start_page
        start_url = f"{self.base_url}{listing_url}"
        if current_page > 1:
            start_url += f"?page={current_page}"

        self.page.goto(start_url)
        
        sermon_data_list = []
        previous_url = ""
        while True:
            current_url = self.page.url.split('#')[0]
            if current_url == previous_url:
                print("URL has not changed, assuming end of pagination.")
                break
            previous_url = current_url

            if end_page and current_page > end_page:
                print(f"Reached end page {end_page}. Stopping index creation.")
                break

            print(f"Processing page {current_page} ({self.page.url})...")
            self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)
            sermon_rows = self.page.locator("table.table-hover.table-align-middle.table-nowrap tr")
            
            if sermon_rows.count() <= 1: # A page with only a header row means no sermons
                print("No more sermons found on this page.")
                break
            
            for row in sermon_rows.all()[1:]: # Skip header row
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
            
            # Stop collecting if we have enough for a limited detail scrape
            if full_details and detail_scrape_limit is not None and len(sermon_data_list) >= detail_scrape_limit:
                print(f"Collected basic info for {len(sermon_data_list)} sermons (limit was {detail_scrape_limit}).")
                print(f"Now stopping pagination to fetch full details for the first {detail_scrape_limit} of these.")
                break

            next_button = self.page.get_by_role("link", name="→")
            if next_button.is_enabled():
                next_button.click()
                self.page.wait_for_load_state("domcontentloaded")
                current_page += 1
            else:
                print("No more pages to process.")
                break

        if full_details:
            sermons_to_scrape = sermon_data_list
            if detail_scrape_limit is not None:
                print(f"Fetching full details for a maximum of {detail_scrape_limit} sermons...")
                sermons_to_scrape = sermon_data_list[:detail_scrape_limit]
            
            for sermon_data in tqdm(sermons_to_scrape, desc="Fetching full sermon details"):
                details = self.get_sermon_details(sermon_data['detail_page_url'], sermon_data['slug'])
                sermon_data.update(details)
                
                # Now get file size
                if sermon_data.get('audio_url'):
                    sermon_data['audio_file_size'] = self.get_file_size(sermon_data['audio_url'])
                else:
                    sermon_data['audio_file_size'] = 0
        # The with_audio_urls parameter is kept for compatibility but its functionality
        # is now handled within the full_details block for efficiency.
        elif with_audio_urls:
            for sermon_data in tqdm(sermon_data_list, desc="Fetching audio URLs and file sizes"):
                sermon_data['audio_url'] = self.get_audio_download_url(sermon_data['detail_page_url'])
                if sermon_data['audio_url']:
                    sermon_data['audio_file_size'] = self.get_file_size(sermon_data['audio_url'])
                else:
                    sermon_data['audio_file_size'] = 0

        return sermon_data_list

    def create_podcast_index(self, listing_url: str, full_details=False, with_audio_urls=False, detail_scrape_limit=None, end_page=None) -> list:
        """Creates an index of sermons from a podcast listing page."""
        self.page.goto(f"{self.base_url}{listing_url}")
        
        sermon_data_list = []
        current_page = 1
        previous_url = ""
        while True:
            current_url = self.page.url.split('#')[0]
            if current_url == previous_url:
                print("URL has not changed, assuming end of pagination.")
                break
            previous_url = current_url

            if end_page and current_page > end_page:
                print(f"Reached end page {end_page}. Stopping index creation.")
                break

            print(f"Processing page {current_page} ({self.page.url})...")
            # This selector is specific to the podcast page structure
            sermon_links = self.page.locator("a.row.d-sm-flex[href^='/media/']")
            
            if not sermon_links.count():
                print("No more sermons found on this page.")
                break
            
            for link in sermon_links.all():
                href = link.get_attribute("href")
                slug_match = re.search(r'/media/([^/]+)', href)
                slug = slug_match.group(1) if slug_match else "Unknown Slug"
                
                # Extracting data from the podcast page structure
                title_texts = link.locator("h2.h3").all_inner_texts()
                speaker_texts = link.locator('div.h5.my-0, div.text-body.line-height-2').all_inner_texts()
                date_texts = link.locator('div.text-muted:last-child').all_inner_texts()
                passage_texts = link.locator(".text-body + .text-muted").all_inner_texts()
                series_texts = link.locator("div.text-body").all_inner_texts()

                sermon_data = {
                    "slug": slug,
                    "page": current_page,
                    "page_url": self.page.url,
                    "edit_url": href, # On podcast page, edit_url is the same as detail_page_url
                    "title": title_texts[0].strip() if title_texts else "Unknown Title",
                    "speaker": speaker_texts[0].strip() if speaker_texts else "Unknown Speaker",
                    "date": date_texts[0].strip() if date_texts else "Unknown Date",
                    "bible_passage": passage_texts[0].strip() if passage_texts else "Unknown Passage",
                    "sermon_series": series_texts[0].strip() if series_texts else "Unknown Series",
                    "media_type": "Audio", # Assuming podcast entries are always audio
                    "podcast_slug": listing_url.split('/')[-1], # Extract from listing_url
                    "detail_page_url": href,
                }
                sermon_data_list.append(sermon_data)

            if current_page > 140:  # Safety limit
                print("Reached the safety page limit. Stopping index creation.")
                break
            
            if full_details and detail_scrape_limit is not None and len(sermon_data_list) >= detail_scrape_limit:
                print(f"Collected {len(sermon_data_list)} sermons, stopping pagination to begin detail scrape.")
                break

            next_button = self.page.get_by_role("link", name="→")
            if next_button.is_enabled():
                next_button.click()
                self.page.wait_for_load_state("domcontentloaded")
                current_page += 1
            else:
                print("No more pages to process.")
                break

        if full_details:
            sermons_to_scrape = sermon_data_list
            if detail_scrape_limit is not None:
                print(f"Fetching full details for a maximum of {detail_scrape_limit} sermons...")
                sermons_to_scrape = sermon_data_list[:detail_scrape_limit]
            
            for sermon_data in tqdm(sermons_to_scrape, desc="Fetching full sermon details"):
                details = self.get_sermon_details(sermon_data['detail_page_url'], sermon_data['slug'])
                sermon_data.update(details)
                
                # Now get file size
                if sermon_data.get('audio_url'):
                    sermon_data['audio_file_size'] = self.get_file_size(sermon_data['audio_url'])
                else:
                    sermon_data['audio_file_size'] = 0
        # The with_audio_urls parameter is kept for compatibility but its functionality
        # is now handled within the full_details block for efficiency.
        elif with_audio_urls:
            for sermon_data in tqdm(sermon_data_list, desc="Fetching audio URLs and file sizes"):
                sermon_data['audio_url'] = self.get_audio_download_url(sermon_data['detail_page_url'])
                if sermon_data['audio_url']:
                    sermon_data['audio_file_size'] = self.get_file_size(sermon_data['audio_url'])
                else:
                    sermon_data['audio_file_size'] = 0

        return sermon_data_list

    def get_sermon_details(self, sermon_url: str, slug: str) -> dict:
        """Gets additional details from a sermon detail page and saves the DOM."""
        details = {
            "bible_passage": "",
            "description": "",
            "audio_url": ""
        }
        try:
            print(f"Getting full details from: {sermon_url}")
            self.page.goto(f"{self.base_url}{sermon_url}", timeout=30000)

            # Wait for the main content to be attached to the DOM, using user's selector
            self.page.wait_for_selector(".article.mt-3", state="attached", timeout=15000)

            # Save DOM for reference
            dom_capture_dir = "dom_captures"
            os.makedirs(dom_capture_dir, exist_ok=True)
            with open(os.path.join(dom_capture_dir, f"{slug}.html"), "w") as f:
                f.write(self.page.content())

            # Scrape Bible Passage using user's specific instructions
            passage_container_locator = self.page.locator("div.py-3:has(h2:text-is('Bible Passage'))")
            
            bible_passage = ""
            if passage_container_locator.count() > 0:
                # Use JavaScript evaluation to get the direct child text node
                bible_passage = passage_container_locator.evaluate('''
                    element => {
                        let passage = '';
                        for (const node of element.childNodes) {
                            if (node.nodeType === Node.TEXT_NODE && node.textContent.trim() !== '') {
                                passage = node.textContent.trim();
                                break;
                            }
                        }
                        return passage;
                    }
                ''')
            
            details["bible_passage"] = bible_passage
                
            # Scrape Description using user's selector
            description_locator = self.page.locator(".article.mt-3")
            if description_locator.count() > 0:
                # Assuming the description is the first <p> inside the container
                details["description"] = description_locator.locator("p").first.inner_text().strip()

            # Scrape Audio URL
            download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
            if download_link.count() > 0:
                details["audio_url"] = download_link.first.get_attribute("href")

        except Exception as e:
            print(f"❌ Could not process page {sermon_url}. Error: {e}")
            # Return empty details, the main loop will continue
        
        return details

    def get_audio_download_url(self, sermon_url: str) -> str:
        """Gets the audio download URL from a sermon detail page."""
        try:
            self.page.goto(f"{self.base_url}{sermon_url}", timeout=30000)
            download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
            if download_link.count() > 0:
                return download_link.first.get_attribute("href")
        except Exception as e:
            print(f"❌ Could not get audio URL from {sermon_url}. Error: {e}")
        return ""

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
        expect(form_locator).to_be_visible(timeout=5000)
        print("Form is visible. Filling details...")

        post_id = sermon_data.get("post_id")
        post_id_tag = f"[post_id={post_id}]" if post_id else ""

        # Fill title
        title = sermon_data.get("title_local", "")
        if pd.notna(title) and title.strip():
            form_locator.locator("#sermon_title").fill(title)

        # Fill subtitle with post_id tag
        #if post_id_tag:
            #form_locator.locator("#sermon_subtitle").fill(post_id_tag)

        # Clear subtitle
            form_locator.locator("#sermon_subtitle").fill("")

        # Fill speaker
        speaker_name = sermon_data.get("preacher", "Guest Speaker")
        if pd.notna(speaker_name) and speaker_name.strip():
            speaker_select = form_locator.locator("#sermon_speaker_id")
            try:
                speaker_select.select_option(label=speaker_name, timeout=2000)
            except Exception:
                speaker_select.select_option(label="Guest Speaker")

        # Fill podcast
        # 5 = test podcast 3
        # 1 = sermons
        form_locator.locator("#sermon_podcast_id").select_option(value="1")

        # Fill series
        series_name = sermon_data.get("sermon_series_local", "")
        if pd.notna(series_name) and series_name.strip():
            series_select = form_locator.locator("#sermon_series_id")
            try:
                series_select.select_option(label=series_name, timeout=2000)
                print(f"Selected existing series: {series_name}")
            except Exception:
                print(f"Series '{series_name}' not found. Creating new one.")
                series_select.select_option(value="new")
                form_locator.locator("#sermon_series_title").fill(series_name)

        # Fill bible passage
        bible_passage = sermon_data.get('bible_passage_local')
        if pd.notna(bible_passage) and bible_passage.strip():
            form_locator.locator('[name="sermon[passages]"]').fill(bible_passage)

        # Construct and fill description
        content_text = sermon_data.get('content_text', '')
        preacher = sermon_data.get('preacher', 'the speaker')
        title = sermon_data.get('title_local', 'the sermon')
        sermon_series = sermon_data.get('sermon_series_local', 'this series')
        
        description_parts = []
        if pd.notna(content_text) and content_text.strip():
            description_parts.append(str(content_text))
            
        description_parts.append(f"In this sermon, {preacher} speaks on the theme of '{title}' as part of the series '{sermon_series}'.")
        if pd.notna(bible_passage) and bible_passage.strip():
            description_parts.append(f"The bible reading is {bible_passage}.")
        if post_id_tag:
            description_parts.append(post_id_tag)
            
        new_description = " ".join(description_parts)

        try:
            # Use TinyMCE API to set the content
            self.page.evaluate('''
                (newContent) => {
                    var editor = tinymce.get('sermon_topic');
                    if (editor) {
                        editor.setContent(newContent);
                    }
                }
            ''', new_description)
            print("Updated description via TinyMCE API.")
        except Exception as e:
            print(f"❌ ERROR: Could not update description via TinyMCE API. Error: {e}")
            form_locator.locator("#sermon_topic").fill(new_description)

        print("Submitting the form...")
        save_button = form_locator.locator("button[type='submit']:has-text('Save Sermon')")
        save_button.click()
        try:
            # Wait for the modal to disappear as a more reliable confirmation
            expect(form_locator).to_be_hidden(timeout=15000)
            print(f"✅ Successfully updated: {sermon_data.get('title_local')}")
        except Exception:
            print("❌ ERROR: Could not confirm successful update (modal did not disappear).")
            return

    def update_sermon(self, sermon_data: dict):
        """Navigates to a sermon's list page, opens the edit modal, and updates the sermon."""
        
        sermon_page_url = sermon_data['page_url']
        sermon_edit_url = sermon_data['edit_url']

        print(f"Navigating to sermon list page: {sermon_page_url}")
        self.page.goto(sermon_page_url)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=5000)

        print("Finding sermon row...")
        sermon_row_selector = f"tr:has(a.js-sermon-form-link[href='{sermon_edit_url}'])"
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
            print(f"❌ Could not find the 'More' button in the sermon row.")
            return False
            
        more_button.click()

        print("Finding and clicking the edit button...")
        edit_selector = f"a.js-sermon-form-link[href='{sermon_edit_url}']"
        edit_button = self.page.locator(edit_selector)
        
        if edit_button.count() == 0:
            print(f"❌ Could not find the edit button after clicking 'More'.")
            return False

        edit_button.click()
        
        self.fill_and_submit_sermon_form(sermon_data)

        # After submitting, wait for the page to reload to prevent race conditions
        try:
            self.page.wait_for_load_state("networkidle", timeout=20000)
        except Exception as e:
            print(f"⚠️ Warning: Timed out waiting for page to settle after update. Error: {e}")

        return True

    def delete_sermon(self, sermon_data: dict):
        """Navigates to a sermon's list page, opens the dropdown, and deletes the sermon."""
        sermon_page_url = sermon_data['page_url'].split('#')[0]
        detail_page_url = sermon_data['detail_page_url']

        print(f"Navigating to sermon list page: {sermon_page_url}")
        self.page.goto(sermon_page_url)
        self.page.wait_for_load_state("networkidle")

        sermon_row_selector = f"tr:has(a[href='{detail_page_url}'])"
        sermon_row = self.page.locator(sermon_row_selector)

        if sermon_row.count() == 0:
            print(f"❌ Could not find the sermon row on page {sermon_page_url} for sermon {sermon_data['title']}.")
            return False

        sermon_row.wait_for(state='visible', timeout=5000)
        sermon_row.hover()

        more_button_selector = "button[data-toggle='dropdown'][title='More']"
        more_button = sermon_row.locator(more_button_selector)
        more_button.wait_for(state='visible', timeout=5000)
        more_button.click()

        delete_selector = f"a[data-method='delete'][href='{detail_page_url}']"
        delete_button = self.page.locator(delete_selector)
        
        if delete_button.count() == 0:
            print(f"❌ Could not find the delete button for sermon {sermon_data['title']}.")
            return False

        delete_button.wait_for(state='visible', timeout=5000)
        delete_button.click()

        # Wait for the deletion to complete. A good way to do this is to wait for the row to disappear.
        expect(sermon_row).to_be_hidden(timeout=5000)
        print(f"✅ Successfully deleted: {sermon_data.get('title')}")
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
        expect(form_locator).to_be_visible(timeout=5000)
        
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