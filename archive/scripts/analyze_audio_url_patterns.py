import csv
import re
import os
from collections import defaultdict

def analyze_patterns(csv_filepath):
    audio_patterns = defaultdict(int)
    permalink_patterns = defaultdict(int)
    with open(csv_filepath, 'r', encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            audio_url = row.get('audio_url', '')
            if audio_url:
                filename, _ = os.path.splitext(audio_url.split('/')[-1])
                match = re.search(r'\d{4}-?\d\d-?\d\d-(\d+)', filename, re.IGNORECASE)
                if match:
                    audio_patterns[match.group(1)] += 1
            
            permalink = row.get('permalink', '')
            if permalink:
                slug = permalink.strip('/').split('/')[-1]
                match = re.search(r'(-\d{1,2}[ap]?m?l?\b)[\w.-]*?$', slug, re.IGNORECASE)
                if match:
                    permalink_patterns[match.group(1)] += 1

    print("--- Audio URL Patterns ---")
    for pattern, count in audio_patterns.items():
        print(f"Pattern: {pattern}, Count: {count}")

    print("\n--- Permalink Patterns ---")
    for pattern, count in permalink_patterns.items():
        print(f"Pattern: {pattern}, Count: {count}")

if __name__ == "__main__":
    analyze_patterns('sermons_cleaned_ai_studio.csv')