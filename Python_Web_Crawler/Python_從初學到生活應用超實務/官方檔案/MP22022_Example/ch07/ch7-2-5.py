import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
cites = ["台北","新北","台中","高雄"]
df = pd.DataFrame(fruits, index=cites)
print(df)

df.loc["新北", "香蕉"] = 9
df.iloc[1,2] = 8
print(df)

r = [5, 5, 5] 
df.loc["台中"] = r
print(df)

s = [0, 0, 0, 0]
df.loc[ : , "香蕉"] = s
print(df)