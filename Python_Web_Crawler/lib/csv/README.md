---
title: csv
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/T5de-VU6Tm-u5bqL7hekPQ)](https://hackmd.io/T5de-VU6Tm-u5bqL7hekPQ)

{%hackmd theme-dark %}

# Usage
```python=
import csv
```

# 讀取 CSV 檔案

### Ex
- .py
    ```python=
    import csv

	# csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/05/Example.csv"
	csvfile = "./Example.csv"

	with open(csvfile, 'r') as fp:
	    reader = csv.reader(fp)
	    for row in reader:
	        print(','.join(row))
	```
- .csv
    ```csv=
    Data1,Data2,Data3
	10,33,45
	5,25,56
    ```

# 寫入 CSV 檔案