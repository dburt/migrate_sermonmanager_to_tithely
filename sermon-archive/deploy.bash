#!/bin/bash

set -ex

# Regenerate static site assets from the local mirror DB.
cd "$(dirname "$0")/.."
uv run python sermon_manager/sermon_manager.py export --out-dir sermon-archive

rsync --verbose --copy-links \
    sermon-archive/stalfreds-sermons.html \
    sermon-archive/sermons.json \
    sermon-archive/podcast_feed.xml \
    illuminu@burt.id.au:dave.burt.id.au/

rsync --verbose --copy-links -r \
    sermon-archive/transcripts/ \
    illuminu@burt.id.au:dave.burt.id.au/transcripts/