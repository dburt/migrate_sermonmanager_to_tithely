import csv
import re
from collections import Counter

def detailed_analysis(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))

    # --- Analyze "Standalone Sermon" entries ---
    print("--- Analyzing Standalone Sermons ---")
    standalone_sermons = [row for row in reader if row['sermon_series'] == 'Standalone Sermon']
    
    # Look for titles with "Part X"
    part_in_title = [row['title'] for row in standalone_sermons if re.search(r'Part \d+', row['title'], re.IGNORECASE)]
    if part_in_title:
        print("Found standalone sermons with 'Part X' in the title:")
        for title in part_in_title:
            print(f"  - {title}")

    # Look for consecutive standalone sermons by the same preacher and bible book
    potential_series = []
    for i in range(len(standalone_sermons) - 1):
        current_sermon = standalone_sermons[i]
        next_sermon = standalone_sermons[i+1]
        if current_sermon['preacher'] == next_sermon['preacher'] and \
           current_sermon['bible_book'] and \
           current_sermon['bible_book'] == next_sermon['bible_book']:
            potential_series.append((current_sermon['title'], next_sermon['title']))

    if potential_series:
        print("\nFound potential series marked as standalone:")
        for series in potential_series:
            print(f"  - {series[0]} -> {series[1]}")

    # --- Analyze title consistency ---
    print("\n--- Analyzing Service Info in Titles ---")
    service_in_title_patterns = ['s@10', '10am', 's@6', '6pm']
    titles_with_service_info = [row['title'] for row in reader if any(p in row['title'].lower() for p in service_in_title_patterns)]
    print(f"Found {len(titles_with_service_info)} titles with service information.")

    # --- Analyze other inconsistencies ---
    print("\n--- Analyzing Other Inconsistencies ---")
    preachers = [row['preacher'] for row in reader if row['preacher']]
    preacher_counts = Counter(preachers)
    print("Preacher counts (top 10):")
    for preacher, count in preacher_counts.most_common(10):
        print(f"  - {preacher}: {count}")

    service_types = [row['service_type'] for row in reader if row['service_type']]
    service_type_counts = Counter(service_types)
    print("\nService type counts:")
    for service_type, count in service_type_counts.items():
        print(f"  - {service_type}: {count}")

if __name__ == "__main__":
    detailed_analysis('sermons_cleaned.csv')