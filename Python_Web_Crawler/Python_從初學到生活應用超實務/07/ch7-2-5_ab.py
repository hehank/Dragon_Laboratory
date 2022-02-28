#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]
          }

cities = ['台北', '新北', '台中', '高雄']

DF = pd.DataFrame(fruits, index=cities)
print(f"完整 DataFrame：\n{DF}")
print()

# TODO: 更新 DataFrame 資料
# ? 更新純量值
DF.loc["新北", "香蕉"] = 9
DF.iloc[1, 2] = 8
print(f"更新純量值：\n{DF}")
print()

# ? 更新單筆紀錄
r = [5, 5, 5]
DF.loc["台中"] = r
print(f"更新單筆紀錄：\n{DF}")
print()

# ? 更新整個欄位
s = [0, 0, 0, 0]
DF.loc[:, "香蕉"] = s
print(f"更新整個欄位：\n{DF}")
print()

# TODO: 刪除 DataFrame 資料
# ? 刪除純量值
DF.loc["台北", "橘子"] = None
DF.iloc[1, 2] = None
print(f"刪除純量值：\n{DF}")
print()

# ? 刪除單筆和多筆紀錄
DF2 = DF.drop(["新北", "高雄"])
print(f"刪除單筆：\n{DF2}")
print()

DF2 = DF2.drop(DF.index[[0, 2]])
print(f"刪除多筆紀錄：\n{DF2}")
print()

# ? 刪除整個欄位
DF2 = DF.drop(["橘子"], axis=1)
print(f"刪除整個欄位：\n{DF2}")

# TODO: 新增 DataFrame 資料
# ? 新增一筆紀錄
DF.loc["桃園"] = [6, 6, 6]
print(f"新增一筆紀錄：\n{DF}")
print()

# ? 新增整個欄位
DF["西瓜"] = [7, 7, 7, 7, 7]
print(f"新增整個欄位：\n{DF}")
