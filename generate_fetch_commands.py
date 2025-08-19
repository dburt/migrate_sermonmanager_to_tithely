#!/usr/bin/env -S uv run --script

import xml.etree.ElementTree as ET

def generate_fetch_commands():
    tree = ET.parse('stalfreds-podcast-fixed.xml')
    root = tree.getroot()

    for item in root.findall('.//item'):
        link = item.find('link').text
        print(f"print(default_api.web_fetch(prompt='Fetch the content of the URL: {link}'))")

if __name__ == '__main__':
    generate_fetch_commands()
