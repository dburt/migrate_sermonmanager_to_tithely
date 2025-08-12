import csv

def analyze_standalone_sermons(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))

    # Filter for standalone, blank, or n/a series
    filtered_sermons = [row for row in reader if row['sermon_series'].lower() in ['standalone sermon', '', 'n/a']]

    # Sort by date
    sorted_sermons = sorted(filtered_sermons, key=lambda row: row['post_date_gmt'])

    # Calculate chunk size (5% of the filtered data)
    chunk_size = int(len(sorted_sermons) * 0.05)

    # Get the first and last chunks
    first_chunk = sorted_sermons[:chunk_size]
    last_chunk = sorted_sermons[-chunk_size:]

    print("--- First 5% of Standalone Sermons ---")
    for row in first_chunk:
        print(f"  - {row['post_date_gmt']} | {row['title']} | {row['preacher']} | {row['bible_passage']}")

    print("\n--- Last 5% of Standalone Sermons ---")
    for row in last_chunk:
        print(f"  - {row['post_date_gmt']} | {row['title']} | {row['preacher']} | {row['bible_passage']}")

if __name__ == "__main__":
    analyze_standalone_sermons('sermons_cleaned.csv')
