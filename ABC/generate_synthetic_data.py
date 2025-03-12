import pandas as pd
from pathlib import Path
from google import genai
import time
from client import client

# Define the base prompt
BASE_PROMPT = """Suppose you are a specialist writer and singer, and You are asked to create a creative prompt to generate the song in bangla languge. 
গানঃ 
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

def process_all_csvs(folder_path):
    # Get all CSV files in the folder
    csv_files = list(folder_path.glob("*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {folder_path}")
        return
    
    print(f"Found {len(csv_files)} CSV files to process")
    
    # Process each CSV file
    for i, csv_file in enumerate(csv_files):
        print(f"\nProcessing file {i + 1}/{len(csv_files)}: {csv_file.name}")
        process_csv(csv_file)
        print(f"Completed processing {csv_file.name}")

def main():
    # Get the folder path
    folder_name = input("Enter the folder name containing CSV files (e.g., SONGS_CSV): ").strip()
    folder_path = Path(__file__).parent / folder_name
    
    # Check if folder exists
    if not folder_path.exists():
        print(f"Folder not found: {folder_path}")
        return
    
    # Process all CSV files
    process_all_csvs(folder_path)

if __name__ == "__main__":
    main() 
    
