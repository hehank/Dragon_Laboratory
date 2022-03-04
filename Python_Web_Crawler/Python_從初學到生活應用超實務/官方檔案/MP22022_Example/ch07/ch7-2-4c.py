import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
cites = ["台北","新北","台中","高雄"]
df = pd.DataFrame(fruits, index=cites)
print(df)

print(df.iloc[3])

print(df.iloc[2:4, 1:3])
