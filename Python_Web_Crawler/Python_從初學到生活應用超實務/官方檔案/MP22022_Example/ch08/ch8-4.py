import pandas as pd

df = pd.read_csv("2330.TW.csv", encoding="utf8")
print(df.info())
df = df.dropna()
print(df.head())





