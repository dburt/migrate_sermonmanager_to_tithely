import csv
from collections import defaultdict
from datetime import datetime, timedelta

def find_potential_series_v3(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))

    # Filter out non-series sermons
    non_series_values = ['standalone sermon', '']
    sermons = [row for row in reader if row['sermon_series'].lower() not in non_series_values]

    # Sort by date
    sorted_sermons = sorted(sermons, key=lambda row: row['post_date_gmt'])

    # Group by bible book
    book_sermons = defaultdict(list)
    for sermon in sorted_sermons:
        if sermon['bible_book']:
            book_sermons[sermon['bible_book']].append(sermon)

    print("--- Potential Sermon Series Found (by Bible Book) ---")

    for book, sermons in book_sermons.items():
        if len(sermons) < 2:
            continue

        print(f"\nBible Book: {book}")
        for sermon in sermons:
            print(f"    - {sermon['post_date_gmt']} | {sermon['title']} | {sermon['sermon_series']}")

    # Group by common words in title
    print("\n--- Potential Sermon Series Found (by Title) ---")
    title_sermons = defaultdict(list)
    for sermon in sorted_sermons:
        # Use the first 3 words of the title as a key
        key = " ".join(sermon['title'].split()[:3])
        title_sermons[key].append(sermon)
    
    for title_key, sermons in title_sermons.items():
        if len(sermons) > 1:
            # Check for interruptions of more than 2 weeks
            dates = [datetime.strptime(sermon['post_date_gmt'], '%Y-%m-%d %H:%M:%S') for sermon in sermons]
            if max(dates) - min(dates) > timedelta(weeks=2 * (len(sermons) -1)):
                continue

            print(f"\nTitle Key: {title_key}")
            for sermon in sermons:
                print(f"    - {sermon['post_date_gmt']} | {sermon['title']} | {sermon['sermon_series']}")

if __name__ == "__main__":
    find_potential_series_v3('sermons_final.csv')