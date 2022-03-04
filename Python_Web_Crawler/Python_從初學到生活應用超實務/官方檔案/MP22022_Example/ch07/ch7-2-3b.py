import pandas as pd

df = pd.read_json("fruits.json")
print(df)

print(df.index)
print(df.columns)
print(df.values)

print(df.values[2])
print(df.values[1][2])