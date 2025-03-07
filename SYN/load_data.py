from datasets import load_dataset
import pandas as pd
ds = load_dataset("fka/awesome-chatgpt-prompts",split='train')
df=pd.DataFrame(ds)

df.to_csv('awesome_chatgpt_prompts.csv', index=False) 