#!/usr/bin/env -S uv run --script
import csv
import re

def final_clean(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Correct sermon series
            if "Worship and the Arts" in row['title']:
                row['sermon_series'] = "Worship and the Arts"
            if "The Heavens Declare" in row['title']:
                row['sermon_series'] = "The Heavens Declare"
            if "Of Royal Descent" in row['title'] or "A Royal Visit" in row['title']:
                 row['sermon_series'] = "Christmas 2005"
            if row['bible_book'] == '2 Timothy':
                row['sermon_series'] = "2 Timothy"

            # Standardize titles
            row['title'] = re.sub(r's@10', '10am', row['title'], flags=re.IGNORECASE)
            row['title'] = re.sub(r's@6', '6pm', row['title'], flags=re.IGNORECASE)

            # Consolidate preacher names
            if row['preacher'] == 'Michael McNamara':
                row['preacher'] = 'Mike McNamara'

            writer.writerow(row)

if __name__ == "__main__":
    final_clean('sermons_cleaned.csv', 'sermons_final.csv')
