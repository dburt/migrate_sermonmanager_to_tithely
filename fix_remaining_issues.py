
import xml.etree.ElementTree as ET
import html

tree = ET.parse('stalfreds-podcast.xml')
root = tree.getroot()

for item in root.findall('.//item'):
    subtitle = item.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}subtitle')
    if subtitle is not None and subtitle.text is not None and len(subtitle.text) > 255:
        subtitle.text = subtitle.text[:255]

    summary = item.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}summary')
    if summary is not None and summary.text is not None:
        summary.text = html.unescape(summary.text)

    keywords = item.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}keywords')
    if keywords is not None and keywords.text is not None:
        keywords.text = keywords.text.replace(' ', ',')

tree.write('stalfreds-podcast.xml', encoding='UTF-8', xml_declaration=True)
