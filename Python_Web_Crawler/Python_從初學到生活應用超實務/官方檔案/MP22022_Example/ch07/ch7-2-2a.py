import pandas as pd

data = [ [4, 0, 1], 
         [3, 4, 5],
         [1, 6, 2],
         [0, 2, 4] ]
cites = ["台北","新北","台中","高雄"]
fruits = ["蘋果", "香蕉", "橘子"]
df = pd.DataFrame(data, index=cites, columns=fruits) 
print(df)
