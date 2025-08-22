#!/bin/bash

set -ex

# Fetch edit page for a particular sermon
# Response will be Vue JS with page content including options for speaker, podcast and series dropdowns
# Select sermon based on date and slugified title
# Valid session will be required

SERMON="${SERMON:="2025-07-06-maturity-in-action"}"
SESSION="${SESSION:="ODdJYTltZGRLQnB1WWpNMWFnQlhXNnN2Mnkyd0VWblBNUTJUMDJkKzVjT25CbDJ0RkR4c2xwblh6ZFBUUzdmODVjeVVXNVRyZ1UxdHBEQ2R3T1lEWGNwaXJ4NzVQZGkyQlp1NXhsalVNS1BLRGp4TllzNmpVa3BmWUhGcjVmOXdzMlhNemZLWisvakw3NFk3MDBBRGsyVWJGakVveEoveld2aUhmWHlBbkorTGc5VWp4d0dyZ1E1RWlMYmhRT0FkYmFldHNwencwUE5mK2hmR09vRjcySVVZbWxMTy9GcGpRMmlpWG92UVBXaz0tLVFHNTM0OW1WSVFUdFpYVFZTUVk2amc9PQ%3D%3D--c41cf7a239f40c1dafad1c287faa49aabb8f1d76"}"

curl -f "https://stalfreds.tithelysetup.com/media/$SERMON/edit?podcast=test-sermon-import" \
  -H 'accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
  -H 'accept-language: en-GB,en;q=0.5' \
  -b "_engage_session=$SESSION" \
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
  -H 'x-csrf-token: DiZyMxPZ6U3fd66VS69mxLNDDHmjPw7XUiApq6MM3X6U2JBpNiGob+4zlll3W9GMNfT7A9aWJzfjt3jkKI0RBg==' \
  -H 'x-requested-with: XMLHttpRequest'
