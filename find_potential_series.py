import csv
from collections import defaultdict

def find_potential_series(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))

    standalone_sermons = [row for row in reader if row['sermon_series'] == 'Standalone Sermon']
    
    # Sort by date to process them in chronological order
    sorted_sermons = sorted(standalone_sermons, key=lambda row: row['post_date_gmt'])

    # Group by preacher
    preacher_sermons = defaultdict(list)
    for sermon in sorted_sermons:
        preacher_sermons[sermon['preacher']].append(sermon)

    print("--- Potential Sermon Series Found ---")

    for preacher, sermons in preacher_sermons.items():
        if len(sermons) < 2:
            continue

        potential_series = []
        current_series = [sermons[0]]

        for i in range(1, len(sermons)):
            # Check if the current sermon is likely part of the current series
            # Heuristic: same bible book, or similar title structure
            if (sermons[i]['bible_book'] and sermons[i]['bible_book'] == current_series[-1]['bible_book']) or \
               (sermons[i]['title'].split(':')[0] == current_series[-1]['title'].split(':')[0]):
                current_series.append(sermons[i])
            else:
                if len(current_series) > 1:
                    potential_series.append(current_series)
                current_series = [sermons[i]]
        
        if len(current_series) > 1:
            potential_series.append(current_series)

        if potential_series:
            print(f"\nPreacher: {preacher}")
            for i, series in enumerate(potential_series):
                print(f"  Potential Series {i+1}:")
                for sermon in series:
                    print(f"    - {sermon['post_date_gmt']} | {sermon['title']} | {sermon['bible_passage']}")

if __name__ == "__main__":
    find_potential_series('sermons_final.csv')
