import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
cites = ["台北","新北","台中","高雄"]
df = pd.DataFrame(fruits, index=cites)
print(df)

print(df.loc["台北"])
print(df.loc[["台北","台中"]])

print(df.loc["台北", "香蕉"])
print(df.loc[["台中","高雄"], ["橘子","香蕉"]])

print(df.loc[:, ["橘子","香蕉"]])

print(df.loc["新北":"台中", "蘋果":"香蕉"])