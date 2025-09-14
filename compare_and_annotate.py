
import pandas as pd
import json

def compare_and_annotate():
    # Load the master CSV file
    try:
        master_df = pd.read_csv('sermons_cleaned_v2.csv')
    except FileNotFoundError:
        print("Error: sermons_cleaned_v2.csv not found.")
        return

    # Load the Tithely sermon index
    try:
        with open('sermon_index.json', 'r') as f:
            sermon_index = json.load(f)
    except FileNotFoundError:
        print("Error: sermon_index.json not found.")
        return

    # Create a DataFrame from the sermon index
    tithely_df = pd.DataFrame(sermon_index)

    # --- Identify Missing Sermons ---
    master_post_ids = set(master_df['post_id'].astype(int))
    tithely_post_ids = set(tithely_df['post_id'].dropna().astype(int))

    missing_post_ids = list(master_post_ids - tithely_post_ids)

    with open('missing_post_ids.txt', 'w') as f:
        for post_id in missing_post_ids:
            f.write(f"{post_id}\n")

    print(f"Found {len(missing_post_ids)} missing sermons. Their post_ids are saved in missing_post_ids.txt")

    # --- Compare and Annotate ---
    annotated_sermons = []
    for sermon in sermon_index:
        post_id = sermon.get('post_id')
        if post_id and not pd.isna(post_id):
            master_sermon = master_df[master_df['post_id'] == int(post_id)]
            if not master_sermon.empty:
                master_sermon = master_sermon.iloc[0]
                discrepancies = {}

                # Compare title
                if sermon.get('title') != master_sermon.get('title'):
                    discrepancies['title'] = {
                        'tithely': sermon.get('title'),
                        'master': master_sermon.get('title')
                    }

                # Compare speaker/preacher
                if sermon.get('speaker') != master_sermon.get('preacher'):
                    discrepancies['speaker'] = {
                        'tithely': sermon.get('speaker'),
                        'master': master_sermon.get('preacher')
                    }

                # Compare series
                if sermon.get('sermon_series') != master_sermon.get('sermon_series'):
                    discrepancies['sermon_series'] = {
                        'tithely': sermon.get('sermon_series'),
                        'master': master_sermon.get('sermon_series')
                    }
                
                # Compare bible_passage
                if sermon.get('bible_passage') != master_sermon.get('bible_passage'):
                    discrepancies['bible_passage'] = {
                        'tithely': sermon.get('bible_passage'),
                        'master': master_sermon.get('bible_passage')
                    }

                if discrepancies:
                    sermon['discrepancies'] = discrepancies
        
        annotated_sermons.append(sermon)

    # Save the annotated sermon index
    with open('sermon_index_annotated.json', 'w') as f:
        json.dump(annotated_sermons, f, indent=4)

    print("Created annotated sermon index: sermon_index_annotated.json")

if __name__ == "__main__":
    compare_and_annotate()
