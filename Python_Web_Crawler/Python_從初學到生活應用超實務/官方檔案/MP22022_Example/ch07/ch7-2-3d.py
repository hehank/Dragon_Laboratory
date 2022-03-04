import pandas as pd

df = pd.read_json("fruits.json")
print(df)

print(df.info())
