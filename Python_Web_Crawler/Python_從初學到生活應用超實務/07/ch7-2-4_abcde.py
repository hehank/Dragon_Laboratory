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

# TODO: 使用欄位標籤選取單一或多個欄位
print("選取單一欄位：")
print(DF["香蕉"])
print()

print("選取多個欄位：")
print(DF[["蘋果", "橘子"]].head(3))
print()

# TODO: 使用索引標籤選取特定範圍的紀錄
print("DF[0:2]：")
print(DF[0:2])
print()

print("DF[\"台北\":\"台中\"]：")
print(DF["台北":"台中"])
print()

# TODO: 使用 loc 索引器選取資料
print("DF.loc[\"台北\"]：")
print(DF.loc["台北"])
print()

print("DF.loc[[\"台北\", \"台中\"]]：")
print(DF.loc[["台北", "台中"]])
print()

print("DF.loc[\"台北\", \"香蕉\"]：")
print(DF.loc["台北", "香蕉"])
print()

print("DF.loc[[\"台中\", \"高雄\"], [\"橘子\", \"香蕉\"]]：")
print(DF.loc[["台中", "高雄"], ["橘子", "香蕉"]])
print()

print("DF.loc[:, [\"橘子\", \"香蕉\"]]：")
print(DF.loc[:, ["橘子", "香蕉"]])
print()

print("DF.loc[\"新北\":\"台中\", \"蘋果\":\"香蕉\"]：")
print(DF.loc["新北":"台中", "蘋果":"香蕉"])
print()

# TODO: 使用 iloc 索引器選取資料
print("DF.iloc[3]：")
print(DF.iloc[3])
print()

print("DF.iloc[2:4, 1:3]：")
print(DF.iloc[2:4, 1:3])
print()

# TODO: 使用布林條件過濾資料和建立遮罩
print("只選擇香蕉大於 3 的地區：")
print(DF[DF.香蕉 > 3])
print()

print("使用布林條件建立相同形狀的遮罩(Mask)：")
DF2 = DF > 3
print(DF2)
print()

# TODO: 指定欄位標籤來排序紀錄資料
DF2 = DF.sort_values("香蕉", ascending=False)  # 大 -> 小
print(DF2)
