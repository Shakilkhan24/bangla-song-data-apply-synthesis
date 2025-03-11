import pandas as pd
from pathlib import Path
import time
from client import client
from tqdm import tqdm

BASE_PROMPT = """প্রদত্ত শব্দটি ব্যবহার করে বাংলায় একটি অর্থবহ ও সুসংগঠিত অনুচ্ছেদ লিখুন, যেখানে অন্তত ১০টি বাক্য থাকবে।  
অনুচ্ছেদটি গল্প, বর্ণনা বা চিন্তাশীল কোনো প্রসঙ্গ নিয়ে হতে পারে।  

শব্দ:  
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

def process_csv(file_path, start_row, end_row):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Validate row range
    total_rows = len(df)
    if start_row < 0 or end_row > total_rows or start_row >= end_row:
        print(f"Invalid row range! CSV contains {total_rows} rows.")
        return
    
    # Select the specific range of rows
    df = df.iloc[start_row:end_row].copy()
    
    # Check if 'paragraph' column already exists
    if 'paragraph' in df.columns:
        print("'paragraph' column already exists. Skipping file.")
        return
    
    df['paragraph'] = None
    
    # Process in chunks of 100 rows
    batch_size = 100
    num_batches = (len(df) // batch_size) + (1 if len(df) % batch_size != 0 else 0)
    
    for batch_num in range(num_batches):
        start_idx = batch_num * batch_size
        end_idx = min(start_idx + batch_size, len(df))
        batch_df = df.iloc[start_idx:end_idx].copy()
        
        print(f"Processing batch {batch_num + 1} of {num_batches}...")
        for index, row in tqdm(batch_df.iterrows(), total=len(batch_df), desc=f"Batch {batch_num + 1}"):
            prompt = generate_prompt(row['word'])
            batch_df.at[index, 'paragraph'] = prompt
            
            # Add delay to avoid rate limiting
            time.sleep(1)
        
        # Save each batch separately
        output_filename = f"{file_path.stem}_batch__{batch_num + 1}.csv"
        batch_df.to_csv(output_filename, index=False, encoding='utf-8-sig')
        print(f"Batch {batch_num + 1} saved as {output_filename}")

def process_single_csv():
    csv_file = input("Enter the CSV file name (e.g., Abdul_Alim_songs.csv): ").strip()
    file_path = Path(__file__).parent / csv_file
    
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    try:
        start_row = int(input("Enter the starting row number: ").strip())
        end_row = int(input("Enter the ending row number: ").strip())
        process_csv(file_path, start_row, end_row)
    except ValueError:
        print("Invalid input! Please enter valid integers for row range.")

if __name__ == "__main__":
    process_single_csv()
