#!/usr/bin/env -S uv run --script
import csv
import subprocess

def classify_sermon_with_debug(sermon):
    prompt = f"""Analyze the following sermon data and provide suggestions for improving its quality.

Sermon Data:
- Title: {sermon['title']}
- Preacher: {sermon['preacher']}
- Sermon Series: {sermon['sermon_series']}
- Service Type: {sermon['service_type']}
- Bible Passage: {sermon['bible_passage']}
- Post Date (GMT): {sermon['post_date_gmt']}

Please provide suggestions for the following fields, keeping your response concise:
1.  **Sermon Series:** Suggest a more appropriate series name if this sermon seems to be part of a series. Otherwise, suggest "Standalone".
2.  **Sermon Topics:** Suggest 1-3 relevant topics.
3.  **Title:** Suggest a standardized title.
4.  **Preacher Name:** Suggest a corrected name if there are inconsistencies.
5.  **Service Type:** Suggest a consolidated service type.
"""
    
    process = subprocess.run(['gemini', '--debug', prompt], capture_output=True, text=True)
    return process.stdout.strip()

def classify_sermons_one_by_one_v2(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))

    standalone_sermons = [row for row in reader if row['sermon_series'] == 'Standalone Sermon']

    for sermon in standalone_sermons[:5]:
        suggestions = classify_sermon_with_debug(sermon)
        print(f"Sermon: {sermon['title']}")
        print(f"Gemini Suggestions:\n{suggestions}")
        print("---")

if __name__ == "__main__":
    classify_sermons_one_by_one_v2('sermons_cleaned.csv')
