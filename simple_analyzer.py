import json

with open('sermons.json', 'r') as f:
    local_sermons = json.load(f)

with open('tithely_metadata_update/sermon_index.json', 'r') as f:
    online_sermons = json.load(f)

local_guids = {s['guid'] for s in local_sermons}

online_slugs = set()
for s in online_sermons:
    # The slug is the last part of the edit_url path
    slug = s['edit_url'].split('/')[-1]
    online_slugs.add(slug)

# The local guids are in the format 'http://stalfreds.org/?post_type=wpfc_sermon&p=689'
# The online slugs are in the format '2010-05-29-no-turning-back'
# I need to extract the post ID from the guid and compare it with the online slug.
# This is not a reliable way to match sermons.

# Let's use the title to match, as the analyzer script does.

local_titles = {s['title'] for s in local_sermons}
online_titles = {s['title'] for s in online_sermons}

matched_sermons = local_titles.intersection(online_titles)
local_only = local_titles.difference(online_titles)
online_only = online_titles.difference(local_titles)

print(f"Total local sermons: {len(local_sermons)}")
print(f"Total online sermons: {len(online_sermons)}")
print(f"Sermons matched on both sides (by title): {len(matched_sermons)}")
print(f"Sermons only in local file (by title): {len(local_only)}")
print(f"Sermons only on Tithely (by title): {len(online_only)}")

