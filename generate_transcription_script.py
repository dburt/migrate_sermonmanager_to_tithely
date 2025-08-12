import json
import sys
import re
import os
import argparse

def sanitize_filename(title):
    """Sanitizes a string to be a valid filename."""
    s = re.sub(r'[\\/*?_"<>|]', "", title)
    s = s.replace(' ', '_')
    s = s.replace(':', '-')
    return s[:100] # Limit filename length

def main(json_filepath, output_script_path):
    """
    Generates a shell script with whisper commands for each sermon audio file.
    """
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            sermons = json.load(f)

        output_dir = "transcripts"
        
        with open(output_script_path, 'w', encoding='utf-8') as script_f:
            script_f.write("#!/bin/bash\n")
            script_f.write("# This script was generated to transcribe all sermon audio files.\n")
            script_f.write("# It will download audio files and transcribe them using Whisper.\n\n")
            script_f.write(f"mkdir -p {output_dir}\n\n")

            for sermon in sermons:
                audio_url = sermon.get('audio_url')
                title = sermon.get('title')
                
                if audio_url and title:
                    clean_title = sanitize_filename(title)
                    # The output path for whisper is just the directory.
                    # Whisper will name the file based on the input audio file name.
                    command = f'whisper "{audio_url}" --model medium --output_dir "{output_dir}" --language English\n'
                    script_f.write(f"echo \"Transcribing: {title}\"\n")
                    script_f.write(command)
                    script_f.write("\n")

        os.chmod(output_script_path, 0o755)
        print(f"Successfully created and made executable the transcription script at: {output_script_path}")
        print("You can now review this file and run it when you are ready to start the transcription.")

    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_filepath}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a shell script to transcribe sermon audio files using Whisper.')
    parser.add_argument('json_filepath', help='The path to the input sermons JSON file.')
    parser.add_argument('output_script_path', help='The path to save the generated shell script.')
    args = parser.parse_args()
    main(args.json_filepath, args.output_script_path)
