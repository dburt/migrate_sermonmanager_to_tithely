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
from typing import List, Dict, Any

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

    def start_browser(self):
        """Starts the Playwright browser instance."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            executable_path=self.brave_executable_path,
            headless=self.headless,
            slow_mo=50
        )
        self.page = self.browser.new_page()
        print("Browser started.")

    def stop_browser(self):
        """Stops the Playwright browser instance."""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        print("Browser stopped.")

    def login(self):
        """Navigates to the login page and logs in with provided credentials."""
        if not self.page:
            raise Exception("Browser not started. Call start_browser() first.")
        print("Navigating to login page...")
        self.page.goto(f"{self.base_url}/login")
        self.page.locator('input[name="user[email]"]').fill(self.email)
        self.page.locator('input[name="user[password]"]').fill(self.password)
        self.page.locator('button[type="submit"]').click()
        print("Login submitted. Waiting for dashboard...")
        expect(self.page.locator("text=You are now logged in")).to_be_visible(timeout=15000)
        print("Login successful!")

    def explore(self, url: str, actions: List[Dict[str, Any]]) -> List[Any]:
        """Navigates to a URL and performs a series of actions."""
        if not self.page:
            raise Exception("Browser not started. Call start_browser() first.")
        
        print(f"Navigating to {url}...")
        self.page.goto(url)
        
        results = []
        for action in actions:
            cmd = action.get("action")
            selector = action.get("selector")
            text = action.get("text")
            
            print(f"Performing action: {cmd}")
            try:
                if cmd == "click":
                    self.page.locator(selector).click(force=True)
                elif cmd == "fill":
                    self.page.locator(selector).fill(text)
                elif cmd == "wait_for_selector":
                    self.page.wait_for_selector(selector, state='visible', timeout=5000)
                elif cmd == "get_text":
                    results.append(self.page.locator(selector).inner_text())
                elif cmd == "get_html":
                    results.append(self.page.locator(selector).inner_html())
                elif cmd == "screenshot":
                    path = f"screenshot_{datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
                    self.page.screenshot(path=path)
                    results.append({"screenshot_path": path})
                else:
                    results.append({"error": f"Unknown action: {cmd}"})
            except Exception as e:
                results.append({"error": str(e)})
        
        return results

    # ... [Other methods like create_main_listing_index, update_sermon, etc. remain unchanged] ...
