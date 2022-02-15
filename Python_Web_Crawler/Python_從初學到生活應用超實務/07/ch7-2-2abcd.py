#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

data = [[4, 0, 1],
        [3, 4, 5],
        [1, 6, 2],
        [0, 2, 4]]

cities = ['台北', '新北', '台中', '高雄']
fruits = ['蘋果', '香蕉', '橘子']

df = pd.DataFrame(data, index=cities, columns=fruits)
print(df)
print()

# TODO: Change columns
df.columns = ['Banana', 'Orange', 'Apple']

# TODO: Change index
cities[2] = '桃園'
df.index = cities

print(df)
print()

# TODO: 匯出 DataFrame 物件
# ? index = False => 不寫入 index
df.to_csv("./Python_Web_Crawler/Python_從初學到生活應用超實務/07/fruits.csv", index=False,
          encoding="utf-8")

# ? force_ascii=False => 取消強制轉換成 ascii
df.to_json("./Python_Web_Crawler/Python_從初學到生活應用超實務/07/fruits.json",
           force_ascii=False)

#  TODO: 匯入 DataFrame 物件
df1 = pd.read_csv("./Python_Web_Crawler/Python_從初學到生活應用超實務/07/fruits.csv",
                  encoding="utf-8")
df1.index = cities
print(df1)
print()

df2 = pd.read_json("./Python_Web_Crawler/Python_從初學到生活應用超實務/07/fruits.json",)
print(df2)
