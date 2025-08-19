#!/usr/bin/env -S uv run --script
import csv
import json
import argparse

def clean_and_convert_csv_to_json(csv_filepath, json_filepath):
    data = []
    header = None
    processed_post_ids = set()

    with open(csv_filepath, 'r', encoding='utf-8') as csvf:
        lines = csvf.readlines()

        for i, line in enumerate(lines):
            stripped_line = line.strip()
            if not stripped_line:
                continue

            if i == 0:
                header = stripped_line.split(',')
                continue
            elif stripped_line == ','.join(header):
                continue

            try:
                reader = csv.reader([stripped_line])
                row_values = next(reader)
            except csv.Error as e:
                print(f"Skipping malformed row due to CSV error: {e} in line: {stripped_line}")
                continue

            if len(row_values) != len(header):
                print(f"Skipping row with incorrect number of columns: {stripped_line}")
                continue

            obj = {}
            for j, h in enumerate(header):
                obj[h] = row_values[j]
            
            post_id = obj.get('post_id')
            if post_id == '897':
                if obj.get('audio_url') == 'http://s3-ap-southeast-2.amazonaws.com/stamp3,29':
                    print(f"Skipping deficient duplicate for post_id 897: {obj}")
                    continue
                elif post_id in processed_post_ids:
                    print(f"Skipping already processed post_id 897: {obj}")
                    continue
            
            data.append(obj)
            if post_id:
                processed_post_ids.add(post_id)

    with open(json_filepath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    print(f"Successfully cleaned and converted {csv_filepath} to {json_filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
    parser.add_argument('csv_filepath', help='The path to the input CSV file.')
    parser.add_argument('json_filepath', help='The path to the output JSON file.')
    args = parser.parse_args()
    clean_and_convert_csv_to_json(args.csv_filepath, args.json_filepath)