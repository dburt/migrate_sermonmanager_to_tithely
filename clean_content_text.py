#!/usr/bin/env -S uv run --script

import sys
import csv

def clean_content(row):
    """Cleans the content_text field by removing redundant information already present in other fields."""
    content = row.get('content_text', '')
    if not content:
        return content

    # List of fields to check and remove from content_text
    fields_to_remove = ['preacher', 'sermon_series', 'bible_passage']
    
    # Static boilerplate text to remove
    boilerplate = ['Bible Text:', 'Preacher:', 'Series:', '|']

    for field in fields_to_remove:
        value = row.get(field)
        if value:
            content = content.replace(value, '')

    for text in boilerplate:
        content = content.replace(text, '')

    # Clean up extra whitespace and separators
    content = ' '.join(content.split())
    
    return content

def main():
    """Main function to read from stdin, clean the CSV data, and write to stdout."""
    reader = csv.DictReader(sys.stdin)
    if not reader.fieldnames:
        return

    writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)
    writer.writeheader()

    for i, row in enumerate(reader, 1):
        try:
            # Rebuild the row to ensure it only contains valid fields, preventing errors
            # from rows that have more columns than the header.
            clean_row = {field: row.get(field) for field in reader.fieldnames}
            clean_row['content_text'] = clean_content(clean_row)
            writer.writerow(clean_row)
        except Exception as e:
            print(f"Error processing row {i}: {e}. Skipping row: {row}", file=sys.stderr)

if __name__ == "__main__":
    main()
