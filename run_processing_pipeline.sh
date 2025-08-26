#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Generate a timestamp for the output files
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
echo "Generated timestamp: ${TIMESTAMP}"

# Define file names
INPUT_CSV="sermons_cleaned_ai_studio.csv"
CLEANED_CSV="sermons_cleaned_${TIMESTAMP}.csv"
JSON_OUTPUT="sermons_${TIMESTAMP}.json"
RSS_OUTPUT="podcast_feed_${TIMESTAMP}.xml"

echo "Starting data processing pipeline..."

# Step 1: Clean the source CSV
echo "Step 1: Cleaning ${INPUT_CSV} -> ${CLEANED_CSV}"
cat "${INPUT_CSV}" | python3 clean_content_text.py > "${CLEANED_CSV}"

# Step 2: Convert cleaned CSV to JSON
echo "Step 2: Converting ${CLEANED_CSV} -> ${JSON_OUTPUT}"
uv run convert_csv_to_json.py "${CLEANED_CSV}" "${JSON_OUTPUT}"

# Step 3: Generate RSS feed from JSON
echo "Step 3: Generating ${JSON_OUTPUT} -> ${RSS_OUTPUT}"
uv run generate_rss_feed.py "${JSON_OUTPUT}" "${RSS_OUTPUT}"

echo ""
echo "----------------------------------------"
echo "Pipeline finished successfully!"
echo "New files created:"
echo "- ${CLEANED_CSV}"
echo "- ${JSON_OUTPUT}"
echo "- ${RSS_OUTPUT}"
echo "----------------------------------------"

# Step 4: Create a symlink to the latest JSON file
echo "Step 4: Creating symlink sermons.json -> ${JSON_OUTPUT}"
ln -sf "${JSON_OUTPUT}" sermons.json
