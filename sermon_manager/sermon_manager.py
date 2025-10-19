#!/usr/bin/env -S uv run --script

import os
import click
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from utils import handle_output

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

        df = pd.read_csv("sermons.csv")

        # Calculate audio_file_size if not present
        if 'audio_file_size' not in df.columns:
            click.echo("Calculating audio file sizes... This may take a while.")
            # Create a dummy manager to access get_file_size
            with TithelyManager("", "", headless=True) as manager:
                df['audio_file_size'] = [manager.get_file_size(url) for url in tqdm(df['audio_url'], desc="Fetching file sizes")]
            click.echo("Audio file sizes calculated.")

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
        
        click.echo("Sermon updated successfully!")

    except Exception as e:
        click.echo(f"An error occurred: {e}")

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



if __name__ == '__main__':
    cli()
