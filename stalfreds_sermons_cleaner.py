import pandas as pd
import re
import requests
import json
import html
from datetime import datetime

# --- Configuration ---
# Create a dummy CSV file for the script to run
csv_data = """post_id,title,post_date_gmt,permalink,status,guid,content_html,content_text,preacher,sermon_series,service_type,bible_book,sermon_topics,audio_url,bible_passage,view_count
980,Fishing at Dawn,2011-09-17 14:00:00,https://stalfreds.org/sermons/fishing-at-dawn/,private,http://stalfreds.org/?post_type=wpfc_sermon&p=980,"Our special guest speaker is Ken Fish who has been at St Alfred's over the weekend speaking at the New Wine Conference.

Ken first visited and spoke at St Alfred's in Nov 1994 so it is a pleasure to welcome him back after all these years.

10 AM Service","Our special guest speaker is Ken Fish who has been at St Alfred's over the weekend speaking at the New Wine Conference.

Ken first visited and spoke at St Alfred's in Nov 1994 so it is a pleasure to welcome him back after all these years.

10 AM Service",,Standalone Sermon,,,,http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-09-18-10-FishingAtDawn.mp3,John 21: 1-14,35
1046,How You Can Be Fit For God's Work,2006-01-21 14:00:00,https://stalfreds.org/sermons/how-you-can-be-fit-for-gods-work/,publish,http://stalfreds.org/?post_type=wpfc_sermon&p=1046,Bible Text: 2 Timothy 2:14-26 | Preacher: Andrew Grills | Series: Standalone Sermon,Bible Text: 2 Timothy 2:14-26 | Preacher: Andrew Grills | Series: Standalone Sermon,Andrew Grills,Standalone Sermon,Sundays at 10am,,,http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060122-10.mp3,2 Timothy 2:14-26,50
27430,Wrath & Reconciliation - S@10,2024-02-03 23:00:10,https://stalfreds.org/sermons/wrath-reconciliation-s10/,publish,https://stalfreds.org/sermons/,,,Ben Clements,From Vice to Virtue,Sundays at 10am,eph,,http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-02-04-10-WrathAndReconciliation.mp3,Genesis 4:1-16; Ephesians 4:29-32,72
"""
with open('sermons.csv', 'w') as f:
    f.write(csv_data)


INPUT_CSV_PATH = 'sermons.csv'
OUTPUT_CSV_PATH = 'cleaned_sermons.csv'
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma:7b"

# --- Bible Book Standardization ---
BIBLE_BOOK_MAP = {
    'Gen': 'Genesis', 'Exo': 'Exodus', 'Lev': 'Leviticus', 'Num': 'Numbers', 'Deut': 'Deuteronomy',
    'Josh': 'Joshua', 'Judg': 'Judges', 'Ruth': 'Ruth', '1 Sam': '1 Samuel', '2 Sam': '2 Samuel',
    '1 Kgs': '1 Kings', '2 Kgs': '2 Kings', '1 Chr': '1 Chronicles', '2 Chr': '2 Chronicles',
    'Ezra': 'Ezra', 'Neh': 'Nehemiah', 'Esth': 'Esther', 'Job': 'Job', 'Ps': 'Psalm', 'Prov': 'Proverbs',
    'Eccl': 'Ecclesiastes', 'Song': 'Song of Solomon', 'Isa': 'Isaiah', 'Jer': 'Jeremiah',
    'Lam': 'Lamentations', 'Ezek': 'Ezekiel', 'Dan': 'Daniel', 'Hos': 'Hosea', 'Joel': 'Joel',
    'Amos': 'Amos', 'Obad': 'Obadiah', 'Jonah': 'Jonah', 'Mic': 'Micah', 'Nah': 'Nahum',
    'Hab': 'Habakkuk', 'Zeph': 'Zephaniah', 'Hag': 'Haggai', 'Zech': 'Zechariah', 'Mal': 'Malachi',
    'Matt': 'Matthew', 'Mt': 'Matthew', 'Mark': 'Mark', 'Luke': 'Luke', 'John': 'John', 'Acts': 'Acts',
    'Rom': 'Romans', '1 Cor': '1 Corinthians', '2 Cor': '2 Corinthians', 'Gal': 'Galatians',
    'Eph': 'Ephesians', 'Phil': 'Philippians', 'Col': 'Colossians', '1 Thess': '1 Thessalonians',
    '2 Thess': '2 Thessalonians', '1 Tim': '1 Timothy', '2 Tim': '2 Timothy', 'Titus': 'Titus',
    'Phlm': 'Philemon', 'Heb': 'Hebrews', 'Jas': 'James', '1 Pet': '1 Peter', '2 Pet': '2 Peter',
    '1 John': '1 John', '2 John': '2 John', '3 John': '3 John', 'Jude': 'Jude', 'Rev': 'Revelation',
    'Psalms': 'Psalm'
}

# --- LLM Interaction ---
def call_gemma(prompt):
    """Calls the local Ollama API to get a response from the Gemma model."""
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return "" # Return empty string on failure

# --- Helper Functions for Deterministic Cleaning ---

def clean_html(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return text.replace('\xa0', ' ').strip()

def standardize_bible_passage(passage):
    if not isinstance(passage, str) or not passage.strip():
        return ""
    
    passage = passage.strip().replace('&', 'and')

    range_match = re.match(r'(\d*\s*[A-Za-z]+)\s*(\d+)\s*[-&]\s*(\d+)', passage)
    if range_match:
        book, start_chap, end_chap = range_match.groups()
        return f"{book.strip()} {start_chap}-{end_chap}"

    list_match = re.match(r'(\d*\s*[A-Za-z]+\s*\d+:)(\d+,\s*\.?\d+-\d+)', passage)
    if list_match:
        return f"{list_match.group(1)}{list_match.group(2).replace(' .', ' ')}"
    
    book_pattern = r'|'.join(sorted(BIBLE_BOOK_MAP.keys(), key=len, reverse=True))
    book_regex = re.compile(f'^({book_pattern})', re.IGNORECASE)
    
    match = book_regex.match(passage)
    if match:
        short_book = match.group(1)
        for key, value in BIBLE_BOOK_MAP.items():
            if key.lower() == short_book.lower():
                long_book = value
                break
        passage = long_book + passage[len(short_book):]

    passage = re.sub(r'\s*:\s*', ':', passage)
    passage = re.sub(r'\s*-\s*', '-', passage)
    
    return passage.strip()

def extract_bible_book(passage):
    if not isinstance(passage, str):
        return ""
    match = re.match(r'^\d*\s*[A-Za-z]+', passage)
    if match:
        book_name = match.group(0).strip()
        if any(book_name in val for val in BIBLE_BOOK_MAP.values()):
            return book_name
    return ""

def parse_date_from_audio_url(url):
    if not isinstance(url, str):
        return None
    match1 = re.search(r'(\d{4}-\d{2}-\d{2})', url)
    if match1:
        return pd.to_datetime(match1.group(1), errors='coerce')
    match2 = re.search(r'Sermon(\d{6})', url)
    if match2:
        return pd.to_datetime(match2.group(1), format='%y%m%d', errors='coerce')
    return None

def clean_title(title):
    if not isinstance(title, str):
        return ""
    return re.sub(r'\s*-\s*\d+am|\s*-\s*\d+pm|\(S@\d+\)|- S@\d+$|-\s*S@\d+', '', title, flags=re.IGNORECASE).strip()

def standardize_service_type(row):
    title = str(row['title']).lower()
    url = str(row['audio_url']).lower()
    service = str(row['service_type']).lower()

    if '6pm' in title or '-18-' in url or '-6.mp3' in url or 's@6' in title:
        return 'Sundays at 6pm'
    if '10am' in title or '-10-' in url or '10l.mp3' in url:
        return 'Sundays at 10am'
    if 'talk' in service or 'men' in service or 'women' in service or 'breakfast' in url or 'event' in url:
        return 'Talks'
    if 'online' in title:
        return 'Online Service'
    if 'st luke' in service:
        return "St Luke's Sundays at 9:30am"
    if 'other' in service:
        return 'Other Services'
        
    return 'Sundays at 10am'

def infer_sermon_topics(row):
    if pd.notna(row['sermon_topics']) and row['sermon_topics']:
        return row['sermon_topics']
    
    prompt = f"""
    You are an expert theological archivist. Your task is to generate relevant sermon topics.
    Based on the following sermon information, suggest up to three comma-separated topics.
    Focus on key theological themes. Examples: Faith, Grace, Redemption, Discipleship, Easter, Christmas.
    If the information is insufficient, return an empty string.
    Output ONLY the comma-separated topics and nothing else.

    Title: "{row['title']}"
    Bible Passage: "{row['bible_passage']}"
    Series: "{row['sermon_series']}"

    TOPICS:
    """
    return call_gemma(prompt)

def infer_sermon_series(row):
    if pd.notna(row['sermon_series']) and row['sermon_series'] not in ['Standalone Sermon', '']:
        return row['sermon_series']
        
    book = row.get('bible_book', '')
    if book and book in BIBLE_BOOK_MAP.values():
        return book

    prompt = f"""
    You are a church archivist creating sermon series. Given the sermon title and bible book, suggest a concise series name.
    If the book is present, the series name should usually be the book name (e.g., "Genesis", "Mark").
    If the title suggests a theme (e.g., "Advent", "Easter"), use that.
    If it's truly a one-off sermon, respond with "Standalone Sermon".
    Respond with ONLY the series name.

    Title: "{row['title']}"
    Bible Book: "{row['bible_book']}"
    
    SERIES NAME:
    """
    return call_gemma(prompt)

def main():
    print("Loading CSV data...")
    try:
        df = pd.read_csv(INPUT_CSV_PATH)
    except FileNotFoundError:
        print(f"Error: '{INPUT_CSV_PATH}' not found. Please save your data in this file.")
        return

    print("Step 1: Initial deterministic cleaning...")
    df['content_text'] = df['content_text'].astype(str).apply(clean_html)
    df['title'] = df['title'].astype(str).apply(clean_title)
    df['permalink'] = df['permalink'].str.replace('/?p=', '/sermons/', regex=False)
    df['guid'] = df.apply(lambda row: row['permalink'] if '?' in str(row['guid']) else row['guid'], axis=1)

    print("Step 2: Correcting sermon dates from audio URLs...")
    df['sermon_date_from_url'] = df['audio_url'].apply(parse_date_from_audio_url)
    df['post_date_gmt'] = pd.to_datetime(df['post_date_gmt'], errors='coerce')
    df['sermon_date'] = df['sermon_date_from_url'].fillna(df['post_date_gmt'])
    df['post_date_gmt'] = df['sermon_date'].dt.strftime('%Y-%m-%d %H:%M:%S').fillna('')
    df.drop(columns=['sermon_date_from_url', 'sermon_date'], inplace=True)

    print("Step 3: Extracting and filling missing data from content...")
    for index, row in df.iterrows():
        content = row['content_text']
        if pd.isna(row['preacher']) or not row['preacher']:
            match = re.search(r'Preacher:\s*([^|]+)', content, re.IGNORECASE)
            if match:
                df.at[index, 'preacher'] = match.group(1).strip()

        if pd.isna(row['sermon_series']) or not row['sermon_series']:
            match = re.search(r'Series:\s*([^|]+)', content, re.IGNORECASE)
            if match:
                df.at[index, 'sermon_series'] = match.group(1).strip()
        
        if pd.isna(row['bible_passage']) or not row['bible_passage']:
            match = re.search(r'Bible Text:\s*([^|]+)', content, re.IGNORECASE)
            if match:
                df.at[index, 'bible_passage'] = match.group(1).strip()

    print("Step 4: Standardizing Bible passages and extracting book names...")
    df['bible_passage'] = df['bible_passage'].astype(str).apply(standardize_bible_passage)
    df['bible_book'] = df['bible_passage'].apply(extract_bible_book)
    
    print("Step 5: Standardizing service types...")
    df['service_type'] = df.apply(standardize_service_type, axis=1)
    
    print("Step 6: Using LLM to infer sermon series for standalone sermons...")
    series_mask = (df['sermon_series'].str.contains('Standalone Sermon', case=False, na=True)) | (df['sermon_series'].isna()) | (df['sermon_series'] == '')
    if not df[series_mask].empty:
        df.loc[series_mask, 'sermon_series'] = df.loc[series_mask].apply(infer_sermon_series, axis=1)

    print("Step 7: Using LLM to infer missing sermon topics...")
    topic_mask = (df['sermon_topics'].isna()) | (df['sermon_topics'] == '')
    if not df[topic_mask].empty:
        df.loc[topic_mask, 'sermon_topics'] = df.loc[topic_mask].apply(infer_sermon_topics, axis=1)
    
    print("Step 8: Finalizing and saving...")
    df.drop(columns=['content_html', 'content_text'], inplace=True, errors='ignore')
    
    final_columns = [
        'post_id', 'title', 'post_date_gmt', 'permalink', 'status', 'guid', 
        'preacher', 'sermon_series', 'service_type', 'bible_book', 
        'sermon_topics', 'audio_url', 'bible_passage', 'view_count'
    ]
    df = df[final_columns]
    
    str_cols = ['preacher', 'sermon_series', 'bible_book', 'sermon_topics', 'bible_passage']
    for col in str_cols:
        df[col] = df[col].fillna('').astype(str).str.strip()

    df.to_csv(OUTPUT_CSV_PATH, index=False)

    print(f"\nProcessing complete! Cleaned data saved to '{OUTPUT_CSV_PATH}'.")
    print("\n--- First 5 rows of cleaned data ---")
    print(df.head())

if __name__ == '__main__':
    main()
