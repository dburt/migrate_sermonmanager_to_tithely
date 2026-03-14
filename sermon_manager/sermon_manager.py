#!/usr/bin/env -S uv run --script

import os
import click
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from utils import handle_output
import core

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


if __name__ == '__main__':
    cli()
