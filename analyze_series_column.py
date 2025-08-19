#!/usr/bin/env -S uv run --script

import csv
from collections import Counter

def analyze_series_column(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        series_values = [row['sermon_series'] for row in reader]

    series_counts = Counter(series_values)

    print("--- Sermon Series Column Analysis ---")
    for series, count in series_counts.most_common(20):
        print(f"  - '{series}': {count}")

if __name__ == "__main__":
    analyze_series_column('sermons_cleaned.csv')
