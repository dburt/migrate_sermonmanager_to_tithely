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

# --- CONFIGURATION ---
# IMPORTANT: Fill these values in before running the script.
# It's best practice to use environment variables for credentials.
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
JSON_FILE_PATH = "sermons.json"  # The path to your sermon data file
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


# (This function finds the sermon, handling pagination)
def find_and_open_sermon_editor(page: Page, sermon_data: dict) -> bool:
    """
    Searches for a sermon's edit button, clicking through pagination if needed.
    Returns True if the edit button was found and clicked, False otherwise.
    """
    title = sermon_data.get("title")
    dt = pd.to_datetime(sermon_data.get("post_date_gmt"), utc=True).tz_convert('Australia/Melbourne')
    sermon_slug_to_find = create_sermon_slug(title, dt)
    
    print(f"\n--- Processing Sermon: {title} ---")
    print(f"Current time: {page.evaluate("new Date().toLocaleString()")}")
    print(f"Searching for link containing: '{sermon_slug_to_find}'")

    start_url = page.url
    print(f"Starting URL: {start_url}")

    ## This loop will continue as long as there are "Next" pages to click
    # while True:
    # This loop will try to find the sermon on the current or next two pages
    for _ in range(3):

        edit_button_locator = page.locator(f"a[title='Edit'][href*='{sermon_slug_to_find}']").first

        # Check if the sermon is on the CURRENT page. Use a short timeout.
        if edit_button_locator.is_visible(timeout=2000): # Short wait, just to check
            print("Found sermon on this page. Clicking 'Edit'...")
            edit_button_locator.click()
            return True # Success!

        # If not found, look for the "Next" button
        print("Sermon not found on this page. Looking for 'Next' button...")
        next_page_button = page.get_by_role("link", name="→")

        if next_page_button.is_enabled():
            print("Navigating to next page...")
            next_page_button.click()
            # Wait for the page to navigate before the loop continues
            page.wait_for_load_state("domcontentloaded")
        else:
            # We've checked the last page and didn't find it.
            print(f"❌ ERROR: Reached last page and could not find sermon '{title}'.")
            # return to starting URL
            print(f"Returning to starting URL: {start_url}")
            page.goto(start_url)
            return False # Failure
    
    # If we reach here, it means we didn't find the sermon in the first 3 pages
    print(f"❌ ERROR: Could not find sermon '{title}' after checking 3 pages.")
    # return to starting URL
    print(f"Returning to starting URL: {start_url}")
    page.goto(start_url)
    return False # Failure

# (This function just fills the form, assuming the modal is open)
def fill_and_submit_sermon_form(page: Page, sermon_data: dict):
    """Fills and submits the sermon form after the modal is opened."""
    print("Waiting for form modal...")
    form_locator = page.locator("form[id^='edit_sermon_']")
    expect(form_locator).to_be_visible(timeout=10000)
    print("Form modal is visible. Filling details...")

    form_locator.locator("#sermon_title").fill(sermon_data.get("title", ""))
    form_locator.locator("#sermon_subtitle").fill("")

    # Assume date is already correct and skip
    # sermon_date = sermon_data.get("post_date_gmt", "").split(" ")[0]
    # if sermon_date:
    #     form_locator.locator("#sermon_sermon_date").fill(sermon_date)

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

    try:
        with open(JSON_FILE_PATH, 'r') as f:
            sermons_to_update = json.load(f)
    except FileNotFoundError:
        print(f"❌ ERROR: JSON file not found at '{JSON_FILE_PATH}'")
        return

    sermons_to_update.reverse()
    print(f"Loaded and reversed {len(sermons_to_update)} sermons for processing.")

    # sermons_to_update = sermons_to_update[3:30] # DEBUG: limit to first 30 sermons starting with the 4th sermon to skip the first 3

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

            # Step 3: Loop through each sermon and update it
            for sermon in sermons_to_update:
                try:
                    was_found_and_opened = find_and_open_sermon_editor(page, sermon)
                    
                    if was_found_and_opened:
                        fill_and_submit_sermon_form(page, sermon)
                        # successful edit will redirect to sermon detail page
                        # use back navigation to return to the list where we left it
                        print("Returning to sermon list...")
                        page.go_back()
                        expect(page.locator("h1:has-text('Test Sermon Import')")).to_be_visible()
                    else:
                        print(f"Skipping '{sermon.get('title')}' as it could not be found.")

                except Exception as e:
                    print(f"❌ An error occurred while processing '{sermon.get('title', 'Unknown Sermon')}': {e}")
                    print("Reloading the page to recover...")
                    page.reload()
                    # print("Going back to previous page...")
                    # page.go_back()
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
