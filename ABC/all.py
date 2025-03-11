import pandas as pd
from pathlib import Path

def merge_csv_files():
    # Get all CSV files matching 100_*.csv in the current directory
    csv_files = sorted(Path(".").glob("100_*.csv"))
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return
    
    # Read and concatenate all CSV files
    df_list = [pd.read_csv(file) for file in csv_files]
    merged_df = pd.concat(df_list, ignore_index=True)
    
    # Save the merged DataFrame
    output_file = "added_csv.csv"
    merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Merged CSV saved as {output_file}")

# Run the function
merge_csv_files()
