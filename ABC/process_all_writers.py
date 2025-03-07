from scrapper import SongScraper
from pathlib import Path

def process_all_writers():
    # Get the base directory (where the script is located)
    base_directory = Path(__file__).parent
    
    # Initialize the scraper
    scraper = SongScraper(base_directory)
    
    # Get all directories in the ABC folder
    writer_folders = [f for f in base_directory.iterdir() if f.is_dir()]
    
    # Exclude special directories
    excluded_folders = ['__pycache__']
    writer_folders = [f for f in writer_folders if f.name not in excluded_folders]
    
    # Process each writer folder
    for folder in writer_folders:
        try:
            print(f"\nProcessing {folder.name}...")
            songs_df = scraper.process_writer_folder(folder.name)
            print(f"\nPreview for {folder.name}:")
            print(songs_df.head())
        except FileNotFoundError as e:
            print(f"Skipping {folder.name}: {str(e)}")
        except Exception as e:
            print(f"Error processing {folder.name}: {str(e)}")

if __name__ == "__main__":
    process_all_writers() 