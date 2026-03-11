#!/usr/bin/env -S uv run --script
import xml.etree.ElementTree as ET
from collections import Counter
import sys

def analyze_export_file(xml_file):
    """
    Parses a WordPress export XML file to analyze one-to-many relationships
    and content redundancy.
    """
    # Namespaces used in the XML file
    ns = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'wp': 'http://wordpress.org/export/1.2/'
    }

    # Counters to store our findings
    meta_key_counts = Counter()
    category_domain_counts = Counter()
    content_counts = Counter()
    
    items_processed = 0
    postmeta_per_item = []
    categories_per_item = []

    # Use iterparse for memory-efficient parsing of large files
    try:
        context = ET.iterparse(xml_file, events=('end',))
        for event, elem in context:
            # Process each 'item' element once it's fully read
            if elem.tag == 'item':
                items_processed += 1

                # 1. Analyze wp:postmeta
                meta_elements = elem.findall('wp:postmeta', ns)
                postmeta_per_item.append(len(meta_elements))
                for meta in meta_elements:
                    key = meta.find('wp:meta_key', ns)
                    if key is not None and key.text:
                        meta_key_counts[key.text] += 1

                # 2. Analyze category
                category_elements = elem.findall('category')
                categories_per_item.append(len(category_elements))
                for cat in category_elements:
                    domain = cat.get('domain', 'unknown_domain')
                    category_domain_counts[domain] += 1

                # 3. Analyze content:encoded for redundancy
                content_element = elem.find('content:encoded', ns)
                if content_element is not None and content_element.text:
                    content_counts[content_element.text.strip()] += 1
                else:
                    content_counts['--EMPTY--'] += 1
                
                # Free up memory by clearing the element
                elem.clear()

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return

    print(f"--- Analysis Results for {xml_file} ---")
    print(f"\nTotal Items (Sermons) Processed: {items_processed}\n")

    # --- Postmeta Report ---
    print("--- One-to-Many: wp:postmeta ---")
    if postmeta_per_item:
        avg_meta = sum(postmeta_per_item) / len(postmeta_per_item)
        print(f"Each item has between {min(postmeta_per_item)} and {max(postmeta_per_item)} 'wp:postmeta' tags (avg: {avg_meta:.1f}).")
    print("\nTop 10 most common meta keys across all items:")
    for key, count in meta_key_counts.most_common(10):
        print(f"- '{key}': {count} times")

    # --- Category Report ---
    print("\n--- One-to-Many: category ---")
    if categories_per_item:
        avg_cat = sum(categories_per_item) / len(categories_per_item)
        print(f"Each item has between {min(categories_per_item)} and {max(categories_per_item)} 'category' tags (avg: {avg_cat:.1f}).")
    print("\nCategory domains found:")
    for domain, count in category_domain_counts.most_common():
        print(f"- '{domain}': {count} times")

    # --- Content Redundancy Report ---
    print("\n--- Redundancy: content:encoded ---")
    print(f"Found {len(content_counts)} unique content blocks.")
    print("\nTop 5 most common content blocks:")
    for content, count in content_counts.most_common(5):
        # Truncate long content for readability
        display_content = (content[:150] + '...') if len(content) > 150 else content
        print(f"\n1. Count: {count} times")
        print(f"   Content: '{display_content}'")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_export_file(sys.argv[1])
    else:
        print("Please provide the path to the XML file.")
