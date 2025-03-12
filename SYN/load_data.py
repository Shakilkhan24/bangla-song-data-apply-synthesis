from datasets import load_dataset
import pandas as pd
ds = load_dataset("ajibawa-2023/Children-Stories-Collection",split='train')
df=pd.DataFrame(ds)

df.to_csv('stories.csv', index=False) 