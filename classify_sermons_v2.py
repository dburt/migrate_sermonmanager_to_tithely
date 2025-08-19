#!/usr/bin/env -S uv run --script
import csv
import subprocess

def classify_sermons_with_gemini(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))

    # Get the first 10 rows
    sample_data = reader[:10]

    # Construct the prompt
    prompt = """Analyze the following sermon data and provide suggestions for improving data quality.
Focus on identifying sermon series, standardizing titles, correcting preacher names, consolidating service types, and populating sermon topics.
Please provide the corrected data in a CSV format.

---

"""

    # Add header
    header = sample_data[0].keys()
    prompt += ",".join(header) + "\n"

    # Add data
    for row in sample_data:
        prompt += ",".join(row.values()) + "\n"

    # Execute the gemini command
    process = subprocess.run(['gemini', prompt], capture_output=True, text=True)
    
    print("--- Gemini Suggestions ---")
    print(process.stdout)

if __name__ == "__main__":
    classify_sermons_with_gemini('sermons_cleaned.csv')
