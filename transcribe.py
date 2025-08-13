#!/usr/bin/env python

import json
import sys
import re
import os
import argparse
import random
from faster_whisper import WhisperModel

def sanitize_filename(title):
    """Sanitizes a string to be a valid filename."""
    s = title.replace(" ", "_").replace(":", "-")
    s = re.sub(r'[\\/*?"<>|]', "", s)
    return s[:150] # Limit filename length for safety

def main(json_filepath, output_dir, sample_size, title_filter):
    """
    Processes sermons and transcribes audio files using Whisper.
    """
    print(f"Current Working Directory: {os.getcwd()}")
    absolute_path = os.path.abspath(json_filepath)
    print(f"Attempting to open JSON file at absolute path: {absolute_path}")

    if not os.path.exists(absolute_path):
        print(f"FATAL: File does not exist at the provided path.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(absolute_path, 'r', encoding='utf-8') as f:
            sermons = json.load(f)

        # --- Logic to select sermons ---
        sermon_sample = []
        if title_filter:
            sermon_sample = [s for s in sermons if s.get('title') == title_filter]
            if not sermon_sample:
                print(f"Error: No sermon found with the exact title '{title_filter}'", file=sys.stderr)
                return
        elif sample_size is not None:
            if sample_size > len(sermons):
                print(f"Warning: Sample size ({sample_size}) is larger than the number of sermons ({len(sermons)}). Processing all sermons.", file=sys.stderr)
                sermon_sample = sermons
            else:
                sermon_sample = random.sample(sermons, sample_size)
        else:
            sermon_sample = sermons
        
        print(f"Processing {len(sermon_sample)} sermon(s).")
        
        # --- Directory Setup ---
        os.makedirs(output_dir, exist_ok=True)
        temp_dir = os.path.join(output_dir, "temp_audio")
        os.makedirs(temp_dir, exist_ok=True)
        
        print(f"Transcripts will be saved in: ./{output_dir}")
        print("\nStarting transcription process...")
        print("---------------------------------")

        total_sermons = len(sermon_sample)
        for i, sermon in enumerate(sermon_sample, 1):
            audio_url = sermon.get('audio_url')
            title = sermon.get('title')
            date = sermon.get('post_date_gmt', 'nodate').split(' ')[0]
            
            print(f"\nProcessing sermon {i}/{total_sermons}: {title}")

            if audio_url and title:
                # Construct a more informative initial prompt for the current sermon
                current_sermon_prompt = f"The sermon title is: {title}."
                if sermon.get('series'):
                    current_sermon_prompt += f" Sermon series: {sermon['series']}."
                if sermon.get('preacher'):
                    current_sermon_prompt += f" Preacher: {sermon['preacher']}."
                if sermon.get('bible_passage'):
                    current_sermon_prompt += f" Bible passage: {sermon['bible_passage']}."

                # --- Create a descriptive filename ---
                clean_title = sanitize_filename(title)
                audio_ext = os.path.splitext(audio_url.split("?")[0])[-1]
                if not audio_ext or len(audio_ext) > 5:
                    audio_ext = ".mp3"
                
                temp_audio_filename = f"{date}_{clean_title}{audio_ext}"
                temp_audio_path = os.path.join(temp_dir, temp_audio_filename)
                transcript_path = os.path.join(output_dir, f"{date}_{clean_title}.txt")

                if os.path.exists(transcript_path):
                    print(f"--> Transcript already exists at {transcript_path}. Skipping.")
                    continue

                try:
                    # --- Download the audio file ---
                    print(f"  Downloading audio to: {temp_audio_path}")
                    download_command = ["curl", "-L", "-o", temp_audio_path, audio_url]
                    subprocess.run(download_command, check=True, capture_output=True)

                    # --- Transcribe the local audio file ---
                    print("  Starting transcription...")
                    try:
                        # Initialize Faster Whisper model (CPU optimized)
                        model = WhisperModel("medium", device="cpu", compute_type="int8")

                        # Transcribe the audio file
                        segments, info = model.transcribe(temp_audio_path, beam_size=5, language="en", initial_prompt=initial_prompt)

                        transcript_content = ""
                        for segment in segments:
                            transcript_content += segment.text + "\n"

                        # Save the transcript to a file
                        with open(transcript_path, "w", encoding="utf-8") as f:
                            f.write(transcript_content)

                        print(f"--> Transcription successful for: {title}")
                    except Exception as e:
                        print(f"--> Transcription FAILED for: {title}", file=sys.stderr)
                        print(f"    Error: {e}", file=sys.stderr)

                except subprocess.CalledProcessError as e:
                    print(f"--> Download FAILED for URL: {audio_url}", file=sys.stderr)
                    print(f"    Error: {e.stderr.decode() if e.stderr else 'Unknown'}", file=sys.stderr)
                finally:
                    # --- Clean up the temporary audio file ---
                    if os.path.exists(temp_audio_path):
                        os.remove(temp_audio_path)
                        print(f"  Cleaned up temporary file: {temp_audio_path}")

            else:
                print("--> Skipping due to missing audio URL or title.")

        print("\n---------------------------------")
        print("Transcription process complete.")

    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_filepath}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe sermon audio files using Whisper.')
    parser.add_argument('json_filepath', help='The path to the input sermons JSON file.')
    parser.add_argument('--output_dir', default='transcripts', help='The directory to save the transcript files.')
    parser.add_argument('--sample-size', type=int, help='Process a random sample of N sermons instead of the whole set.')
    parser.add_argument('--title', dest='title_filter', help='Transcribe a specific sermon by its exact title.')
    args = parser.parse_args()
    main(args.json_filepath, args.output_dir, args.sample_size, args.title_filter)
