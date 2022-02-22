---
title: pandas
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/UdCwaYC4TqiswsUiD_7HZg/badge)](https://hackmd.io/UdCwaYC4TqiswsUiD_7HZg)

{%hackmd theme-dark %}

# Usage
```python=
import pandas as pd
```

# Series
```python=
pd.Series(data=None, index=None, dtype=None, name=None, options, ...)
```
- name：欄位名稱。

## 介紹
- 是一種一維的陣列資料結構。
- 陣列內可存放 int、str、float、Python object (例如：list、dict、...)、Numpy 的 ndarray、純量、...等。
- 看起來像二維陣列，因為一個是 data，一個是 index。
- 結構與 Python 的 list 類似。

## All Examples


# DataFrame
## 介紹
- 是一種二維的陣列資料結構。
- 可視為是類似 Excel 的工作表。
- 陣列內可存放 int、str、float、Python object (例如：list、dict、...)、Numpy 的 ndarray、純量、...等。

## .concat
```python=
pd.concat(obj, axis=0)
```
- obj：[Series1, Series2, ...] or [DataFrame1, DataFrame2, ...]
- axis：要連接的軸
    - 0 => index -> 預設
    - 1 => column(欄)

## .DataFrame
```python=
df = pd.DataFrame(data=None, index=None, dtype=None, name=None)
```
- index：行
- columns：列

### 匯出 DataFrame 物件
|方法|說明|
|---|----|
|df.to_csv(filename)|匯出成 CSV 格式的檔案|
|df.to_json(filename)|匯出成 JSON 格式的檔案|
|df.to_html(filename)|匯出成 HTML 表格標籤的檔案|
|df.to_excel(filename)|匯出成 Excel 檔案|

### 匯入 DataFrame 物件
|方法|說明|
|---|----|
|df.read_csv(filename)|匯入 CSV 格式的檔案|
|df.read_json(filename)|匯入 JSON 格式的檔案|
|df.read_html(filename)|匯入 HTML 檔案，Pandas 會抽出 \<table\> 標籤的資料|
|df.read_excel(filename)|匯入 Excel 檔案|

### .loc[]
- 用於選取資料。
- 用法：
	```python=
	df.loc[索引標籤]
	df.loc[[索引標籤1, 索引標籤2, ...]]
    df.loc[索引標籤, 欄位標籤]
    df.loc[[索引標籤1, 索引標籤2, ...], [欄位標籤1, 欄位標籤2, ...]]
    df.loc[索引標籤1:索引標籤2, 欄位標籤]
    df.loc[索引標籤, 欄位標籤1:欄位標籤2]
    df.loc[索引標籤1:索引標籤2, 欄位標籤1:欄位標籤2]
	```

### .iloc[]
- 使用從 0 開始的索引位置來選取資料。
- 用法：
    ```python=
    df.iloc[列索引位置, 欄索引位置]
    ```
> loc 索引器的索引和欄位標籤會包含最後一個標籤。