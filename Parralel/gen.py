import pandas as pd
from pathlib import Path
from google import genai
import time
from client import client
import argparse

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
    
    # Check if translated columns already exist
    if 'Question_bn' in df.columns or 'Complex_CoT_bn' in df.columns or 'Response_bn' in df.columns:
        print("Translated columns already exist. Skipping file.")
        return
    
    # Add new columns for translations
    df['Question_bn'] = None
    df['Complex_CoT_bn'] = None
    df['Response_bn'] = None
    
    # Process each row
    for index, row in df.iterrows():
        print(f"Processing row {index + 1}/{len(df)}")
        
        # Translate each column
        try:
            df.at[index, 'Question_bn'] = generate_prompt(row['Question'])
            time.sleep(1)  # Add delay between API calls
            df.at[index, 'Complex_CoT_bn'] = generate_prompt(row['Complex_CoT'])
            time.sleep(1)
            df.at[index, 'Response_bn'] = generate_prompt(row['Response'])
            time.sleep(1)
        except Exception as e:
            print(f"Error processing row {index + 1}: {str(e)}")
            continue
    
    # Save the updated CSV (overwrite the original file)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print(f"\nUpdated file saved to: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Process CSV files")
    parser.add_argument('csv_file', type=str, help='CSV file to process')
    args = parser.parse_args()
    
    file_path = Path(__file__).parent / args.csv_file
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    process_csv(file_path)

if __name__ == "__main__":
    main() 
    
    
    
    
  