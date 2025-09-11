#!/usr/bin/env -S uv run --script

import sys
import csv
import re
import argparse
import os
from collections import defaultdict

def correct_service_time_and_date(row):
    """Corrects the service_type and adds a melbourne_time column based on audio_url and permalink."""
    audio_url = row.get('audio_url', '')
    permalink = row.get('permalink', '')
    post_date_gmt = row.get('post_date_gmt', '')
    row['melbourne_time'] = '' # Initialize the new column

    # Patterns for different times
    time_patterns = {
        '10:00': [r'-10l', r'-10', r'-10am', r'-1000am'],
        '18:00': [r'-6pm', r'-18', r'-600pm', r'-6'],
        '09:00': [r'-9am', r'-9', r'-09'],
        '11:00': [r'-11am', r'-11'],
        '09:30': [r'-0930l', r'-930am', r'-930'],
        '23:30': [r'-23l', r'-23']
    }

    # Check audio_url for time patterns
    if audio_url:
        filename, _ = os.path.splitext(audio_url.split('/')[-1])
        for time, patterns in time_patterns.items():
            for pattern in patterns:
                if re.search(fr'{pattern}[\w.-]*$', filename, re.IGNORECASE):
                    row['service_type'] = f"Sundays at {time}"
                    if ' ' in post_date_gmt:
                        date_part = post_date_gmt.split(' ')[0]
                        row['melbourne_time'] = f"{date_part}T{time}:00+10:00"
                    return row # first match wins

    # Check permalink for time patterns
    if permalink:
        slug = permalink.strip('/').split('/')[-1]
        for time, patterns in time_patterns.items():
            for pattern in patterns:
                if re.search(fr'{pattern}[\w.-]*$', slug, re.IGNORECASE):
                    row['service_type'] = f"Sundays at {time}"
                    if ' ' in post_date_gmt:
                        date_part = post_date_gmt.split(' ')[0]
                        row['melbourne_time'] = f"{date_part}T{time}:00+10:00"
                    return row # first match wins

    return row

def clean_content(row):
    """Cleans the content_text field by removing redundant information already present in other fields."""
    content = row.get('content_text', '')
    if not content:
        return content

    parts = content.split('|')
    new_parts = []
    for part in parts:
        part = part.strip()
        if not part.lower().startswith(('bible text:', 'preacher:', 'series:')):
            new_parts.append(part)

    return ' '.join(new_parts)

def main():
    """Main function to read from a file, clean the CSV data, and write back to the file."""
    parser = argparse.ArgumentParser(description='Clean a CSV file.')
    parser.add_argument('input_csv', help='The path to the input CSV file.')
    parser.add_argument('output_csv', help='The path to the output CSV file.')
    args = parser.parse_args()

    rows = []
    problematic_rows = []
    with open(args.input_csv, 'r', encoding='utf-8') as csvf:
        reader = csv.reader(csvf)
        header = next(reader)
        fieldnames = header + ['melbourne_time']
        for row_values in reader:
            if row_values and row_values[0] == 'post_id':
                continue # Skip extra header rows
            if len(row_values) > len(header):
                problematic_rows.append(row_values)
            elif len(row_values) == len(header):
                rows.append(dict(zip(header, row_values)))

    if problematic_rows:
        with open('problematic_rows.csv', 'w', encoding='utf-8', newline='') as csvf:
            writer = csv.writer(csvf)
            # Create a header for the problematic rows file
            problematic_header = header + [f'extra_col_{i+1}' for i in range(len(problematic_rows[0]) - len(header))]
            writer.writerow(problematic_header)
            writer.writerows(problematic_rows)
        print(f"Found {len(problematic_rows)} problematic rows. Saved to problematic_rows.csv")

    # First pass: correct service time and date
    corrected_rows = [correct_service_time_and_date(row) for row in rows]

    # Second pass: handle duplicate titles
    title_counts = defaultdict(int)
    for row in corrected_rows:
        title_counts[row.get('title')] += 1

    processed_titles = set()
    final_rows = []
    for row in corrected_rows:
        original_title = row.get('title')
        if title_counts[original_title] > 1:
            new_title = original_title
            service_time = row.get('service_type', '')
            post_date = row.get('post_date_gmt', '')

            if '10:00' in service_time:
                new_title = f"{original_title} (10am)"
            elif '18:00' in service_time:
                new_title = f"{original_title} (6pm)"
            
            if new_title in processed_titles and post_date:
                year = post_date.split('-')[0]
                new_title = f"{original_title} ({year})"
            
            if new_title in processed_titles and post_date:
                new_title = f"{original_title} ({post_date.split(' ')[0]})"

            # Ensure final title is unique
            final_title = new_title
            counter = 1
            while final_title in processed_titles:
                final_title = f"{new_title} ({counter})"
                counter += 1
            
            row['title'] = final_title
            processed_titles.add(final_title)
        else:
            processed_titles.add(original_title)
        
        row['content_text'] = clean_content(row)
        final_rows.append(row)

    with open(args.output_csv, 'w', encoding='utf-8', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        # Filter out any keys that are not in the fieldnames
        output_rows = []
        for row in final_rows:
            output_rows.append({k: row.get(k) for k in fieldnames})
        writer.writerows(output_rows)

    print(f"Successfully cleaned {args.input_csv} into {args.output_csv}")

if __name__ == "__main__":
    main()
