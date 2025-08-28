#!/usr/bin/env -S uv run --script

import json
import csv

with open('sermons.json', 'r') as f:
    local_sermons = json.load(f)

with open('tithely_metadata_update/sermon_index.json', 'r') as f:
    online_sermons = json.load(f)

local_sermons_by_title = {s['title']: s for s in local_sermons}
online_sermons_by_title = {s['title']: s for s in online_sermons}

with open('detailed_discrepancy_report.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'title', 'source', 'preacher/speaker', 'discrepancies', 'sermon_series', 'bible_passage',
        'post_date_gmt', 'date', 'permalink', 'edit_url', 'audio_url',
        'guid', 'slug', 'content_text', 'service_type', 'bible_book',
        'sermon_topics', 'view_count', 'page', 'page_url'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Check for discrepancies in matched sermons
    for title, local_sermon in local_sermons_by_title.items():
        if title in online_sermons_by_title:
            online_sermon = online_sermons_by_title[title]
            discrepancy = None

            # if (local_sermon.get('preacher') != online_sermon.get('speaker') or
            #     local_sermon.get('sermon_series') != online_sermon.get('sermon_series') or
            #     local_sermon.get('bible_passage') != online_sermon.get('bible_passage')):
            #     discrepancy = True
            # list of fields with discrepancies:
            discrepancies = [
                'preacher/speaker' if local_sermon.get('preacher') != online_sermon.get('speaker') else None,
                'sermon_series' if local_sermon.get('sermon_series') != online_sermon.get('sermon_series') else None,
                'bible_passage' if local_sermon.get('bible_passage') != online_sermon.get('bible_passage') else None,
            # ].compact().join(', ')
            # compact is ruby not python, so:
            ]
            discrepancies = ', '.join([d for d in discrepancies if d is not None])

            if discrepancy:
                # Write local sermon data
                writer.writerow({
                    'title': title,
                    'source': 'local',
                    'discrepancies': discrepancies,
                    'preacher/speaker': local_sermon.get('preacher'),
                    'sermon_series': local_sermon.get('sermon_series'),
                    'bible_passage': local_sermon.get('bible_passage'),
                    'post_date_gmt': local_sermon.get('post_date_gmt'),
                    'permalink': local_sermon.get('permalink'),
                    'audio_url': local_sermon.get('audio_url'),
                    'guid': local_sermon.get('guid'),
                    'content_text': local_sermon.get('content_text'),
                    'service_type': local_sermon.get('service_type'),
                    'bible_book': local_sermon.get('bible_book'),
                    'sermon_topics': local_sermon.get('sermon_topics'),
                    'view_count': local_sermon.get('view_count')
                })

                # Write online sermon data
                writer.writerow({
                    'title': title,
                    'source': 'online',
                    'discrepancies': discrepancies,
                    'preacher/speaker': online_sermon.get('speaker'),
                    'sermon_series': online_sermon.get('sermon_series'),
                    'bible_passage': online_sermon.get('bible_passage'),
                    'date': online_sermon.get('date'),
                    'edit_url': online_sermon.get('edit_url'),
                    'slug': online_sermon.get('slug'),
                    'page': online_sermon.get('page'),
                    'page_url': online_sermon.get('page_url')
                })
        else:
            # Sermon exists locally but not online
            writer.writerow({
                'title': title,
                'source': 'local_only',
                'discrepancies': 'missing_online',
                'preacher/speaker': local_sermon.get('preacher'),
                'sermon_series': local_sermon.get('sermon_series'),
                'bible_passage': local_sermon.get('bible_passage'),
                'post_date_gmt': local_sermon.get('post_date_gmt'),
                'permalink': local_sermon.get('permalink'),
                'audio_url': local_sermon.get('audio_url'),
                'guid': local_sermon.get('guid'),
                'content_text': local_sermon.get('content_text'),
                'service_type': local_sermon.get('service_type'),
                'bible_book': local_sermon.get('bible_book'),
                'sermon_topics': local_sermon.get('sermon_topics'),
                'view_count': local_sermon.get('view_count')
            })

    for title, local_sermon in online_sermons_by_title.items():
        if title not in local_sermons_by_title:
            # Sermon exists online but not locally
            writer.writerow({
                'title': title,
                'source': 'online_only',
                'discrepancies': 'missing_local',
                'preacher/speaker': local_sermon.get('speaker'),
                'sermon_series': local_sermon.get('sermon_series'),
                'bible_passage': local_sermon.get('bible_passage'),
                'date': local_sermon.get('date'),
                'edit_url': local_sermon.get('edit_url'),
                'slug': local_sermon.get('slug'),
                'page': local_sermon.get('page'),
                'page_url': local_sermon.get('page_url')
            })

print("Detailed discrepancy report generated: detailed_discrepancy_report.csv")
