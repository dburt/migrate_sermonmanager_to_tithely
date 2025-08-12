
import csv
from datetime import datetime

def analyze_sermons_data(file_path):
    date_formats = set()
    sermon_series_missing = 0
    sermon_topics_missing = 0
    total_rows = 0

    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            total_rows += 1
            
            # Check date format
            date_str = row.get('post_date_gmt')
            if date_str:
                try:
                    datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                    date_formats.add('%Y-%m-%d %H:%M:%S')
                except ValueError:
                    date_formats.add('Unknown')
            
            # Check for missing sermon series
            if not row.get('sermon_series'):
                sermon_series_missing += 1

            # Check for missing sermon topics
            if not row.get('sermon_topics'):
                sermon_topics_missing += 1

    print(f"Total rows analyzed: {total_rows}")
    print(f"Date formats found: {date_formats}")
    print(f"Rows with missing sermon series: {sermon_series_missing}")
    print(f"Rows with missing sermon topics: {sermon_topics_missing}")

if __name__ == "__main__":
    analyze_sermons_data('sermons_cleaned.csv')
