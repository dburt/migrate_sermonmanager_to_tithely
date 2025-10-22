from playwright.sync_api import sync_playwright, expect

class TithelyManager:
    def __init__(self, email, password, headless=True, _echo=print):
        self.email = email
        self.password = password
        self.headless = headless
        self.base_url = "https://stalfreds.tithelysetup.com"
        self.playwright = None
        self.browser = None
        self.page = None
        self._echo = _echo

    def __enter__(self):
        self._echo("Entering TithelyManager context.")
        self.start_browser()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_browser()

    def start_browser(self):
        """Starts the Playwright browser instance."""
        self.playwright = sync_playwright().start()
        self._echo("Playwright started.")
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            slow_mo=50
        )
        self._echo("Browser launched.")
        self.page = self.browser.new_page()
        self._echo("New page created.")
        self._echo("Browser started.")

    def stop_browser(self):
        """Stops the Playwright browser instance."""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        self._echo("Browser stopped.")

    def login(self):
        """Navigates to the login page and logs in with provided credentials."""
        self._echo("Navigating to login page...")
        self.page.goto(f"{self.base_url}/login")
        self.page.locator('input[name="user[email]"]').fill(self.email)
        self.page.locator('input[name="user[password]"]').fill(self.password)
        self.page.locator('button[type="submit"]').click()
        self._echo("Login submitted. Waiting for dashboard...")
        expect(self.page.locator("text=You are now logged in")).to_be_visible(timeout=15000)
        self._echo("Login successful!")

    def list_sermons(self, page_number=1, podcast_slug=None):
        """Scrapes a single page of a sermon listing."""
        if podcast_slug:
            url = f"{self.base_url}/podcasts/{podcast_slug}?page={page_number}"
            self._echo(f"Navigating to podcast listing: {url}...")
            self.page.goto(url)
            return self._scrape_podcast_listing()
        else:
            url = f"{self.base_url}/media/listing?page={page_number}"
            self._echo(f"Navigating to general media listing: {url}...")
            self.page.goto(url)
            return self._scrape_general_listing()

    def _scrape_general_listing(self):
        self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)
        sermon_rows = self.page.locator("table.table-hover.table-align-middle.table-nowrap tr")
        
        sermons = []
        for row in sermon_rows.all()[1:]:
            title_link = row.locator("td.table-item-name a").first
            href = title_link.get_attribute("href")
            slug_match = __import__('re').search(r'/media/([^/]+)', href)
            slug = slug_match.group(1) if slug_match else "Unknown Slug"

            sermon_data = {
                "slug": slug,
                "title": title_link.inner_text().strip(),
                "speaker": row.locator("td").nth(2).inner_text().strip(),
                "date": row.locator("td").first.inner_text().strip(),
                "sermon_series": row.locator("td").nth(3).get_attribute("title"),
            }
            sermons.append(sermon_data)
        return sermons

    def _scrape_podcast_listing(self):
        self.page.wait_for_selector("a.row.d-sm-flex[href^='/media/']", timeout=10000)
        sermon_links = self.page.locator("a.row.d-sm-flex[href^='/media/']")
        
        sermons = []
        for link in sermon_links.all():
            href = link.get_attribute("href")
            slug_match = __import__('re').search(r'/media/([^/]+)', href)
            slug = slug_match.group(1) if slug_match else "Unknown Slug"

            sermon_data = {
                "slug": slug,
                "title": link.locator("h2.h3").inner_text().strip(),
                "speaker": link.locator('div.h5.my-0, div.text-body.line-height-2').first.inner_text().strip(),
                "date": link.locator('div.text-muted:last-child').inner_text().strip(),
                "bible_passage": link.locator(".text-body + .text-muted").first.inner_text().strip(),
                "sermon_series": link.locator("div.text-body").first.inner_text().strip(),
            }
            sermons.append(sermon_data)
        return sermons

    def get_sermon_details(self, slug):
        """Gets additional details from a sermon detail page."""
        url = f"{self.base_url}/media/{slug}"
        self._echo(f"Navigating to {url}...")
        self.page.goto(url)
        self.page.wait_for_selector(".article.mt-3", state="attached", timeout=15000)

        details = {
            "slug": slug,
            "title": "",
            "bible_passage": "",
            "description": "",
            "audio_url": ""
        }

        passage_container_locator = self.page.locator("div.py-3:has(h2:text-is('Bible Passage'))")
        if passage_container_locator.count() > 0:
            details["bible_passage"] = passage_container_locator.evaluate(
                'element => { let passage = ""; for (const node of element.childNodes) { if (node.nodeType === Node.TEXT_NODE && node.textContent.trim() !== "") { passage = node.textContent.trim(); break; } } return passage; }'
            )

        title_locator = self.page.locator("h1").first
        if title_locator.count() > 0:
            details["title"] = title_locator.inner_text().strip()
        
        description_locator = self.page.locator(".article.mt-3")
        if description_locator.count() > 0:
            details["description"] = description_locator.locator("p").first.inner_text().strip()

        download_link = self.page.locator("a.btn.btn-link[href*='cloudfront.net']")
        if download_link.count() > 0:
            details["audio_url"] = download_link.first.get_attribute("href")
            
        return details

    def get_file_size(self, url: str) -> int:
        """Gets the file size in bytes from a URL using a HEAD request."""
        if not isinstance(url, str) or not url.startswith('http'):
            return 0
        try:
            import requests
            response = requests.head(url, timeout=10, allow_redirects=True)
            response.raise_for_status()
            file_size = response.headers.get('Content-Length')
            if file_size:
                return int(file_size)
        except requests.exceptions.RequestException as e:
            self._echo(f"Error getting file size for {url}: {e}")
        return 0


import xml.etree.ElementTree as ET

class WordpressParser:
    def __init__(self, xml_file, _echo=print):
        self.xml_file = xml_file
        self._echo = _echo
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.namespaces = {
            'wp': 'http://wordpress.org/export/1.2/',
            'content': 'http://purl.org/rss/1.0/modules/content/',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'wfw': 'http://wellformedweb.org/CommentAPI/',
            'rss20': 'http://backend.userland.com/rss20',
            'atom': 'http://www.w3.org/2005/Atom',
            'sy': 'http://purl.org/rss/1.0/modules/syndication/',
            'slash': 'http://purl.org/rss/1.0/modules/slash/',
            'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
            'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
            'wp': 'http://wordpress.org/export/1.2/'
        }

    def get_sermon_by_post_id(self, post_id):
        for item in self.root.findall('channel/item', self.namespaces):
            post_type = item.find('wp:post_type', self.namespaces)
            if post_type is not None:
                self._echo(f"Found item with post_type: {post_type.text}")
            if post_type is not None and post_type.text == 'wpfc_sermon':
                current_post_id = item.find('wp:post_id', self.namespaces)
                if current_post_id is not None:
                    self._echo(f"Found sermon with post_id: {current_post_id.text}")
                if current_post_id is not None and current_post_id.text == str(post_id):
                    return self._parse_sermon_item(item)
        return None

    def _parse_sermon_item(self, item):
        title = item.find('title', self.namespaces).text if item.find('title', self.namespaces) is not None else ""
        content = item.find('content:encoded', self.namespaces).text if item.find('content:encoded', self.namespaces) is not None else ""
        
        # Extract custom fields (meta data)
        meta = {}
        for postmeta in item.findall('wp:postmeta', self.namespaces):
            meta_key = postmeta.find('wp:meta_key', self.namespaces)
            meta_value = postmeta.find('wp:meta_value', self.namespaces)
            if meta_key is not None and meta_value is not None:
                meta[meta_key.text] = meta_value.text

        # Extract relevant sermon data
        sermon_data = {
            "post_id": item.find('wp:post_id', self.namespaces).text,
            "title": title,
            "content": content,
            "speaker": meta.get('sermon_speaker', ''),
            "series": meta.get('sermon_series', ''),
            "bible_passage": meta.get('sermon_passage', ''),
            "audio_url": meta.get('sermon_audio', ''),
            "date": item.find('wp:post_date', self.namespaces).text
        }
        return sermon_data

def compare_sermons(sermon1, sermon2):
    """Compares two sermon dictionaries and returns a list of differences."""
    differences = []
    keys = set(sermon1.keys()).union(set(sermon2.keys()))

    for key in sorted(list(keys)):
        val1 = sermon1.get(key)
        val2 = sermon2.get(key)

        if val1 != val2:
            differences.append(f"Field '{key}': Local='{val1}', Remote='{val2}'")
            
    return differences


class TithelyManager:
    # ... (rest of the class) ...

    def get_sermon_by_audio_file_size(self, audio_file_size, page_number=1):
        """Gets a sermon from Tithely by finding it by its audio file size."""
        self._echo(f"Finding sermon with audio file size {audio_file_size} on page {page_number}...")
        
        sermons_on_page = self.list_sermons(page_number=page_number)
        
        target_sermon_slug = None
        for sermon in sermons_on_page:
            details = self.get_sermon_details(sermon['slug'])
            if details.get('audio_url'):
                size = self.get_file_size(details['audio_url'])
                if size == int(audio_file_size):
                    target_sermon_slug = sermon['slug']
                    break

        if not target_sermon_slug:
            raise Exception(f"Sermon with audio file size '{audio_file_size}' not found on page {page_number}.")

        self._echo(f"Found sermon with slug: {target_sermon_slug}")
        return self.get_sermon_details(target_sermon_slug)

    def update_sermon(self, audio_file_size, sermon_data, page_number=1):
        """Updates a sermon on Tithely by finding it by its audio file size."""
        self._echo(f"Finding sermon with audio file size {audio_file_size} on page {page_number}...")
        
        sermons_on_page = self.list_sermons(page_number=page_number)
        
        target_sermon_slug = None
        for sermon in sermons_on_page:
            details = self.get_sermon_details(sermon['slug'])
            if details.get('audio_url'):
                size = self.get_file_size(details['audio_url'])
                if size == int(audio_file_size):
                    target_sermon_slug = sermon['slug']
                    break

        if not target_sermon_slug:
            raise Exception(f"Sermon with audio file size '{audio_file_size}' not found on page {page_number}.")

        self._echo(f"Found sermon with slug: {target_sermon_slug}")

        # Now we can proceed with the update as before
        self.page.goto(f"{self.base_url}/media/listing?page={page_number}")
        self.page.wait_for_selector("table.table-hover.table-align-middle.table-nowrap", timeout=10000)
        
        sermon_row = self.page.locator(f"tr:has(a[href='/media/{target_sermon_slug}'])")
        if sermon_row.count() == 0:
            raise Exception(f"Sermon with slug '{target_sermon_slug}' not found on page {page_number} of the media listing.")

        edit_link = sermon_row.locator("a.js-sermon-form-link").first

        sermon_row.hover()
        more_button = sermon_row.locator("button[data-toggle='dropdown'][title='More']")
        more_button.click(force=True)
        
        edit_link.wait_for(state='visible', timeout=5000)
        edit_link.click()

        form_locator = self.page.locator("form[id^='edit_sermon_']")
        expect(form_locator).to_be_visible(timeout=5000)
        self._echo("Form is visible. Filling details...")

        # For now, just update the title.
        if 'title' in sermon_data:
            form_locator.locator("#sermon_title").fill(sermon_data['title'])

        if 'preacher' in sermon_data:
            speaker_select = form_locator.locator("#sermon_speaker_id")
            try:
                speaker_select.select_option(label=sermon_data['preacher'], timeout=2000)
            except Exception:
                speaker_select.select_option(label="Guest Speaker")

        if 'sermon_series' in sermon_data:
            series_name = sermon_data['sermon_series']
            if series_name and str(series_name).strip():
                series_select = form_locator.locator("#sermon_series_id")
                try:
                    series_select.select_option(label=series_name, timeout=2000)
                except Exception:
                    series_select.select_option(value="new")
                    form_locator.locator("#sermon_series_title").fill(series_name)

        if 'bible_passage' in sermon_data:
            form_locator.locator('[name="sermon[passages]"]').fill(sermon_data['bible_passage'])

        if 'description' in sermon_data:
            try:
                self.page.evaluate('''
                    (newContent) => {
                        var editor = tinymce.get('sermon_topic');
                        if (editor) {
                            editor.setContent(newContent);
                        }
                    }
                ''', sermon_data['description'])
            except Exception:
                form_locator.locator("#sermon_topic").fill(sermon_data['description'])

        save_button = form_locator.locator("button[type='submit']:has-text('Save Sermon')")
        save_button.click()
        expect(form_locator).to_be_hidden(timeout=15000)
        self._echo("Sermon update submitted.")
