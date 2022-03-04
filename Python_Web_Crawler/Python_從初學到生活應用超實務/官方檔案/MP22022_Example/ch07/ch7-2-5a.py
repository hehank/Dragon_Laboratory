import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
cites = ["台北","新北","台中","高雄"]
df = pd.DataFrame(fruits, index=cites)
print(df)

df.loc["台北", "橘子"] = None
df.iloc[1,2] = None
print(df)

df2 = df.drop(["新北", "高雄"])    # 2,4 筆
df2 = df2.drop(df.index[[0, 2]])   # 1,3 筆
print(df2)

df2 = df.drop(["橘子"], axis=1)
print(df2)