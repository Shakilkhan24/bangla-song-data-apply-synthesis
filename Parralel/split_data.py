import pandas as pd
import os
import numpy as np 
df=pd.read_csv('medical-o1.csv')


# Number of parts to split into
N = 3 # Change this to the number of parts you want

# Create output folder (optional)
os.makedirs("medical_spilits", exist_ok=True)

# Split the DataFrame
dfs = np.array_split(df, N)

# Save each part as a separate CSV
for i, split_df in enumerate(dfs, start=1):
    split_df.to_csv(f"medical_spilits/csv_{i}.csv", index=False)

print(f"Dataset split into {N} parts and saved in 'csv_splits' folder.")
