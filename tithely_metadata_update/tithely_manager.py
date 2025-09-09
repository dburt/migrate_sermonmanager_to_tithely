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

    def create_sermon_index(self, listing_url="/media/listing", full_details=False, with_audio_urls=False):
        """Creates an index of all sermons with their slugs and page numbers."""
        self.page.goto(f"{self.base_url}{listing_url}")
        
        sermon_data_list = []
        current_page = 1
        while True:
            print(f"Processing page {current_page}...")
            self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)
            sermon_rows = self.page.locator("table.table-hover.table-align-middle.table-nowrap tr")
            if not sermon_rows.count():
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
                print("Reached the end of the sermon list. Stopping index creation.")
                break
            next_button = self.page.get_by_role("link", name="→")
            if next_button.is_enabled():
                next_button.click()
                self.page.wait_for_load_state("domcontentloaded")
                current_page += 1
            else:
                print("No more pages to process.")
                break

        if with_audio_urls:
            for sermon_data in sermon_data_list:
                sermon_data['audio_url'] = self.get_audio_download_url(sermon_data['detail_page_url'])

        if full_details:
            for sermon_data in sermon_data_list:
                sermon_data.update(self.get_sermon_details(sermon_data['detail_page_url']))

        return sermon_data_list

    def get_sermon_details(self, sermon_url: str) -> dict:
        """Gets additional details from a sermon detail page."""
        print(f"Getting full details from: {sermon_url}")
        self.page.goto(f"{self.base_url}{sermon_url}")
        
        # NOTE: This is a placeholder. We need to inspect the sermon page
        # to determine what additional details are available and how to scrape them.
        details = {
            "description": self.page.locator(".sermon-description").first.inner_text().strip() if self.page.locator(".sermon-description").count() > 0 else "",
        }
        
        self.page.go_back()
        return details

    def get_audio_download_url(self, sermon_url: str) -> str:
        """Gets the audio download URL from a sermon detail page."""
        print(f"Getting audio download URL from: {sermon_url}")
        self.page.goto(f"{self.base_url}{sermon_url}")
        download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
        if download_link.count() > 0:
            return download_link.first.get_attribute("href")
        return ""

    def get_file_size(self, url: str) -> int:
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
