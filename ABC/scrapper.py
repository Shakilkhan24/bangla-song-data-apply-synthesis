import os
from docx import Document
import re
import pandas as pd
from pathlib import Path

class SongScraper:
    def __init__(self, base_directory):
        self.base_dir = Path(base_directory)
        
    def extract_songs_from_folder(self, folder_path):
        folder_path = Path(folder_path)
        files = list(folder_path.rglob('*.docx'))
        
        writers = []
        titles = []
        songs = []
        
        writer_name = folder_path.name  # Get writer name from folder name
        
        for file in files:
            match = re.match(r'(?:song\d+_)?(.+?)\.docx', file.name, re.IGNORECASE)
            if match:
                title = match.group(1).replace('_', ' ').title()
                
                try:
                    doc = Document(file)
                    content = '\n\n'.join([para.text.strip() for para in doc.paragraphs if para.text.strip()])
                    
                    writers.append(writer_name)
                    titles.append(title)
                    songs.append(content)
                    
                    print(f"Processed: {file.name}")
                except Exception as e:
                    print(f"Error processing {file.name}: {str(e)}")
        
        return pd.DataFrame({
            'Writer': writers,
            'Title': titles,
            'Song': songs
        })
    
    def process_writer_folder(self, folder_name):
        folder_path = self.base_dir / folder_name
        
        if not folder_path.exists():
            raise FileNotFoundError(f"Writer folder not found: {folder_path}")
            
        songs_df = self.extract_songs_from_folder(folder_path)
        
        # Save to CSV using writer's name
        csv_path = self.base_dir / f"{folder_name}_songs.csv"
        songs_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"\nSaved {len(songs_df)} songs to {csv_path}")
        
        return songs_df

if __name__ == "__main__":
    try:
        # Get the absolute path of the script's directory
        base_directory = Path(__file__).parent  # Automatically gets the ABC directory
        
        # Initialize scraper
        scraper = SongScraper(base_directory)
        
        # List of writer folders to process
        writer_folders = ["Abdul Hai Al Hadi"]  # Add more writer folders here
        
        for folder in writer_folders:
            print(f"\nProcessing {folder}...")
            try:
                songs_df = scraper.process_writer_folder(folder)
                print(f"\nPreview for {folder}:")
                print(songs_df.head())
            except FileNotFoundError as e:
                print(f"Skipping {folder}: {str(e)}")
            except Exception as e:
                print(f"Error processing {folder}: {str(e)}")
            
    except Exception as e:
        print(f"Error: {str(e)}")