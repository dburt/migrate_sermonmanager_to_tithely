#!/usr/bin/env -S uv run --script
import csv
import html
import re

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            cleaned_row = [html.unescape(field) for field in row]
            
            # Create a dictionary from the header and the cleaned row
            row_dict = dict(zip(header, cleaned_row))

            # Attempt to extract missing data from content_text
            if not row_dict.get('preacher'):
                match = re.search(r'Preacher: (.*?)(?:\||$)', row_dict.get('content_text', ''))
                if match:
                    row_dict['preacher'] = match.group(1).strip()

            if not row_dict.get('sermon_series'):
                match = re.search(r'Series: (.*?)(?:\||$)', row_dict.get('content_text', ''))
                if match:
                    row_dict['sermon_series'] = match.group(1).strip()

            if not row_dict.get('bible_passage'):
                match = re.search(r'Bible Text: (.*?)(?:\||$)', row_dict.get('content_text', ''))
                if match:
                    row_dict['bible_passage'] = match.group(1).strip()

            # Write the updated row back to the list
            final_row = [row_dict[h] for h in header]
            writer.writerow(final_row)

if __name__ == "__main__":
    clean_csv('sermons.csv', 'sermons_cleaned.csv')
