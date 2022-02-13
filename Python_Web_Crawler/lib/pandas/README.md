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
```python=
pd.DataFrame(data=None, index=None, dtype=None, name=None)
```

## 介紹
- 是一種二維的陣列資料結構。
- 可視為是類似 Excel 的工作表。
- 陣列內可存放 int、str、float、Python object (例如：list、dict、...)、Numpy 的 ndarray、純量、...等。

## concat
```python=
pd.concat(obj, axis=0)
```
- obj：[Series1, Series2, ...] or [DataFrame1, DataFrame2, ...]
- axis：要連接的軸
    - 0 => index -> 預設
    - 1 => column(欄)