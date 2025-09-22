
import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from datetime import datetime

async def main():
    load_dotenv()

    login_url = os.getenv("WORDPRESS_LOGIN_URL")
    username = os.getenv("WORDPRESS_USERNAME")
    password = os.getenv("WORDPRESS_PASSWORD")

    if not all([login_url, username, password]):
        print("Error: Make sure WORDPRESS_LOGIN_URL, WORDPRESS_USERNAME, and WORDPRESS_PASSWORD are set in your .env file.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            print(f"Navigating to login page: {login_url}")
            await page.goto(login_url)

            print("Filling in login credentials...")
            await page.fill("#user_login", username)
            await page.fill("#user_pass", password)
            await page.click("#wp-submit")

            await page.wait_for_load_state("networkidle")
            
            if "wp-admin" not in page.url:
                print("Login failed. Please check your credentials.")
                await browser.close()
                return

            print("Login successful.")

            export_url = login_url.split('/wp-login.php')[0] + "/wp-admin/edit.php?post_type=wpfc_sermon&page=sm-import-export"
            print(f"Navigating to Sermon Manager export page: {export_url}")
            await page.goto(export_url)
            
            async with page.expect_download() as download_info:
                print("Starting export...")
                await page.click('#sm-export-content')
            
            download = await download_info.value
            
            date_str = datetime.now().strftime("%Y-%m-%d")
            file_name = f"stalfredschurch.WordPress.{date_str}.xml"
            file_path = os.path.join(os.getcwd(), file_name)

            await download.save_as(file_path)
            print(f"Successfully downloaded and saved export to: {file_path}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
