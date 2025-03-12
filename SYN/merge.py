import os
import pandas as pd

# Define the directory containing the CSV files
directory = "SONGS_CSV"

# List all CSV files in the directory
csv_files = [f for f in os.listdir(directory) if f.endswith(".csv")]

# Read and concatenate all CSV files
df_list = [pd.read_csv(os.path.join(directory, file)) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Save the merged CSV file
combined_df.to_csv("merged_songs.csv", index=False)

print(f"Merged {len(csv_files)} CSV files into 'merged_songs.csv'.")
