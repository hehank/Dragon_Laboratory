import pandas as pd

df = pd.read_csv("Youbike.csv", encoding="utf8")
df = df[["sna", "tot", "sbi", "bemp"]]
print(df.head())
print(df.info())
df["sbi/tot"] = df["sbi"] / df["tot"]
print(df.head())
df["bemp/tot"] = df["bemp"] / df["tot"]
print(df.head())