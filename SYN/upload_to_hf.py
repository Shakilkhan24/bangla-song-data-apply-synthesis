from datasets import load_dataset, DatasetDict
from huggingface_hub import HfApi

# Load your CSV file
dataset = load_dataset("csv", data_files="Rabindra Nath Tagore_songs.csv")

repo_name = "Shakil2448868/bangla-rabindranath-songs-synth_prompts"

dataset.push_to_hub(repo_name)

print(f"Dataset uploaded to https://huggingface.co/datasets/{repo_name}")
