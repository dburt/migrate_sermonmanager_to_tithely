#!/usr/bin/env -S uv run --script

import xml.etree.ElementTree as ET

tree = ET.parse('stalfreds-podcast.xml')
root = tree.getroot()

for item in root.findall('.//item'):
    link = item.find('link')
    guid = item.find('guid')
    if link is not None and guid is not None:
        guid.text = link.text
        guid.set('isPermaLink', 'true')

tree.write('stalfreds-podcast.xml', encoding='UTF-8', xml_declaration=True)
