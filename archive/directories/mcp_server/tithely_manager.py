#!/usr/bin/env -S uv run --script

# tithely_manager.py

import json
import os
import re
import sys
import pandas as pd
import httpx
from datetime import datetime
from playwright.async_api import async_playwright, Page, expect
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

    async def __aenter__(self):
        await self.start_browser()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop_browser()

    async def start_browser(self):
        """Starts the Playwright browser instance."""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            executable_path=self.brave_executable_path,
            headless=self.headless,
            slow_mo=50
        )
        self.page = await self.browser.new_page()
        print("Browser started.")

    async def stop_browser(self):
        """Stops the Playwright browser instance."""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        print("Browser stopped.")

    async def login(self):
        """Navigates to the login page and logs in with provided credentials."""
        print("Navigating to login page...")
        await self.page.goto(f"{self.base_url}/login")
        await self.page.locator('input[name="user[email]"]').fill(self.email)
        await self.page.locator('input[name="user[password]"]').fill(self.password)
        await self.page.locator('button[type="submit"]').click()
        print("Login submitted. Waiting for dashboard...")
        await expect(self.page.locator("text=You are now logged in")).to_be_visible(timeout=15000)
        print("Login successful!")

    async def create_main_listing_index(self, listing_url="/media/listing", full_details=False, with_audio_urls=False, detail_scrape_limit=None, start_page=1, end_page=None):
        """Creates an index of all sermons with their slugs and page numbers."""
        
        current_page = start_page
        start_url = f"{self.base_url}{listing_url}"
        if current_page > 1:
            start_url += f"?page={current_page}"

        await self.page.goto(start_url)
        
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
            await self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)
            sermon_rows = self.page.locator("table.table-hover.table-align-middle.table-nowrap tr")
            
            if await sermon_rows.count() <= 1:
                print("No more sermons found on this page.")
                break
            
            for row in await sermon_rows.all():
                if await row.locator("th").count() > 0: # Skip header row
                    continue
                title_link = row.locator("td.table-item-name a").first
                href = await title_link.get_attribute("href")
                slug_match = re.search(r'/media/([^/]+)', href)
                slug = slug_match.group(1) if slug_match else "Unknown Slug"
                edit_link = row.locator("a.js-sermon-form-link").first
                edit_url = await edit_link.get_attribute("href")
                
                podcast_slug = None
                if "?podcast=" in edit_url:
                    podcast_slug = edit_url.split("?podcast=")[-1]

                if podcast_slug == 'media':
                    print(f"Skipping sermon (already processed, in 'media' podcast): {await title_link.inner_text()}")
                    continue

                sermon_data = {
                    "slug": slug,
                    "page": current_page,
                    "page_url": self.page.url,
                    "edit_url": edit_url,
                    "title": await title_link.inner_text(),
                    "speaker": await row.locator("td").nth(2).inner_text(),
                    "date": await row.locator("td").first.inner_text(),
                    "sermon_series": await row.locator("td").nth(3).get_attribute("title"),
                    "media_type": await row.locator("td").nth(4).inner_text(),
                    "podcast_slug": podcast_slug,
                    "detail_page_url": href,
                }
                sermon_data_list.append(sermon_data)

            if current_page > 140:
                print("Reached the safety page limit. Stopping index creation.")
                break
            
            if full_details and detail_scrape_limit is not None and len(sermon_data_list) >= detail_scrape_limit:
                print(f"Collected basic info for {len(sermon_data_list)} sermons (limit was {detail_scrape_limit}).")
                break

            next_button = self.page.get_by_role("link", name="→")
            if await next_button.is_enabled():
                await next_button.click()
                await self.page.wait_for_load_state("domcontentloaded")
                current_page += 1
            else:
                print("No more pages to process.")
                break

        if full_details:
            sermons_to_scrape = sermon_data_list
            if detail_scrape_limit is not None:
                sermons_to_scrape = sermon_data_list[:detail_scrape_limit]
            
            print(f"Fetching full details for {len(sermons_to_scrape)} sermons...")
            for sermon_data in sermons_to_scrape:
                details = await self.get_sermon_details(sermon_data['detail_page_url'], sermon_data['slug'])
                sermon_data.update(details)
                
                if sermon_data.get('audio_url'):
                    sermon_data['audio_file_size'] = await self.get_file_size(sermon_data['audio_url'])
                else:
                    sermon_data['audio_file_size'] = 0
        
        elif with_audio_urls:
            print(f"Fetching audio URLs for {len(sermon_data_list)} sermons...")
            for sermon_data in sermon_data_list:
                sermon_data['audio_url'] = await self.get_audio_download_url(sermon_data['detail_page_url'])
                if sermon_data['audio_url']:
                    sermon_data['audio_file_size'] = await self.get_file_size(sermon_data['audio_url'])
                else:
                    sermon_data['audio_file_size'] = 0

        return sermon_data_list

    async def get_sermon_details(self, sermon_url: str, slug: str) -> dict:
        """Gets additional details from a sermon detail page and saves the DOM."""
        details = {"bible_passage": "", "description": "", "audio_url": ""}
        try:
            print(f"Getting full details from: {sermon_url}")
            await self.page.goto(f"{self.base_url}{sermon_url}", timeout=30000)
            await self.page.wait_for_selector(".article.mt-3", state="attached", timeout=15000)

            passage_container_locator = self.page.locator("div.py-3:has(h2:text-is('Bible Passage'))")
            if await passage_container_locator.count() > 0:
                details["bible_passage"] = await passage_container_locator.evaluate(
                    'element => { let passage = ""; for (const node of element.childNodes) { if (node.nodeType === Node.TEXT_NODE && node.textContent.trim() !== "") { passage = node.textContent.trim(); break; } } return passage; }'
                )
            
            description_locator = self.page.locator(".article.mt-3")
            if await description_locator.count() > 0:
                details["description"] = await description_locator.locator("p").first.inner_text()

            download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
            if await download_link.count() > 0:
                details["audio_url"] = await download_link.first.get_attribute("href")
        except Exception as e:
            print(f"❌ Could not process page {sermon_url}. Error: {e}")
        
        return details

    async def get_audio_download_url(self, sermon_url: str) -> str:
        """Gets the audio download URL from a sermon detail page."""
        try:
            await self.page.goto(f"{self.base_url}{sermon_url}", timeout=30000)
            download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
            if await download_link.count() > 0:
                return await download_link.first.get_attribute("href")
        except Exception as e:
            print(f"❌ Could not get audio URL from {sermon_url}. Error: {e}")
        return ""

    async def get_file_size(self, url: str) -> int:
        """Gets the file size in bytes from a URL using a HEAD request."""
        if not isinstance(url, str) or not url.startswith('http'):
            return 0
        try:
            async with httpx.AsyncClient() as client:
                response = await client.head(url, timeout=10, follow_redirects=True)
                response.raise_for_status()
                file_size = response.headers.get('Content-Length')
                if file_size:
                    return int(file_size)
        except httpx.RequestError as e:
            print(f"❌ Could not get file size for {url}. Error: {e}")
        return 0

    async def update_sermon(self, sermon_data: dict):
        """Navigates to a sermon's list page, opens the edit modal, and updates the sermon."""
        sermon_page_url = sermon_data['page_url']
        sermon_edit_url = sermon_data['edit_url']

        print(f"Navigating to sermon list page: {sermon_page_url}")
        await self.page.goto(sermon_page_url)
        await self.page.wait_for_load_state("networkidle")
        await self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=5000)

        sermon_row_selector = f"tr:has(a.js-sermon-form-link[href='{sermon_edit_url}'])"
        sermon_row = self.page.locator(sermon_row_selector)
        
        if await sermon_row.count() == 0:
            print(f"❌ Could not find the sermon row on page {sermon_page_url}.")
            return False

        await sermon_row.hover()
        more_button = sermon_row.locator("button[data-toggle='dropdown'][title='More']")
        await more_button.click(force=True)
        
        edit_button = self.page.locator(f"a.js-sermon-form-link[href='{sermon_edit_url}']")
        await edit_button.wait_for(state='visible', timeout=5000)
        await edit_button.click()
        
        await self.fill_and_submit_sermon_form(sermon_data)
        await self.page.wait_for_load_state("networkidle", timeout=20000)
        return True

    async def fill_and_submit_sermon_form(self, sermon_data: dict):
        """Fills and submits the sermon form after the modal is opened."""
        form_locator = self.page.locator("form[id^='edit_sermon_']")
        await expect(form_locator).to_be_visible(timeout=5000)
        print("Form is visible. Filling details...")

        # ... [The logic for filling the form remains the same, just add await] ...

        await form_locator.locator("#sermon_title").fill(sermon_data.get("title_local", ""))
        await form_locator.locator("#sermon_subtitle").fill("")
        
        speaker_select = form_locator.locator("#sermon_speaker_id")
        try:
            await speaker_select.select_option(label=sermon_data.get("preacher", "Guest Speaker"), timeout=2000)
        except Exception:
            await speaker_select.select_option(label="Guest Speaker")

        await form_locator.locator("#sermon_podcast_id").select_option(value="1")

        series_name = sermon_data.get("sermon_series_local", "")
        if pd.notna(series_name) and series_name.strip():
            series_select = form_locator.locator("#sermon_series_id")
            try:
                await series_select.select_option(label=series_name, timeout=2000)
            except Exception:
                await series_select.select_option(value="new")
                await form_locator.locator("#sermon_series_title").fill(series_name)

        # ... [Rest of the form filling] ...

        save_button = form_locator.locator("button[type='submit']:has-text('Save Sermon')")
        await save_button.click()
        await expect(form_locator).to_be_hidden(timeout=15000)
        print(f"✅ Successfully updated: {sermon_data.get('title_local')}")


if __name__ == "__main__":
    print("This is a library and should not be run directly.")
    sys.exit(1)
