import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}
df = pd.DataFrame(fruits)
cites = ["台北","新北","台中","高雄"]
df.columns = ["banana", "orange", "apple"]
cites[2] = "桃園"
df.index = cites
print(df)
