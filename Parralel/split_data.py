from datasets import load_dataset
import pandas as pd
import os
import numpy as np 
# Load dataset
ds = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT", "en",split='train')
df = pd.DataFrame(ds)

# Number of parts to split into
N = 60 # Change this to the number of parts you want

# Create output folder (optional)
os.makedirs("csv_splits", exist_ok=True)

# Split the DataFrame
dfs = np.array_split(df, N)

# Save each part as a separate CSV
for i, split_df in enumerate(dfs, start=1):
    split_df.to_csv(f"csv_splits/csv_{i}.csv", index=False)

print(f"Dataset split into {N} parts and saved in 'csv_splits' folder.")
