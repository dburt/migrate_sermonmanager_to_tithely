#!/usr/bin/env -S uv run --script

import json
from datetime import datetime, timezone
import html
import argparse

def generate_rss_feed(json_filepath, rss_filepath):
    with open(json_filepath, 'r', encoding='utf-8') as f:
        sermons = json.load(f)

    current_year = datetime.now().year
    build_date = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S %z')

    # RSS Feed Header
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
    <itunes:image href="https://stalfreds.org/podcast-logo.jpg" />
    <itunes:category text="Religion &amp; Spirituality"/>
    <image>
        <url>https://stalfreds.org/podcast-logo.jpg</url>
        <title>St Alfred's Anglican Church Sermons</title>
        <link>https://stalfreds.org/sermons/</link>
    </image>
'''

    # RSS Feed Items
    for sermon in sermons:
        continue if not sermon.get('status') == 'publish'

        title = html.escape(sermon.get('title', 'No Title'))
        permalink = sermon.get('permalink', '#')
        post_date_gmt = sermon.get('post_date_gmt')
        audio_url = sermon.get('audio_url')
        preacher = html.escape(sermon.get('preacher', 'N/A'))
        sermon_series = html.escape(sermon.get('sermon_series', 'N/A'))
        bible_passage = html.escape(sermon.get('bible_passage', 'N/A'))
        content_text = html.escape(sermon.get('content_text', ''))
        image_url = sermon.get('image_url', '') # Assuming image_url is for the series art

        pub_date = ""
        if post_date_gmt:
            try:
                dt_object = datetime.strptime(post_date_gmt, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
                pub_date = dt_object.strftime('%a, %d %b %Y %H:%M:%S %z')
            except ValueError:
                pub_date = ""

        description = f"In this sermon, {preacher} speaks on the theme of {title} as part of the series {sermon_series}. The Bible reading is {bible_passage}. {content_text}"
        summary = description

        enclosure = ""
        if audio_url and audio_url != '-':
            audio_type = "audio/mpeg"
            if '.mp3' in audio_url.lower():
                audio_type = "audio/mpeg"
            elif '.m4a' in audio_url.lower():
                audio_type = "audio/x-m4a"
            enclosure = f'<enclosure url="{html.escape(audio_url)}" type="{audio_type}" length="0" />'

        item_image = f'<itunes:image href="{html.escape(image_url)}" />' if image_url else ''

        rss_feed += f'''
    <item>
        <title>{title}</title>
        <link>{permalink}</link>
        <pubDate>{pub_date}</pubDate>
        <guid>{permalink}</guid>
        {enclosure}
        <description><![CDATA[{description}]]></description>
        <itunes:author>{preacher}</itunes:author>
        <itunes:subtitle>{sermon_series} | {preacher} | {bible_passage}</itunes:subtitle>
        <itunes:summary><![CDATA[{summary}]]></itunes:summary>
        {item_image}
        <itunes:explicit>false</itunes:explicit>
    </item>
'''

    rss_feed += '''
</channel>
</rss>
'''

    with open(rss_filepath, 'w', encoding='utf-8') as f:
        f.write(rss_feed)

    print(f"Successfully generated RSS feed at {rss_filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an RSS feed from a JSON file.')
    parser.add_argument('json_filepath', help='The path to the input JSON file.')
    parser.add_argument('rss_filepath', help='The path to the output RSS file.')
    args = parser.parse_args()
    generate_rss_feed(args.json_filepath, args.rss_filepath)
