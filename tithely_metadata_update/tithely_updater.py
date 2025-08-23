#!/usr/bin/env -S uv run --script

# tithely_updater.py
# assist from Gemini 2.5 Pro

import json
import os
import re
import sys
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright, Page, expect
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
# IMPORTANT: Fill these values in before running the script.
# It's best practice to use environment variables for credentials.
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
JSON_FILE_PATH = "sermons.json"  # The path to your sermon data file
SERMON_INDEX_PATH = "sermon_index.json" # The path to the sermon index file
BASE_URL = "https://stalfreds.tithelysetup.com"

# --- Find your Brave path ---
# Windows: C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe
# macOS: /Applications/Brave Browser.app/Contents/MacOS/Brave Browser
# Linux: /usr/bin/brave-browser (or similar)
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"

# Set to True to run without a visible browser window, False to watch it work
HEADLESS_MODE = False
# ---------------------

def create_sermon_slug(title: str, dt: datetime) -> str:
    """
    Creates a URL-friendly slug from a sermon title and date string that matches Tithely's format.
    """
    date_part = dt.strftime('%Y-%m-%d')
    slug = title.lower()
    # slug = slug.replace("'", "")
    slug = re.sub(r'[^a-z0-9]+', '-', slug)  # Replace non-alphanumeric with hyphen
    slug = slug.strip('-')
    full_slug = f"{date_part}-{slug}"
    truncated_slug = full_slug[:60]
    final_slug = truncated_slug.strip('-')
    return final_slug

def login(page: Page, email: str, password: str):
    """Navigates to the login page and logs in with provided credentials."""
    print("Navigating to login page...")
    page.goto(f"{BASE_URL}/login")

    # Use locators that are unlikely to change
    page.locator('input[name="user[email]"]').fill(email)
    page.locator('input[name="user[password]"]').fill(password)
    page.locator('button[type="submit"]').click()

    # Wait for login to complete by expecting the URL to change to the dashboard
    print("Login submitted. Waiting for dashboard...")
    expect(page.locator("text=You are now logged in")).to_be_visible(timeout=15000)
    print("Login successful!")

def create_sermon_index(page: Page):
    """
    Creates an index of all sermons with their slugs and page numbers.
    Returns a list of dictionaries with slugs and page numbers.
    """
    sermon_index = []
    current_page = 1

    while True:
        print(f"Processing page {current_page}...")
        sermon_links = page.locator("a.row.d-sm-flex[href^='/media/']")
        
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
                "page_url": page.url,
                "edit_url": link.get_attribute("href"),
                "title": title_texts[0].strip() if title_texts else "Unknown Title",
                "speaker": speaker_texts[0].strip() if speaker_texts else "Unknown Speaker",
                "date": date_texts[0].strip() if date_texts else "Unknown Date",
                "bible_passage": passage_texts[0].strip() if passage_texts else "Unknown Passage",
                "sermon_series": series_texts[0].strip() if series_texts else "Unknown Series",
            })

        if current_page > 140:  # Safety limit to avoid infinite loops
            print("Reached the end of the sermon list. Stopping index creation.")
            break

        # Check for the "Next" button
        next_button = page.get_by_role("link", name="→")
        if next_button.is_enabled():
            next_button.click()
            page.wait_for_load_state("domcontentloaded")
            current_page += 1
        else:
            print("No more pages to process.")
            break

    return sermon_index

def compare_and_group_sermons(sermons_json_path: str, sermon_index_path: str) -> dict:
    """
    Compares the local sermon data with the scraped sermon index and groups the sermons that need updating by page.
    """
    with open(sermons_json_path, 'r') as f:
        local_sermons = json.load(f)
    
    with open(sermon_index_path, 'r') as f:
        online_sermons = json.load(f)

    local_sermons_dict = {create_sermon_slug(s['title'], pd.to_datetime(s['post_date_gmt'], utc=True).tz_convert('Australia/Melbourne')): s for s in local_sermons}
    
    updates_by_page = {}

    for online_sermon in online_sermons:
        slug = online_sermon['slug']
        if slug in local_sermons_dict:
            local_sermon = local_sermons_dict[slug]
            
            # Compare fields to see if an update is needed
            update_needed = False
            if local_sermon.get("preacher") != online_sermon.get("speaker"):
                update_needed = True
            if local_sermon.get("sermon_series") != online_sermon.get("sermon_series"):
                update_needed = True
            if local_sermon.get("bible_passage") != online_sermon.get("bible_passage"):
                update_needed = True

            if update_needed:
                page_url = online_sermon['page_url']
                if page_url not in updates_by_page:
                    updates_by_page[page_url] = []
                
                updates_by_page[page_url].append({
                    "edit_url": online_sermon['edit_url'],
                    "title": local_sermon['title'],
                    "preacher": local_sermon.get('preacher', 'Guest Speaker'),
                    "sermon_series": local_sermon.get('sermon_series', ''),
                    "bible_passage": local_sermon.get('bible_passage', '')
                })

    return updates_by_page

def fill_and_submit_sermon_form(page: Page, sermon_data: dict):
    """Fills and submits the sermon form after the modal is opened."""
    form_locator = page.locator("form[id^='edit_sermon_']")
    expect(form_locator).to_be_visible(timeout=10000)
    print("Form is visible. Filling details...")

    form_locator.locator("#sermon_title").fill(sermon_data.get("title", ""))
    form_locator.locator("#sermon_subtitle").fill("")

    speaker_name = sermon_data.get("preacher", "Guest Speaker")
    speaker_select = form_locator.locator("#sermon_speaker_id")
    try:
        speaker_select.select_option(label=speaker_name)
    except Exception:
        speaker_select.select_option(label="Guest Speaker")

    form_locator.locator("#sermon_podcast_id").select_option(value="3")

    # Sermon series: create or select existing
    series_name = sermon_data.get("sermon_series", "")
    series_select = form_locator.locator("#sermon_series_id") # <-- Assuming this ID
    if series_select:
        try:
            series_select.select_option(label=series_name)
            print(f"Selected existing series: {series_name}")
        except Exception:
            print(f"Series '{series_name}' not found. Creating new one.")
            series_select.select_option(value="new")
            form_locator.locator("#sermon_series_title").fill(series_name)

    form_locator.locator('[name="sermon[passages]"]').fill(sermon_data.get("bible_passage", ""))

    # Click Save
    print("Submitting the form...")
    save_button = form_locator.locator("button[type='submit']:has-text('Save Sermon')")
    save_button.click()

    # Verify Success
    try:
        expect(page.locator("text=Updated Sermon")).to_be_visible(timeout=20000)
        print(f"✅ Successfully updated: {sermon_data.get('title')}")
    except Exception:
        print("❌ ERROR: Could not confirm successful update. Check if the form was submitted correctly.")
        return

def main():
    """Main function to orchestrate the browser automation."""
    if not TITHELY_EMAIL or not TITHELY_PASSWORD:
        print("❌ ERROR: Please provide TITHELY_EMAIL and TITHELY_PASSWORD as environment variables.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=BRAVE_EXECUTABLE_PATH,
            headless=HEADLESS_MODE,
            slow_mo=50  # Adds a small delay to see what's happening
        )
        context = browser.new_context()
        page = context.new_page()

        try:
            # Step 1: Log in once at the beginning of the session
            login(page, TITHELY_EMAIL, TITHELY_PASSWORD)

            # Step 2: Navigate to the sermons list page before the loop starts
            podcast_list_url = f"{BASE_URL}/podcasts/test-sermon-import"
            print(f"Navigating to the sermon list page: {podcast_list_url}")
            page.goto(podcast_list_url)
            expect(page.locator("h1:has-text('Test Sermon Import')")).to_be_visible()

            # Step 3: Create an index of all sermons if it doesn't exist
            if not os.path.exists(SERMON_INDEX_PATH):
                print("Sermon index not found. Creating it now...")
                sermon_index = create_sermon_index(page)
                with open(SERMON_INDEX_PATH, "w") as index_file:
                    json.dump(sermon_index, index_file, indent=4)
                print(f"Found {len(sermon_index)} sermons in the index.")
            else:
                print("Sermon index found. Skipping index creation.")

            # Step 4: Compare and group sermons for update
            updates_by_page = compare_and_group_sermons(JSON_FILE_PATH, SERMON_INDEX_PATH)
            
            if not updates_by_page:
                print("No sermons need updating.")
                return

            print(f"Found {sum(len(s) for s in updates_by_page.values())} sermons to update across {len(updates_by_page)} pages.")

            # Step 5: Loop through each page and update the sermons
            for page_url, sermons_to_update in updates_by_page.items():
                print(f"\n--- Navigating to page: {page_url} ---")
                page.goto(page_url)
                for sermon in sermons_to_update:
                    try:
                        print(f"Processing sermon: {sermon['title']}")
                        # Find the edit button and click it
                        edit_button = page.locator(f"a.js-sermon-form-link[href^='{sermon['edit_url']}/edit']")
                        edit_button.click()
                        
                        fill_and_submit_sermon_form(page, sermon)
                        
                        # After updating, we are on the sermon detail page. Go back to the index page.
                        page.goto(page_url)

                    except Exception as e:
                        print(f"❌ An error occurred while processing '{sermon.get('title', 'Unknown Sermon')}': {e}")
                        print("Reloading the page to recover...")
                        page.reload()
                        print(f"Current URL: {page.url}")

            print("\n🎉 All sermons have been processed.")

        except Exception as e:
            print(f"An unexpected error occurred during the process: {e}")
            # Take a screenshot on failure for debugging
            page.screenshot(path="error_screenshot.png")
            print("Screenshot saved to error_screenshot.png")
        finally:
            browser.close()


if __name__ == "__main__":
    main()