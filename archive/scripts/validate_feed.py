#!/usr/bin/env -S uv run --script

import feedparser

feed = feedparser.parse('stalfreds-podcast.xml')

if feed.bozo:
    print(f'The feed is not well-formed. Error: {feed.bozo_exception}')
else:
    print('The feed is well-formed.')
