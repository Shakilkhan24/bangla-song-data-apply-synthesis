import pandas as pd

# CSV ফাইল লোড করা (প্রথম লাইনে কোনো হেডার নেই, তাই header=None ব্যবহার করছি)
df = pd.read_csv("csv_1.csv", header=None)

# কলামের নাম সেট করা
df.columns = ["word"]  # আপনি ইচ্ছেমতো নাম দিতে পারেন

# পরিবর্তন সংরক্ষণ করা
df.to_csv("csv_1.csv", index=False)

# পরিবর্তিত DataFrame দেখানো
print(df.head())
