import pandas as pd

df1 = pd.read_csv("fruits.csv", encoding="utf8")
df2 = pd.read_json("fruits.json")
print(df1)
print(df2)