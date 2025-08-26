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

    def create_sermon_index(self):
        """Creates an index of all sermons with their slugs and page numbers."""
        self.page.goto(f"{self.base_url}/podcasts/test-sermon-import")
        sermon_index = []
        current_page = 1
        while True:
            print(f"Processing page {current_page}...")
            sermon_links = self.page.locator("a.row.d-sm-flex[href^='/media/']")
            if not sermon_links.count():
                print("No more sermons found on this page.")
                break
            for link in sermon_links.all():
                slug_match = re.search(r'/media/([^/]+)', link.get_attribute("href"))
                title_texts = link.locator("h2.h3").all_inner_texts()
                speaker_texts = link.locator('div.h5.my-0, div.text-body.line-height-2').all_inner_texts()
                date_texts = link.locator('div.text-muted:last-child').all_inner_texts()
                passage_texts = link.locator(".text-body + .text-muted").all_inner_texts()
                series_texts = link.locator("div.text-body").all_inner_texts()
                sermon_index.append({
                    "slug": slug_match.group(1) if slug_match else "Unknown Slug",
                    "page": current_page,
                    "page_url": self.page.url,
                    "edit_url": link.get_attribute("href"),
                    "title": title_texts[0].strip() if title_texts else "Unknown Title",
                    "speaker": speaker_texts[0].strip() if speaker_texts else "Unknown Speaker",
                    "date": date_texts[0].strip() if date_texts else "Unknown Date",
                    "bible_passage": passage_texts[0].strip() if passage_texts else "Unknown Passage",
                    "sermon_series": series_texts[0].strip() if series_texts else "Unknown Series",
                })
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
        return sermon_index

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
        form_locator.locator("#sermon_podcast_id").select_option(value="3")
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
