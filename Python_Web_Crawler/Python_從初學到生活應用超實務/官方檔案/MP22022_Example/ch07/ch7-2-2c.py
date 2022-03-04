import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
df = pd.DataFrame(fruits)
df.to_csv("fruits.csv",index=False,encoding="utf8")
df.to_json("fruits.json")
