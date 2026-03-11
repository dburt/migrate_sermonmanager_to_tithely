import json
import csv

with open('sermons.json', 'r') as f:
    local_sermons = json.load(f)

with open('sermon_index.json', 'r') as f:
    online_sermons = json.load(f)

local_sermons_by_title = {s['title']: s for s in local_sermons}
online_sermons_by_title = {s['title']: s for s in online_sermons}

with open('discrepancy_report.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'status', 'local_preacher', 'online_speaker', 'local_sermon_series', 'online_sermon_series', 'local_bible_passage', 'online_bible_passage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Check for discrepancies in matched sermons
    for title, local_sermon in local_sermons_by_title.items():
        if title in online_sermons_by_title:
            online_sermon = online_sermons_by_title[title]
            discrepancy = False
            row = {'title': title, 'status': 'discrepancy'}

            if local_sermon.get('preacher') != online_sermon.get('speaker'):
                discrepancy = True
                row['local_preacher'] = local_sermon.get('preacher')
                row['online_speaker'] = online_sermon.get('speaker')

            if local_sermon.get('sermon_series') != online_sermon.get('sermon_series'):
                discrepancy = True
                row['local_sermon_series'] = local_sermon.get('sermon_series')
                row['online_sermon_series'] = online_sermon.get('sermon_series')

            if local_sermon.get('bible_passage') != online_sermon.get('bible_passage'):
                discrepancy = True
                row['local_bible_passage'] = local_sermon.get('bible_passage')
                row['online_bible_passage'] = online_sermon.get('bible_passage')

            if discrepancy:
                writer.writerow(row)

    # Check for local only sermons
    for title, local_sermon in local_sermons_by_title.items():
        if title not in online_sermons_by_title:
            writer.writerow({'title': title, 'status': 'local_only'})

    # Check for online only sermons
    for title, online_sermon in online_sermons_by_title.items():
        if title not in local_sermons_by_title:
            writer.writerow({'title': title, 'status': 'online_only'})

print("Discrepancy report generated: discrepancy_report.csv")
