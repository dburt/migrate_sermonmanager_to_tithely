#!/usr/bin/env -S uv run --script
import xml.etree.ElementTree as ET
import re
import sys
from collections import Counter

def analyze_content_details(xml_file):
    """
    Parses a WordPress export XML file to analyze the composition of the
    'content:encoded' field.
    """
    ns = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
    }

    total_items = 0
    total_content_len = 0
    total_markup_len = 0
    total_text_len = 0
    max_content_len = 0
    max_text_len = 0

    # Use iterparse for memory-efficient parsing
    try:
        context = ET.iterparse(xml_file, events=('end',))
        for event, elem in context:
            if elem.tag == 'item':
                total_items += 1
                content_element = elem.find('content:encoded', ns)
                
                content_html = (content_element.text or "").strip()
                content_len = len(content_html)
                
                # Find all HTML tags
                tags = re.findall(r'<[^>]+>', content_html)
                markup_len = sum(len(tag) for tag in tags)
                
                # Calculate plain text by removing tags
                plain_text = re.sub(r'<[^>]+>', '', content_html)
                text_len = len(plain_text)

                total_content_len += content_len
                total_markup_len += markup_len
                total_text_len += text_len
                
                if content_len > max_content_len:
                    max_content_len = content_len
                if text_len > max_text_len:
                    max_text_len = text_len

                elem.clear()

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return

    print(f"--- Content Field Analysis for {xml_file} ---")
    print(f"\nProcessed {total_items} items.")

    # --- Overall Statistics ---
    print("\n--- Overall Composition ---")
    if total_content_len > 0:
        text_percentage = (total_text_len / total_content_len) * 100
        markup_percentage = (total_markup_len / total_content_len) * 100
        print(f"Total characters in content fields: {total_content_len}")
        print(f"- Plain Text: {total_text_len} characters ({text_percentage:.1f}%)")
        print(f"- HTML Markup: {total_markup_len} characters ({markup_percentage:.1f}%)")
    else:
        print("No content found to analyze.")

    # --- Size Analysis ---
    print("\n--- Size and Usefulness ---")
    avg_text_len = total_text_len / total_items if total_items > 0 else 0
    print(f"Average plain text per item: {avg_text_len:.0f} characters.")
    print(f"Longest plain text in a single item: {max_text_len} characters.")
    print(f"Longest total content (including markup) in a single item: {max_content_len} characters.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_content_details(sys.argv[1])
    else:
        print("Please provide the path to the XML file.")

