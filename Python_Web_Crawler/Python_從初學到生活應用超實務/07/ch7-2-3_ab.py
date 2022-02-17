#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

DF = pd.read_json("./Python_Web_Crawler/Python_從初學到生活應用超實務/07/fruits.json")

print(DF)
print()

# TODO: 顯示 DF 的前幾筆資料
print("顯示前 2 筆資料：")
print(DF.head(2))
print()

# TODO: 顯示 DF 的最後幾筆資料
print("顯示最後 3 筆資料：")
print(DF.tail(3))
print()

# TODO: 顯示 DF 的 Index(索引)
print("顯示 Index(索引)：")
print(DF.index)
print()

# TODO: 顯示 DF 的 Columns(欄位)
print("顯示 Columns(欄位)：")
print(DF.columns)
print()

# TODO: 顯示 DF 的 Values(資料)
print("顯示 Values(資料)：")
print(DF.values)
print()

# TODO: 顯示 DF 的部分資料
print("顯示第 3 筆資料：")
print(DF.values[2])
print()
print("顯示第 2 筆第 3 欄資料：")
print(DF.values[1][2])
print()

# TODO: 顯示 DF 的總資料數
print("顯示總資料數：")
print(len(DF))
print()

# TODO: 顯示 DF 的形狀
print("顯示形狀(列, 行)：")
print(DF.shape)
print()

# TODO: 顯示 DF 的摘要資訊
print("顯示摘要資訊：")
print(DF.info())
