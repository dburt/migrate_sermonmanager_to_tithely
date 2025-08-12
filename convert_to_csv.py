
import xml.etree.ElementTree as ET
import csv
import re
import sys
from collections import defaultdict

def create_csv_from_export(xml_file, csv_file):
    """
    Parses a WordPress export file and converts the sermon data into a CSV file.
    """
    ns = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'wp': 'http://wordpress.org/export/1.2/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }

    # The headers for our CSV file
    headers = [
        'post_id', 'title', 'post_date_gmt', 'permalink', 'status', 'guid',
        'content_html', 'content_text', 'preacher', 'sermon_series',
        'service_type', 'bible_book', 'sermon_topics', 'audio_url', 
        'bible_passage', 'view_count'
    ]

    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            context = ET.iterparse(xml_file, events=('end',))
            for event, elem in context:
                if elem.tag == 'item':
                    # --- 1. Extract One-to-One Data ---
                    row = {
                        'post_id': elem.findtext('wp:post_id', namespaces=ns),
                        'title': elem.findtext('title'),
                        'post_date_gmt': elem.findtext('wp:post_date_gmt', namespaces=ns),
                        'permalink': elem.findtext('link'),
                        'status': elem.findtext('wp:status', namespaces=ns),
                        'guid': elem.findtext('guid')
                    }

                    # --- 2. Handle Content Fields ---
                    content_html = (elem.findtext('content:encoded', namespaces=ns) or "").strip()
                    row['content_html'] = content_html
                    row['content_text'] = re.sub(r'<[^>]+>', '', content_html)

                    # --- 3. Handle Categories (Concatenation) ---
                    categories = defaultdict(list)
                    for cat in elem.findall('category'):
                        domain = cat.get('domain', '')
                        if cat.text:
                            categories[domain].append(cat.text)
                    
                    row['preacher'] = '|'.join(categories.get('wpfc_preacher', []))
                    row['sermon_series'] = '|'.join(categories.get('wpfc_sermon_series', []))
                    row['service_type'] = '|'.join(categories.get('wpfc_service_type', []))
                    row['bible_book'] = '|'.join(categories.get('wpfc_bible_book', []))
                    row['sermon_topics'] = '|'.join(categories.get('wpfc_sermon_topics', []))

                    # --- 4. Handle Postmeta (Pivoting) ---
                    meta = defaultdict(str)
                    for postmeta in elem.findall('wp:postmeta', ns):
                        key = postmeta.findtext('wp:meta_key', namespaces=ns)
                        value = postmeta.findtext('wp:meta_value', namespaces=ns)
                        if key and value:
                            meta[key] = value

                    row['audio_url'] = meta.get('sermon_audio', '')
                    row['bible_passage'] = meta.get('bible_passage', '')
                    row['view_count'] = meta.get('Views', '')

                    writer.writerow(row)
                    elem.clear()
        
        print(f"Successfully created CSV file: {csv_file}")

    except (ET.ParseError, IOError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        create_csv_from_export(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python script.py <input_xml_file> <output_csv_file>")

