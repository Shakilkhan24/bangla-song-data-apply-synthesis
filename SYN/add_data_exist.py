from datasets import load_dataset, Dataset
import pandas as pd

# Load existing dataset from Hugging Face
ds = load_dataset("Shakil2448868/bangla-songs-synthetic-prompt")

# Convert to pandas DataFrame
df_existing = ds['train'].to_pandas()

# Load new data
new_data_path = "merged_songs.csv"  # Change to your new CSV file path
df_new = pd.read_csv(new_data_path)

# Combine datasets
df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# Convert back to Hugging Face Dataset
combined_dataset = Dataset.from_pandas(df_combined)

# Push updated dataset to Hub
combined_dataset.push_to_hub("Shakil2448868/bangla-songs-synthetic-prompt")