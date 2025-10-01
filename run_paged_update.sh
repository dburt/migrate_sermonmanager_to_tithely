#!/bin/bash

# This script runs the Tithely sermon update process one page at a time
# for a specified range, making the process more robust to interruptions.

START=3
END=20

for i in $(seq $START $END)
do
  echo "--------------------------------------------------"
  echo "Processing Page $i of $END"
  echo "--------------------------------------------------"
  ./tithely_metadata_update/selective_importer.py --live-update --delay 2 --start-page $i --end-page $i
done

echo "--------------------------------------------------"
echo "All pages processed successfully."
echo "--------------------------------------------------"
