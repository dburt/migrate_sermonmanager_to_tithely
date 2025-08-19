#!/usr/bin/env -S uv run --script
import xml.etree.ElementTree as ET
import requests

tree = ET.parse('stalfreds-podcast.xml')
root = tree.getroot()

with open('url_report.txt', 'w') as f:
    for item in root.findall('.//item'):
        enclosure = item.find('enclosure')
        if enclosure is not None:
            url = enclosure.get('url')
            if url:
                try:
                    response = requests.head(url, allow_redirects=True)
                    if response.status_code == 200:
                        f.write(f'{url} is valid\n')
                    else:
                        f.write(f'{url} is not valid. Status code: {response.status_code}\n')
                except requests.exceptions.RequestException as e:
                    f.write(f'{url} is not valid. Error: {e}\n')