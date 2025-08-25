#!/usr/bin/env -S uv run --script

import sys
import csv

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
