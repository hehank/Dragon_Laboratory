---
title: csv
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/T5de-VU6Tm-u5bqL7hekPQ/badge)](https://hackmd.io/T5de-VU6Tm-u5bqL7hekPQ?both)

{%hackmd theme-dark %}

# Usage
```python=
import csv
```

# 開啟檔案
## open()
```python=
open(file[, mode='r'][, buffering=- 1][, encoding=None][, errors=None][, newline=None][, closefd=True][, opener=None])
```
### 說明：
- file：要開啟的檔案。
    - 例："test.txt"、"./mydata/test/test.csv"
- mode：指定打開檔案的模式，預設為'r'。
    - 模式：
        | mode | 說明                                                                                               |
        | ---- | -------------------------------------------------------------------------------------------------- |
        | 'r'  | 讀取(預設)                                                                                         |
        | 'w'  | 寫入，如果是寫入已存在檔案會先`清空`內容，如果檔案不存在會幫你建立                                 |
        | 'w+  | 與 'w' 模式差別在於此模式包含讀取                                                                  |
        | 'x'  |                                                                                                    |
        | 'a'  | 寫入，如果是寫入已存在檔案，要寫入的內容會直接`接續`在原本的檔案內容後面，如果檔案不存在會幫你建立 |
        | 'a+  | 與 'a' 模式差別在於此模式包含讀取                                                                  |
        | 'b'  | 二進制(binary)模式                                                                                 |
        | 't'  | 文本模式(預設)                                                                                     |
- buffering：
- encoding：指定編碼模式。
    - 例：encoding="utf-8"
- errors：指定如何處理编碼和解碼錯誤 (無法在二進制模式下使用)。
    - 例：errors='ignore' => 忽略錯誤訊息
- newline：控制 [universal newlines(通用換行字元)](https://docs.python.org/zh-tw/3/glossary.html#term-universal-newlines) 如何作用。也就是設定要把 '\n' 取代為什麼字元。
    - 例：newline="" => 移除換行字元。
- closefd：
- opener：
- 如果文件無法開啟會引發 [OSError](https://docs.python.org/zh-tw/3/library/exceptions.html#OSError)。

## Reference
- [Python_内置函数](https://docs.python.org/zh-tw/3/library/functions.html?highlight=open#open)
- [Python open() 函数](https://www.runoob.com/python/python-func-open.html)
- [[Python初學起步走-Day29] - 檔案讀寫 ](https://ithelp.ithome.com.tw/articles/10161708)

# 讀取 CSV 檔案
## csv.reader()
```python=
csv.reader(csvfile, delimiter=',')
```
- 說明：
    - csvfile：要讀取的 csv 檔案。
    - delimiter：指定讀取時的分隔字元(預設為',')。
- Ex：
    - .py
    	```python=
    	import csv
    
    	csvfile = "./test.csv"
    
    	with open(csvfile, newline='') as csvfile:
    	    
    	    rows = csv.reader(csvfile, delimiter=':')

    	    for row in rows:
    	        print(row)
    	```
    - .csv
        ```csv=
        t1:t2:t3
        t4:t5:t6
        t7:t8:t9
        ```
    - out  
        ![](https://i.imgur.com/Oji1gwO.png)

## csv.DictReader()
```python=
csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
```

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
## csv.writer()
```python=
csv.writer(csvfile, delimiter=',')
```
- 說明：
    - csvfile：要寫入的 csv 檔案。
    - delimiter：指定寫入時的分隔字元(預設為',')。
- Ex：
    - .py
        ```python=
        import csv

		csvfile = "./out.csv"

		with open(csvfile, mode="w", encoding="utf-8", newline='') as fp:

		    writer = csv.writer(fp, delimiter=' ')

		    for i in range(1, 10, 3):
		        writer.writerow([i, i+1, i+2])
        ```
    - out.csv
        ```csv=
        1 2 3
		4 5 6
		7 8 9
        ```
- Ex(寫入二維表格)：
    - .py
    	```python=
    	import csv

		csvfile = "./out.csv"

		with open(csvfile, mode="w", encoding="utf-8", newline='') as fp:

		    writer = csv.writer(fp, delimiter=' ')
	
		    lst = []
		    for i in range(1, 10, 3):
		        lst.append([i, i+1, i+2])

		    writer.writerows(lst)
		```
    - out.csv
        ```csv=
        1 2 3
		4 5 6
		7 8 9
        ```

## csv.DictWriter()
```python=
csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
```

# Reference
- [Python 讀取與寫入 CSV 檔案教學與範例](https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/)
- [CSV 文件读写](https://docs.python.org/zh-tw/3/library/csv.html)