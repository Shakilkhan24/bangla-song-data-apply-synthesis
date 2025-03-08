import argparse
from scrapper import SongScraper
from pathlib import Path

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Scrape songs from a writer's folder")
    parser.add_argument(
        'folder',
        type=str,
        help="Name of the writer's folder to process"
    )
    args = parser.parse_args()
    
    # Get the base directory (where the script is located)
    base_directory = Path(__file__).parent
    
    # Initialize the scraper
    scraper = SongScraper(base_directory)
    
    # Process the specified writer folder
    try:
        print(f"\nProcessing {args.folder}...")
        songs_df = scraper.process_writer_folder(args.folder)
        print(f"\nPreview for {args.folder}:")
        print(songs_df.head())
    except FileNotFoundError as e:
        print(f"\nError: {str(e)}")
        print("Please make sure:")
        print(f"1. The folder '{args.folder}' exists in the ABC directory")
        print(f"2. The folder contains .docx files")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main() 