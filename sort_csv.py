
import csv
import sys

def sort_csv(input_file, output_file):
    """Sorts a CSV file by the first column (post_id)."""
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            data = sorted(reader, key=lambda row: int(row[0]))

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(data)
        print(f"Successfully sorted {input_file} to {output_file}")

    except (IOError, csv.Error) as e:
        print(f"Error processing CSV file: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error converting post_id to integer: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    sort_csv('/home/akash/projects/stalfreds_podcast/sermons_cleaned.csv', '/home/akash/projects/stalfreds_podcast/sermons_sorted.csv')
