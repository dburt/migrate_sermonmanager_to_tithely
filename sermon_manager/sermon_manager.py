#!/usr/bin/env -S uv run --script

import os
import re
import json
import hashlib
import datetime
import click
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from utils import handle_output
import core
import db

def _fts_query(query):
    """Build a safe FTS5 MATCH expression from free text (prefix AND terms)."""
    tokens = []
    for word in str(query).split():
        clean = ''.join(ch for ch in word if ch.isalnum())
        if clean:
            tokens.append(f'"{clean}"*')
    return ' AND '.join(tokens)

@click.group()
def cli():
    """A CLI for managing sermons on Tithely."""
    pass

@cli.command()
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def login(headless):
    """Login to Tithely and save the session state."""
    click.echo("Starting Tithely login...")
    
    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")
    
    if not email or not password:
        click.echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.")
        return

    try:
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless) as manager:
            manager.login()
        click.echo("Login successful!")
    except Exception as e:
        click.echo(f"An error occurred during login: {e}")

@cli.command("list-remote")
@click.option("--page", default=1, help="The page number to fetch.")
@click.option("--output", default=None, help="The output file to save the results to (JSON).")
@click.option("--podcast-slug", default=None, help="The slug of the podcast to list.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def list_remote(page, output, podcast_slug, headless):
    """List sermons from the main Tithely media listing."""
    click.echo(f"Fetching page {page} of remote sermons...")
    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")

    if not email or not password:
        click.echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.")
        return

    try:
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless) as manager:
            manager.login()
            sermons = manager.list_sermons(page_number=page, podcast_slug=podcast_slug)
        
        handle_output(sermons, output)

    except Exception as e:
        click.echo(f"An error occurred: {e}")

@cli.command("list-local")
@click.option("--limit", default=10, help="The number of sermons to list.")
@click.option("--audio-file-size", type=int, default=None, help="The audio file size to search for.")
@click.option("--output", default=None, help="The output file to save the results to (JSON), or 'stdout'.")
def list_local(limit, audio_file_size, output):
    """List sermons from the local sermons.csv file."""
    click.echo("Listing local sermons...")
    try:
        import pandas as pd
        from core import TithelyManager
        from tqdm import tqdm
        import os

        cached_file = "sermons_with_sizes.csv"

        if os.path.exists(cached_file):
            df = pd.read_csv(cached_file)
            click.echo(f"Loaded cached sermon data from {cached_file}.")
        else:
            df = pd.read_csv("sermons.csv")
            click.echo("Calculating audio file sizes... This may take a while.")
            # Create a dummy manager to access get_file_size
            from core import TithelyManager
            with TithelyManager("", "", headless=True, _echo=click.echo) as manager:
                df['audio_file_size'] = [manager.get_file_size(url) for url in tqdm(df['audio_url'], desc="Fetching file sizes")]
            click.echo("Audio file sizes calculated.")
            df.to_csv(cached_file, index=False)
            click.echo(f"Cached sermon data to {cached_file}.")

        if audio_file_size:
            sermon = df[df['audio_file_size'] == audio_file_size].to_dict(orient="records")
            if sermon:
                handle_output(sermon[0], output)
            else:
                click.echo(f"Sermon with audio file size {audio_file_size} not found locally.")
        else:
            sermons = df.head(limit).to_dict(orient="records")
            handle_output(sermons, output)

    except FileNotFoundError:
        click.echo("Error: sermons.csv not found.")

@cli.command("search")
@click.argument("query")
@click.option("--limit", default=20, type=int, help="Max number of results to return (default: 20).")
@click.option("--output", default=None, help="The output file to save the results to (JSON), or 'stdout'.")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
def search_cmd(query, limit, output, db_path):
    """Full-text search local sermon data, including transcript contents.

    Searches title, speaker, series, bible passage, topics, description and
    transcript text. Prints ranked matches as JSON to stdout (or --output).
    """
    if db_path is None:
        db_path = db.DEFAULT_DB_PATH
    conn = db.connect(db_path)
    db.init_db(conn)
    fts = _fts_query(query)
    if not fts:
        click.echo("Error: query must contain at least one alphanumeric word.", err=True)
        return
    try:
        rows = db.search_fts(conn, fts, limit=limit)
    except Exception as e:
        click.echo(f"Error: search failed - {e}.", err=True)
        return
    results = [
        {
            "slug": m.get("slug"),
            "sermon_key": db._sermon_key(m),
            "title": m.get("title"),
            "speaker": m.get("speaker") or m.get("preacher") or "",
            "date": m.get("date") or "",
            "series": m.get("sermon_series") or "",
            "bible_passage": m.get("bible_passage") or "",
        }
        for m in rows
    ]
    handle_output({"query": query, "count": len(results), "results": results}, output or "stdout")

@cli.command("get-remote")
@click.argument("slug")
@click.option("--output", default=None, help="The output file to save the results to (JSON).")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def get_remote(slug, output, headless):
    _echo = click.echo if output != "stdout" else lambda msg, **kwargs: click.echo(msg, **kwargs)
    _echo(f"Fetching details for sermon: {slug}...")
    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")

    if not email or not password:
        _echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.", err=True)
        return

    try:
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=_echo) as manager:
            manager.login()
            sermon = manager.get_sermon_details(slug)
        
        handle_output(sermon, output)

    except Exception as e:
        _echo(f"An error occurred: {e}", err=True)

@cli.command("update")
@click.argument("audio_file_size")
@click.option("--from-file", "from_file", default=None, help="The JSON file to load sermon data from.")
@click.option("--from-stdin", "from_stdin", is_flag=True, help="Read sermon data from stdin.")
@click.option("--page", default=1, help="The page number the sermon is on.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def update(audio_file_size, from_file, from_stdin, page, headless):
    """Update a sermon on Tithely."""
    click.echo(f"Updating sermon with audio file size: {audio_file_size}...")
    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")

    if not email or not password:
        click.echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.")
        return

    if not from_file and not from_stdin:
        click.echo("Error: either --from-file or --from-stdin must be specified.")
        return
    if from_file and from_stdin:
        click.echo("Error: --from-file and --from-stdin cannot be used together.")
        return

    try:
        import json
        sermon_data = None
        if from_stdin:
            sermon_data = json.load(click.get_text_stream('stdin'))
        else:
            with open(from_file, 'r') as f:
                sermon_data = json.load(f)

        from core import TithelyManager
        with TithelyManager(email, password, headless=headless) as manager:
            manager.login()
            manager.update_sermon(audio_file_size, sermon_data, page_number=page)
        
    except Exception as e:
        click.echo(f"An error occurred: {e}")

@cli.command("update-title")
@click.argument("audio_file_size")
@click.argument("new_title")
@click.option("--page", default=1, help="The page number the sermon is on.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def update_title(audio_file_size, new_title, page, headless):
    """Update the title of a sermon on Tithely."""
    _echo = click.echo
    _echo(f"Updating title for sermon with audio file size: {audio_file_size} to '{new_title}'...")

    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")

    if not email or not password:
        _echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.", err=True)
        return

    try:
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=_echo) as manager:
            manager.login()
            sermon_data = manager.get_sermon_by_audio_file_size(audio_file_size, page_number=page)
            
            if sermon_data:
                sermon_data['title'] = new_title
                manager.update_sermon(audio_file_size, sermon_data, page_number=page)
                _echo("Sermon title updated successfully!")
            else:
                _echo(f"Sermon with audio file size {audio_file_size} not found.", err=True)

    except Exception as e:
        _echo(f"An error occurred: {e}.", err=True)

def _single_field_update(audio_file_size, field, value, page, headless, label):
    """Shared implementation for the single-field update commands."""
    _echo = click.echo
    _echo(f"Updating {label} for sermon with audio file size: {audio_file_size} to '{value}'...")

    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")

    if not email or not password:
        _echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.", err=True)
        return 1

    try:
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=_echo) as manager:
            manager.login()
            sermon_data = manager.get_sermon_by_audio_file_size(audio_file_size, page_number=page)

            if sermon_data:
                sermon_data[field] = value
                manager.update_sermon(audio_file_size, sermon_data, page_number=page)
                _echo(f"Sermon {label} updated successfully!")
                return 0
            else:
                _echo(f"Sermon with audio file size {audio_file_size} not found.", err=True)
                return 1

    except Exception as e:
        _echo(f"An error occurred: {e}.", err=True)
        return 1

@cli.command("update-speaker")
@click.argument("audio_file_size")
@click.argument("new_speaker")
@click.option("--page", default=1, help="The page number the sermon is on.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def update_speaker(audio_file_size, new_speaker, page, headless):
    """Update the speaker of a sermon on Tithely."""
    _single_field_update(audio_file_size, 'preacher', new_speaker, page, headless, "speaker")

@cli.command("update-series")
@click.argument("audio_file_size")
@click.argument("new_series")
@click.option("--page", default=1, help="The page number the sermon is on.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def update_series(audio_file_size, new_series, page, headless):
    """Update the series of a sermon on Tithely."""
    _single_field_update(audio_file_size, 'sermon_series', new_series, page, headless, "series")

@cli.command("update-bible-passage")
@click.argument("audio_file_size")
@click.argument("new_bible_passage")
@click.option("--page", default=1, help="The page number the sermon is on.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def update_bible_passage(audio_file_size, new_bible_passage, page, headless):
    """Update the bible passage of a sermon on Tithely."""
    _single_field_update(audio_file_size, 'bible_passage', new_bible_passage, page, headless, "bible passage")

@cli.command("update-description")
@click.argument("audio_file_size")
@click.argument("new_description")
@click.option("--page", default=1, help="The page number the sermon is on.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def update_description(audio_file_size, new_description, page, headless):
    """Update the description of a sermon on Tithely."""
    _single_field_update(audio_file_size, 'description', new_description, page, headless, "description")

@cli.command("compare")
@click.option("--local-file", "local_file", default=None, help="Path to the local sermon data JSON file.")
@click.option("--remote-file", "remote_file", default=None, help="Path to the remote sermon data JSON file.")
@click.option("--local-stdin", "local_stdin", is_flag=True, help="Read local sermon data from stdin.")
@click.option("--remote-stdin", "remote_stdin", is_flag=True, help="Read remote sermon data from stdin.")
def compare(local_file, remote_file, local_stdin, remote_stdin):
    """Compare two sermon data objects (local and remote)."""
    _echo = click.echo
    _echo("Comparing sermon data...")

    if (not local_file and not local_stdin) or (local_file and local_stdin):
        _echo("Error: exactly one of --local-file or --local-stdin must be specified.", err=True)
        return
    if (not remote_file and not remote_stdin) or (remote_file and remote_stdin):
        _echo("Error: exactly one of --remote-file or --remote-stdin must be specified.", err=True)
        return

    try:
        import json
        local_sermon = None
        remote_sermon = None

        if local_stdin:
            local_sermon = json.load(click.get_text_stream('stdin'))
        else:
            with open(local_file, 'r') as f:
                local_sermon = json.load(f)

        if remote_stdin:
            # For remote_stdin, we need to read from a different stream or ensure it's not conflicting
            # For now, let's assume remote_stdin will be handled by piping from a separate command
            # This part needs careful consideration for how to handle two stdin inputs
            _echo("Error: --remote-stdin is not yet fully supported for direct piping of two inputs. Please use --remote-file.", err=True)
            return
        else:
            with open(remote_file, 'r') as f:
                remote_sermon = json.load(f)

        # Perform comparison (this logic will be in a helper function)
        from core import compare_sermons
        differences = compare_sermons(local_sermon, remote_sermon)

        if differences:
            _echo("Differences found:")
            for diff in differences:
                _echo(f"- {diff}")
        else:
            _echo("No differences found.")

    except FileNotFoundError as e:
        _echo(f"Error: File not found - {e}.", err=True)
    except json.JSONDecodeError as e:
        _echo(f"Error: Invalid JSON format - {e}.", err=True)
    except Exception as e:
        _echo(f"An unexpected error occurred: {e}.", err=True)

@cli.command("get-wordpress-sermon")
@click.argument("xml_file")
@click.argument("post_id")
@click.option("--output", default=None, help="The output file to save the results to (JSON), or 'stdout'.")
def get_wordpress_sermon(xml_file, post_id, output):
    """Get a single sermon from a WordPress XML export by post_id."""
    _echo = click.echo if output != "stdout" else lambda msg: click.echo(msg, err=True)
    _echo(f"Fetching sermon with post_id {post_id} from {xml_file}...")

    try:
        from core import WordpressParser
        parser = WordpressParser(xml_file, _echo=_echo)
        sermon = parser.get_sermon_by_post_id(post_id)
        
        if sermon:
            handle_output(sermon, output)
        else:
            _echo(f"Sermon with post_id {post_id} not found in {xml_file}.")

    except FileNotFoundError:
        _echo(f"Error: XML file not found at {xml_file}.")
    except Exception as e:
        _echo(f"An error occurred: {e}.")

@cli.command("get-file-size")
@click.argument("url")
def get_file_size(url):
    """Get the file size of a URL."""
    from core import TithelyManager
    # We don't need to login for this, so we can pass dummy credentials
    with TithelyManager("", "") as manager:
        size = manager.get_file_size(url)
        click.echo(size)

@cli.command("search-speaker")
@click.argument("speaker_name")
@click.option("--max-pages", default=50, help="The maximum number of pages to search.")
@click.option("--output", default=None, help="The output file to save the results to (JSON), or 'stdout'.")
@click.option('--headless', is_flag=True, help='Run the browser in headless mode.')
def search_speaker(speaker_name, max_pages, output, headless):
    """Search for sermons by a specific speaker."""
    _echo = click.echo if output != "stdout" else lambda msg, **kwargs: click.echo(msg, **kwargs)
    _echo(f"Searching for sermons by '{speaker_name}' across {max_pages} pages...")

    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")

    if not email or not password:
        _echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.", err=True)
        return

    try:
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=_echo) as manager:
            manager.login()
            found_sermons = manager.search_speaker(speaker_name, max_pages=max_pages)
        
        handle_output(found_sermons, output)

    except Exception as e:
        _echo(f"An error occurred: {e}", err=True)

# --- Phase 3: Scrape & Index ---

def _get_credentials():
    """Helper to get Tithely credentials from env."""
    email = os.getenv("TITHELY_EMAIL")
    password = os.getenv("TITHELY_PASSWORD")
    if not email or not password:
        click.echo("Error: TITHELY_EMAIL and TITHELY_PASSWORD must be set in your .env file.", err=True)
        return None, None
    return email, password


@cli.command("scrape-index")
@click.option("--output", default="tithely_index.json", help="Output file path.")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
@click.option("--with-details", is_flag=True, help="Visit each detail page for full metadata.")
@click.option("--with-sizes", is_flag=True, help="Do HEAD requests for audio_file_size.")
@click.option("--podcast-slug", default=None, help="Scrape a specific podcast slug instead of general listing.")
def scrape_index(output, headless, with_details, with_sizes, podcast_slug):
    """Scrape all Tithely listing pages to build a complete index."""
    email, password = _get_credentials()
    if not email:
        return

    try:
        import json
        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
            manager.login()
            sermons = manager.scrape_all_listings(
                podcast_slug=podcast_slug,
                with_details=with_details,
                with_sizes=with_sizes,
            )

        with open(output, 'w') as f:
            json.dump(sermons, f, indent=2)
        click.echo(f"Saved {len(sermons)} sermons to {output}")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


@cli.command("refresh-index")
@click.option("--existing-index", default="tithely_index.json", help="Existing index to merge into.")
@click.option("--pages", default=None, help="Page range to scrape, e.g. '1-5' or '3'.")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
def refresh_index(existing_index, pages, headless):
    """Incrementally scrape specific pages and merge into existing index."""
    email, password = _get_credentials()
    if not email:
        return

    try:
        import json
        from core import TithelyManager

        # Load existing index
        existing = []
        if os.path.exists(existing_index):
            with open(existing_index, 'r') as f:
                existing = json.load(f)
            click.echo(f"Loaded {len(existing)} existing sermons from {existing_index}")

        # Parse page range
        start_page, end_page = 1, 1
        if pages:
            if '-' in pages:
                start_page, end_page = map(int, pages.split('-'))
            else:
                start_page = end_page = int(pages)

        with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
            manager.login()
            new_sermons = []
            for page_num in range(start_page, end_page + 1):
                sermons = manager.list_sermons(page_number=page_num)
                new_sermons.extend(sermons)
                click.echo(f"Page {page_num}: {len(sermons)} sermons")

        # Merge: update existing by slug, add new
        existing_by_slug = {s['slug']: s for s in existing}
        for s in new_sermons:
            existing_by_slug[s['slug']] = s
        merged = list(existing_by_slug.values())

        with open(existing_index, 'w') as f:
            json.dump(merged, f, indent=2)
        click.echo(f"Merged index: {len(merged)} sermons saved to {existing_index}")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


# --- Phase 3b: Mirror Sync ---

@cli.command("sync")
@click.option("--full", is_flag=True, help="Full re-scrape of all pages + details.")
@click.option("--limit-pages", default=100, help="Max pages to scan in incremental mode.")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
def sync_cmd(full, limit_pages, db_path, headless):
    """Sync Tithely sermons into the local SQLite mirror.

    Incremental mode (default) scans listing pages until a page with no new
    slugs is found, fetching details only for newly seen sermons. --full
    re-scrapes everything with details and audio sizes.
    """
    email, password = _get_credentials()
    if not email:
        return

    if db_path is None:
        db_path = db.DEFAULT_DB_PATH
    conn = db.connect(db_path)
    db.init_db(conn)

    from core import TithelyManager
    with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
        manager.login()

        if full:
            click.echo("Full sync: scraping all listings with details + sizes...")
            sermons = manager.scrape_all_listings(with_details=True, with_sizes=True)
            res = db.upsert_tithely(conn, sermons)
            click.echo(f"Full sync result: {res['new']} new, {res['updated']} updated.")
        else:
            res = {'new': 0, 'updated': 0, 'unchanged': 0}
            existing = db.get_tithely_slugs(conn)
            for page in range(1, limit_pages + 1):
                try:
                    sermons = manager.list_sermons(page_number=page)
                except Exception as e:
                    click.echo(f"Error on page {page}: {e}", err=True)
                    break
                if not sermons:
                    click.echo(f"No sermons on page {page}. Scan complete.")
                    break

                new_on_page = [s for s in sermons if s.get('slug') not in existing]
                click.echo(f"Page {page}: {len(sermons)} sermons, {len(new_on_page)} new")

                # Fetch details + sizes only for newly seen sermons
                for i, s in enumerate(new_on_page, 1):
                    slug = s.get('slug')
                    click.echo(f"  [{i}/{len(new_on_page)}] fetching details: {slug}")
                    try:
                        details = manager.get_sermon_details(slug)
                        s.update(details)
                        if s.get('audio_url'):
                            s['audio_file_size'] = manager.get_file_size(s['audio_url'])
                    except Exception as e:
                        click.echo(f"  ERROR {slug}: {e}", err=True)

                page_res = db.upsert_tithely(conn, new_on_page)
                res['new'] += page_res['new']
                res['updated'] += page_res['updated']
                res['unchanged'] += page_res['unchanged']
                existing |= {s.get('slug') for s in sermons}

                if not new_on_page:
                    click.echo(f"No new sermons on page {page}. Stopping scan.")
                    break

    n = db.refresh_fts(conn)
    click.echo(
        f"Sync complete: {res['new']} new, {res['updated']} updated, "
        f"{res['unchanged']} unchanged. FTS index refreshed ({n} rows)."
    )


# --- Phase 3c: Export ---

def _site_json(sermons):
    """Convert merged DB records into the site/feed JSON shape."""
    out = []
    for m in sermons:
        slug = m.get('slug') or ''
        wp_link = m.get('permalink') or ''
        permalink = wp_link if wp_link else f"https://stalfreds.org/media/{slug}"
        out.append({
            'post_id': m.get('wordpress_post_id') or '',
            'title': m.get('title') or '',
            'post_date_gmt': m.get('post_date_gmt') or '',
            'perm': permalink,
            'permalink': permalink,
            'status': 'publish',
            'guid': permalink,
            'content_text': m.get('content_text') or '',
            'description': m.get('description') or '',
            'preacher': m.get('speaker') or m.get('preacher') or '',
            'sermon_series': m.get('sermon_series') or '',
            'service_type': m.get('service_type') or '',
            'bible_book': '',
            'sermon_topics': m.get('sermon_topics') or m.get('topics') or '',
            'audio_url': m.get('audio_url') or '',
            'audio_file_size': m.get('audio_file_size') or 0,
            'bible_passage': m.get('bible_passage') or '',
            'view_count': m.get('view_count') or 0,
            'melbourne_time': m.get('melbourne_time') or '',
            'slug': slug,
            'has_transcript': bool((m.get('transcript') or '').strip()),
        })
    # Newest first; rows with no date sink to the bottom
    out.sort(key=lambda s: s['post_date_gmt'], reverse=True)
    return out


@cli.command("export")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
@click.option("--out-dir", "out_dir", default="sermon-archive", help="Directory for sermons.json, podcast_feed.xml and transcripts/.")
def export_cmd(db_path, out_dir):
    """Export the mirror DB to static site assets (sermons.json + podcast_feed.xml).

    Transcripts are written as per-sermon files under <out-dir>/transcripts/<slug>.json
    and fetched on demand by the site, rather than embedded in sermons.json.
    """
    if db_path is None:
        db_path = db.DEFAULT_DB_PATH

    conn = db.connect(db_path)
    db.init_db(conn)
    sermons = db.get_sermons_with_transcripts(conn)

    os.makedirs(out_dir, exist_ok=True)
    written, transcripts_thumb = _write_transcript_files(sermons, out_dir)

    site = _site_json(sermons)
    json_path = os.path.join(out_dir, 'sermons.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(site, f, ensure_ascii=False)
    click.echo(f"Exported {len(site)} sermons to {json_path}")

    manifest_path = os.path.join(out_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump({
            'sermons': _file_thumbprint(json_path),
            'transcripts': transcripts_thumb,
            'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }, f, ensure_ascii=False)
    click.echo(f"Exported cache manifest to {manifest_path}")

    rss_path = os.path.join(out_dir, 'podcast_feed.xml')
    _write_rss_feed(site, rss_path)
    click.echo(f"Exported RSS feed to {rss_path}")
    click.echo(f"Exported {written} transcripts to {os.path.join(out_dir, 'transcripts')}")

    search_path = os.path.join(out_dir, 'search.db')
    n = db.build_search_db(conn, search_path)
    click.echo(f"Exported FTS search DB ({n} rows) to {search_path}")


def _reflow_transcript(text):
    """Join hard-wrapped lines into flowing prose.

    Whisper output is stored as one segment per line; rendered with
    ``white-space: pre-wrap`` those become mid-sentence breaks. Collapse every
    run of whitespace within a paragraph to a single space, keeping only genuine
    blank-line paragraph breaks.
    """
    text = (text or '').replace('\r\n', '\n').replace('\r', '\n')
    paragraphs = re.split(r'\n\s*\n', text)
    return '\n\n'.join(' '.join(p.split()) for p in paragraphs if p.strip())


def _file_thumbprint(path, chunk_size=1 << 20):
    """Return a short content hash used for cache-busting query strings."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()[:16]


def _write_transcript_files(sermons, out_dir):
    """Write one transcripts/<slug>.json per sermon that has a transcript.

    Returns ``(written, thumbprint)`` where thumbprint is a content hash over
    all written transcripts, used to cache-bust on-demand transcript fetches.
    """
    transcripts_dir = os.path.join(out_dir, 'transcripts')
    os.makedirs(transcripts_dir, exist_ok=True)
    current = set()
    written = 0
    thumbprint = hashlib.sha256()
    for m in sermons:
        text = _reflow_transcript(m.get('transcript') or '')
        slug = m.get('slug') or ''
        if not text or not slug:
            continue
        current.add(slug)
        payload = {
            'slug': slug,
            'title': m.get('title') or '',
            'transcript': text,
            'word_count': len(re.findall(r"\b\w+\b", text)),
        }
        with open(os.path.join(transcripts_dir, f"{slug}.json"), 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False)
        thumbprint.update(slug.encode('utf-8'))
        thumbprint.update(b'\0')
        thumbprint.update(text.encode('utf-8'))
        written += 1
    for stale in os.listdir(transcripts_dir):
        if stale.endswith('.json') and stale[:-5] not in current:
            os.remove(os.path.join(transcripts_dir, stale))
    return written, thumbprint.hexdigest()[:16]


def _write_rss_feed(sermons, rss_path):
    """Generate a podcast-compliant RSS feed from exported sermon dicts."""
    import html as html_mod
    from datetime import datetime, timezone

    current_year = datetime.now().year
    build_date = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S %z')

    rss_feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:sy="http://purl.org/rss/1.0/modules/syndication/" xmlns:slash="http://purl.org/rss/1.0/modules/slash/" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
<channel>
    <title>St Alfred's Anglican Church Sermons</title>
    <link>https://stalfreds.org/sermons/</link>
    <description>Sermons from St Alfred's Anglican Church, Blackburn North.</description>
    <language>en-au</language>
    <copyright>Copyright {current_year} St Alfred's Anglican Church</copyright>
    <lastBuildDate>{build_date}</lastBuildDate>
    <itunes:author>St Alfred's Anglican Church</itunes:author>
    <itunes:subtitle>Weekly sermons from St Alfred's Anglican Church</itunes:subtitle>
    <itunes:summary>Sermons from St Alfred's Anglican Church, Blackburn North.</itunes:summary>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>episodic</itunes:type>
    <itunes:owner>
        <itunes:name>St Alfred's Anglican Church</itunes:name>
        <itunes:email>info@stalfreds.org</itunes:email>
    </itunes:owner>
    <itunes:category text="Religion &amp; Spirituality"/>
</channel>
'''

    items = []
    for s in sermons:
        if s.get('status') != 'publish':
            continue
        title = html_mod.escape(s.get('title') or 'No Title')
        permalink = s.get('permalink') or '#'
        audio_url = s.get('audio_url') or ''
        preacher = html_mod.escape(s.get('preacher') or 'N/A')
        sermon_series = html_mod.escape(s.get('sermon_series') or 'N/A')
        bible_passage = html_mod.escape(s.get('bible_passage') or 'N/A')
        content_text = html_mod.escape(s.get('content_text') or '')

        pub_date = ""
        pdt = s.get('post_date_gmt')
        if pdt:
            try:
                dt_object = datetime.strptime(pdt, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
                pub_date = dt_object.strftime('%a, %d %b %Y %H:%M:%S %z')
            except ValueError:
                pass

        description = (
            f"In this sermon, {preacher} speaks on the theme of {title} as part of the "
            f"series {sermon_series}. The Bible reading is {bible_passage}. {content_text}".strip()
        )

        enclosure = ""
        if audio_url:
            audio_type = "audio/x-m4a" if '.m4a' in audio_url.lower() else "audio/mpeg"
            enclosure = f'<enclosure url="{html_mod.escape(audio_url)}" type="{audio_type}" length="{s.get("audio_file_size") or 0}" />'

        items.append(f'''    <item>
        <title>{title}</title>
        <link>{permalink}</link>
        <pubDate>{pub_date}</pubDate>
        <guid>{permalink}</guid>
        {enclosure}
        <description><![CDATA[{description}]]></description>
        <itunes:author>{preacher}</itunes:author>
        <itunes:subtitle>{sermon_series} | {preacher} | {bible_passage}</itunes:subtitle>
        <itunes:summary><![CDATA[{description}]]></itunes:summary>
        <itunes:explicit>false</itunes:explicit>
    </item>''')

    rss_feed += "\n".join(items)
    rss_feed += "\n</channel>\n</rss>\n"

    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_feed)


# --- Phase 4: Gap Analysis ---

@cli.command("gap-report")
@click.option("--local-csv", default="sermons_with_sizes.csv", help="Path to local WordPress CSV.")
@click.option("--remote-index", default="tithely_index.json", help="Path to Tithely index JSON.")
@click.option("--output", default="gap_report.json", help="Output file path.")
def gap_report(local_csv, remote_index, output):
    """Generate a gap analysis report comparing WordPress CSV to Tithely index."""
    import json
    from gap_analysis import run_gap_analysis, format_summary

    report = run_gap_analysis(local_csv, remote_index)

    with open(output, 'w') as f:
        json.dump(report, f, indent=2)
    click.echo(f"Gap report saved to {output}")
    click.echo(format_summary(report))


@cli.command("gap-summary")
@click.option("--local-csv", default="sermons_with_sizes.csv", help="Path to local WordPress CSV.")
@click.option("--remote-index", default="tithely_index.json", help="Path to Tithely index JSON.")
def gap_summary(local_csv, remote_index):
    """Print a human-readable gap analysis summary."""
    from gap_analysis import run_gap_analysis, format_summary
    report = run_gap_analysis(local_csv, remote_index)
    click.echo(format_summary(report))


@cli.command("prepare-updates")
@click.option("--gap-report", "gap_report_path", default="gap_report.json", help="Path to gap report JSON.")
@click.option("--fields", default=None, help="Comma-separated fields to include (e.g. 'title,preacher').")
@click.option("--output", default="pending_updates.json", help="Output file path.")
def prepare_updates_cmd(gap_report_path, fields, output):
    """Generate update payloads from the gap report's matched_with_diffs section."""
    import json
    from gap_analysis import prepare_updates

    with open(gap_report_path, 'r') as f:
        report = json.load(f)

    field_list = [f.strip() for f in fields.split(',')] if fields else None
    updates = prepare_updates(report, fields=field_list)

    with open(output, 'w') as f:
        json.dump(updates, f, indent=2)
    click.echo(f"Prepared {len(updates)} update payloads → {output}")


@cli.command("prepare-creates")
@click.option("--gap-report", "gap_report_path", default="gap_report.json", help="Path to gap report JSON.")
@click.option("--output", default="pending_creates.json", help="Output file path.")
def prepare_creates_cmd(gap_report_path, output):
    """Generate create payloads from the gap report's local_only section."""
    import json
    from gap_analysis import prepare_creates

    with open(gap_report_path, 'r') as f:
        report = json.load(f)

    creates = prepare_creates(report)

    with open(output, 'w') as f:
        json.dump(creates, f, indent=2)
    click.echo(f"Prepared {len(creates)} create payloads → {output}")


# --- Phase 5: Update & Create ---

@cli.command("update-by-slug")
@click.argument("slug")
@click.option("--from-file", "from_file", default=None, help="JSON file with sermon data.")
@click.option("--from-stdin", "from_stdin", is_flag=True, help="Read sermon data from stdin.")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
def update_by_slug(slug, from_file, from_stdin, headless):
    """Update a sermon on Tithely by its slug (direct navigation, no page scanning)."""
    email, password = _get_credentials()
    if not email:
        return

    if not from_file and not from_stdin:
        click.echo("Error: either --from-file or --from-stdin must be specified.", err=True)
        return

    try:
        import json
        if from_stdin:
            sermon_data = json.load(click.get_text_stream('stdin'))
        else:
            with open(from_file, 'r') as f:
                sermon_data = json.load(f)

        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
            manager.login()
            manager.update_sermon_by_slug(slug, sermon_data)
        click.echo("Update complete.")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


@cli.command("create")
@click.option("--from-file", "from_file", default=None, help="JSON file with sermon data.")
@click.option("--from-stdin", "from_stdin", is_flag=True, help="Read sermon data from stdin.")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
def create_sermon(from_file, from_stdin, headless):
    """Create a new sermon on Tithely."""
    email, password = _get_credentials()
    if not email:
        return

    if not from_file and not from_stdin:
        click.echo("Error: either --from-file or --from-stdin must be specified.", err=True)
        return

    try:
        import json
        if from_stdin:
            sermon_data = json.load(click.get_text_stream('stdin'))
        else:
            with open(from_file, 'r') as f:
                sermon_data = json.load(f)

        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
            manager.login()
            manager.create_sermon(sermon_data)
        click.echo("Create complete.")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


@cli.command("batch-update")
@click.option("--from-file", "from_file", required=True, help="JSON file with list of update payloads.")
@click.option("--dry-run", is_flag=True, help="Preview without making changes.")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
@click.option("--resume-from", type=int, default=0, help="Resume from this index (0-based).")
def batch_update(from_file, dry_run, headless, resume_from):
    """Batch update sermons from a JSON file of update payloads."""
    email, password = _get_credentials()
    if not email:
        return

    try:
        import json
        with open(from_file, 'r') as f:
            updates = json.load(f)

        # Convert prepare-updates format to batch_operate format
        operations = []
        for u in updates:
            operations.append({
                'type': u.get('type', 'update'),
                'slug': u['slug'],
                'page_number': u.get('page_number'),
                'data': u.get('updates', u.get('data', {})),
            })

        click.echo(f"Loaded {len(operations)} update operations. Resume from: {resume_from}")

        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
            manager.login()
            results = manager.batch_operate(operations, dry_run=dry_run, resume_from=resume_from)

        succeeded = sum(1 for r in results if r['success'])
        failed = sum(1 for r in results if not r['success'])
        click.echo(f"Batch update complete: {succeeded} succeeded, {failed} failed.")

        # Save results log
        results_file = from_file.replace('.json', '_results.json')
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        click.echo(f"Results saved to {results_file}")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


@cli.command("batch-create")
@click.option("--from-file", "from_file", required=True, help="JSON file with list of create payloads.")
@click.option("--dry-run", is_flag=True, help="Preview without making changes.")
@click.option("--headless", is_flag=True, help="Run browser in headless mode.")
@click.option("--resume-from", type=int, default=0, help="Resume from this index (0-based).")
def batch_create(from_file, dry_run, headless, resume_from):
    """Batch create sermons from a JSON file of create payloads."""
    email, password = _get_credentials()
    if not email:
        return

    try:
        import json
        with open(from_file, 'r') as f:
            creates = json.load(f)

        operations = [{'type': 'create', 'slug': '', 'data': c} for c in creates]
        click.echo(f"Loaded {len(operations)} create operations. Resume from: {resume_from}")

        from core import TithelyManager
        with TithelyManager(email, password, headless=headless, _echo=click.echo) as manager:
            manager.login()
            results = manager.batch_operate(operations, dry_run=dry_run, resume_from=resume_from)

        succeeded = sum(1 for r in results if r['success'])
        failed = sum(1 for r in results if not r['success'])
        click.echo(f"Batch create complete: {succeeded} succeeded, {failed} failed.")

        results_file = from_file.replace('.json', '_results.json')
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        click.echo(f"Results saved to {results_file}")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


# --- Phase 6: Audio Mirror ---

@cli.command("download-audio")
@click.argument("url")
@click.option("--output-dir", default="audio_mirror", help="Directory to save audio files.")
def download_audio_cmd(url, output_dir):
    """Download a single audio file by URL."""
    from audio_mirror import download_audio
    result = download_audio(url, output_dir, _echo=click.echo)
    if result['success']:
        click.echo(f"Saved to: {result['path']} ({result['size']} bytes)")
    else:
        click.echo(f"Download failed: {result.get('error', 'unknown')}", err=True)


@cli.command("mirror-audio")
@click.option("--from-index", default="tithely_index.json", help="JSON index with audio_url entries.")
@click.option("--output-dir", default="audio_mirror", help="Directory to save audio files.")
@click.option("--dry-run", is_flag=True, help="Show what would be downloaded without downloading.")
@click.option("--resume/--no-resume", default=True, help="Resume interrupted downloads.")
def mirror_audio_cmd(from_index, output_dir, dry_run, resume):
    """Batch download all audio files from an index."""
    from audio_mirror import mirror_audio
    mirror_audio(from_index, output_dir, dry_run=dry_run, resume=resume, _echo=click.echo)


@cli.command("mirror-audio-db")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
@click.option("--rclone-remote", default="hyperion:/D:/stalfreds_audio", help="rclone remote directory to stream audio into.")
@click.option("--dry-run", is_flag=True, help="Show what would be streamed without transferring.")
def mirror_audio_db_cmd(db_path, rclone_remote, dry_run):
    """Stream pending sermon audio into an rclone remote (no local disk usage)."""
    if db_path is None:
        db_path = db.DEFAULT_DB_PATH

    conn = db.connect(db_path)
    db.init_db(conn)

    from audio_mirror import mirror_audio_db
    mirror_audio_db(conn, rclone_remote=rclone_remote, dry_run=dry_run, _echo=click.echo)


@cli.command("transcribe")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
@click.option("--model", default="medium", help="faster-whisper model name (default: medium).")
@click.option("--limit", type=int, default=None, help="Transcribe at most N pending sermons.")
@click.option("--title", "title_filter", default=None, help="Transcribe only the pending sermon with this exact title.")
def transcribe_cmd(db_path, model, limit, title_filter):
    """Transcribe sermons lacking a transcript and store them in the DB."""
    if db_path is None:
        db_path = db.DEFAULT_DB_PATH

    conn = db.connect(db_path)
    db.init_db(conn)

    from transcriber import transcribe_missing
    transcribe_missing(conn, model_name=model, limit=limit, title_filter=title_filter, _echo=click.echo)


@cli.command("transcribe-remote")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
@click.option("--model", default="medium", help="faster-whisper model name (default: medium).")
@click.option("--limit", type=int, default=None, help="Queue at most N pending sermons.")
@click.option("--batch-size", "batch_size", type=int, default=10, help="Sermons per worker invocation (default: 10).")
def transcribe_remote_cmd(db_path, model, limit, batch_size):
    """Transcribe sermons on the Hyperion GPU via ssh + rclone and import results."""
    if db_path is None:
        db_path = db.DEFAULT_DB_PATH

    conn = db.connect(db_path)
    db.init_db(conn)

    from remote_transcribe import run_remote_transcribe
    run_remote_transcribe(conn, limit=limit, batch_size=batch_size, model=model, echo=click.echo)


@cli.command("status")
@click.option("--db", "db_path", default=None, help=f"Path to the SQLite database (default: {db.DEFAULT_DB_PATH}).")
@click.option("--watch", "watch", type=int, default=0, help="Poll every N seconds (e.g. 60).")
@click.option("--json", "as_json", is_flag=True, help="Emit a JSON snapshot to stdout.")
def status_cmd(db_path, watch, as_json):
    """Show transcription progress and estimated completion time."""
    import time as _time
    import json as _json
    from monitor import status_report, _save_baseline, _load_baseline, _drain_pid, \
        _process_start, _remote_done_count

    if db_path is None:
        db_path = db.DEFAULT_DB_PATH

    _echo = None if as_json else click.echo

    while True:
        conn = db.connect(db_path)
        db.init_db(conn)
        pid = _drain_pid()
        base = _load_baseline()
        if pid and (not base or base.get("pid") != pid):
            start = _process_start(pid)
            if start:
                _save_baseline(
                    pid, start, _remote_done_count(),
                    conn.execute("SELECT COUNT(*) c FROM transcriptions").fetchone()["c"],
                )
        report = status_report(conn, _echo=_echo)
        if as_json:
            click.echo(_json.dumps(report))
        conn.close()
        if not watch:
            break
        _time.sleep(watch)


if __name__ == '__main__':
    cli()
