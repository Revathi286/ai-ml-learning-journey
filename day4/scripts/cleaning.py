import pandas as pd

df = pd.read_csv("../data/data.csv")

print("Missing Values:\n", df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Score'] = df['Score'].fillna(0)

print("\nCleaned Data:\n", df)