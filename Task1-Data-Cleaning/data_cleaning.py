import pandas as pd
df = pd.read_csv("dataset/netflix_titles.csv")

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

df = df.drop_duplicates()

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df['type'] = df['type'].str.upper()
df['date_added'] = pd.to_datetime(
    df['date_added'].str.strip(),
    errors='coerce'
)

print("\nData Types:")
print(df.dtypes)

import os
os.makedirs("cleaned_dataset", exist_ok=True)
df.to_csv(
    "cleaned_dataset/cleaned_netflix_data.csv",
    index=False
)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved in cleaned_dataset folder.")