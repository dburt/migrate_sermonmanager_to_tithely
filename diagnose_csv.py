#!/usr/bin/env -S uv run --script
import sys
import csv

def diagnose_csv(filepath):
    """
    Diagnoses a CSV file to find rows with more columns than the header.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            header_line = csvfile.readline()
            # Manually split header to avoid issues with csv.reader state
            header = header_line.strip().split(',')
            expected_columns = len(header)
            print(f"Header has {expected_columns} columns.")
            print("-" * 20)
            
            malformed_row_count = 0
            
            # Reset file pointer and use csv.reader for robust parsing
            csvfile.seek(0)
            next(csvfile) # Skip header row for the reader
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader, 2): # Start from line 2
                if not row:
                    continue
                
                actual_columns = len(row)
                if actual_columns > expected_columns:
                    malformed_row_count += 1
                    print(f'\n[Row {i}] Found {actual_columns} columns (expected {expected_columns}).')
                    print(f'  - Full Row Data: {row}')
                    extra_data = row[expected_columns:]
                    print(f"  - Extra Data: {extra_data}")

            print(f"\n----------------------------------------")
            print(f"Diagnosis complete.")
            print(f"Found {malformed_row_count} rows with more columns than the header.")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        diagnose_csv(sys.argv[1])
    else:
        print("Usage: python3 diagnose_csv.py <path_to_csv_file>", file=sys.stderr)
