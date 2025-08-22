#!/bin/bash

set -ex

# Post an update for a sermon on Tithely
# Response will be JSON with sermon details
# Select sermon based on date and slugified title
# Valid session will be required

SERMON="${SERMON:="2025-07-06-maturity-in-action"}"
SESSION="${SESSION:="ODdJYTltZGRLQnB1WWpNMWFnQlhXNnN2Mnkyd0VWblBNUTJUMDJkKzVjT25CbDJ0RkR4c2xwblh6ZFBUUzdmODVjeVVXNVRyZ1UxdHBEQ2R3T1lEWGNwaXJ4NzVQZGkyQlp1NXhsalVNS1BLRGp4TllzNmpVa3BmWUhGcjVmOXdzMlhNemZLWisvakw3NFk3MDBBRGsyVWJGakVveEoveld2aUhmWHlBbkorTGc5VWp4d0dyZ1E1RWlMYmhRT0FkYmFldHNwencwUE5mK2hmR09vRjcySVVZbWxMTy9GcGpRMmlpWG92UVBXaz0tLVFHNTM0OW1WSVFUdFpYVFZTUVk2amc9PQ%3D%3D--c41cf7a239f40c1dafad1c287faa49aabb8f1d76"}"

TITLE="${TITLE:="Maturity in Conflict"}"
SUBTITLE="${SUBTITLE:=""}"
SERMON_DATE="${SERMON_DATE:="2025-07-27"}"
SPEAKER_ID="${SPEAKER_ID:="7"}"
PODCAST_ID="${PODCAST_ID:="3"}"
SERIES_ID="${SERIES_ID:="new"}"
SERIES_TITLE="${SERIES_TITLE:="James: Maturity in Christ"}"
PASSAGES="${PASSAGES:="James 4:1-12"}"
TOPIC="${TOPIC:="<p>In this sermon, Ren&eacute; Pfitzner speaks on the theme of Maturity in Conflict as part of the series James: Maturity in Christ. The Bible reading is James 4:1-12.</p>"}"

curl "https://stalfreds.tithelysetup.com/media/$SERMON" \
  -H 'accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
  -H 'accept-language: en-GB,en;q=0.5' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundaryxvozT40vAWVkuqh9' \
  -b "_engage_session=$SESSION" \
  -H 'origin: https://stalfreds.tithelysetup.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://stalfreds.tithelysetup.com/podcasts/test-sermon-import' \
  -H 'sec-ch-ua: "Not;A=Brand";v="99", "Brave";v="139", "Chromium";v="139"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: cwwk5akx84oLpMUntXgUDE1Vy70mMw2qpQH+a2a8oCnp8sa/jMmyqDrg/euJjKNEy+I8x1OaJEoUlq8k7T1sUQ==' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw $'------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="utf8"\r\n\r\n✓\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="_method"\r\n\r\npatch\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[title]"\r\n\r\n'"$TITLE"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[subtitle]"\r\n\r\n'"$SUBTITLE"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[sermon_date]"\r\n\r\n'"$SERMON_DATE"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[speaker_id]"\r\n\r\n'"$SPEAKER_ID"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[podcast_id]"\r\n\r\n'"$PODCAST_ID"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[series_id]"\r\n\r\n'"$SERIES_ID"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[series_title]"\r\n\r\n'"$SERIES_TITLE"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[passages]"\r\n\r\n'"$PASSAGES"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[topic]"\r\n\r\n'"$TOPIC"'\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[retained_audio]"\r\n\r\n\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[retained_notes]"\r\n\r\n\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[remove_audio]"\r\n\r\n\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[video_url]"\r\n\r\n\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="sermon[password]"\r\n\r\n\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9\r\nContent-Disposition: form-data; name="button"\r\n\r\n\r\n------WebKitFormBoundaryxvozT40vAWVkuqh9--\r\n'
