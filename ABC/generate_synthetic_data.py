import pandas as pd
from pathlib import Path
from google import genai
import time
from client import client

# Define the base prompt
BASE_PROMPT = """Translate into bangla language
text: 
{}

"""

def generate_prompt(song_text):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=BASE_PROMPT.format(song_text)
        )
        return response.text
    except Exception as e:
        print(f"Error generating prompt: {str(e)}")
        return None

def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if syn_prompt column already exists
    if 'syn_prompt' in df.columns:
        print("syn_prompt column already exists. Skipping file.")
        return
    
    # Add new column for prompts
    df['syn_prompt'] = None
    
    # Process each song
    for index, row in df.iterrows():
        print(f"Processing song {index + 1}/{len(df)}: {row['Title']}")
        prompt = generate_prompt(row['Song'])
        df.at[index, 'syn_prompt'] = prompt
        
        # Add delay to avoid rate limiting
        time.sleep(1)
    
    # Save the updated CSV (overwrite the original file)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print(f"\nUpdated file saved to: {file_path}")

def process_single_csv():
    # Get the CSV file path from user input
    csv_file = input("Enter the CSV file name (e.g., Abdul_Alim_songs.csv): ").strip()
    file_path = Path(__file__).parent / csv_file
    
    # Check if file exists
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    # Process the CSV file
    process_csv(file_path)

if __name__ == "__main__":
    process_single_csv() 
    # after running this file, add the csv file like SONGS_CSV/abdul alim_song.csv
    
    
    
    
 