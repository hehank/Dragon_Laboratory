---
title: JSON
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/jVUV_g5vQaSQ6jazhJE4Bg/badge)](https://hackmd.io/jVUV_g5vQaSQ6jazhJE4Bg)


{%hackmd theme-dark %}

# Intro
- 全名：JavaScript Object Notation。
- 是一種描述結構化資料的常用格式。
- 是目前 Web API 和 Open Data 最常使用的資料傳輸格式。
- 使用大括號定義 Key-Value Pairs。
    - 例：
        ```json=
        {
            "key1": "value1"
            "key2": "value2"
            "key3": "value3"
            ...
        }
        ```
- JSON 物件陣列
    - 例：
        ```json=
        [
            {
            "key1": "value1"
            "key2": "value2"
            "key3": "value3"
            ...
            },
            {
            "key1": "value1"
            "key2": "value2"
            "key3": "value3"
            ...
            },
            ...
        ]
        ```

# Usage
```python=
import json
```
## JSON 資料對應的 Python 資料型別
| Python 資料型別          | JSON 資料    |
|:------------------------ |:------------ |
| dict(字典)               | JSON 物件    |
| list(串列)               | JSON 陣列    |
| str(字串)                | string(字串) |
| int(整數)、float(浮點數) | number(數值) |
| True、False              | true、false  |
| None                     | null         |

## Python 字典 -> JSON 字串
```python=
json.dumps(data, fp, sort_keys=False, indent=None, ensure_ascii=True)
```
- 說明：
    - data：Python 字典。
    - fp：要寫入的.json檔案名稱
        - EX："example.json"
    - sort_keys：等於 True 的時候，會按照 Key 來排序。
    - indent：可以設定顯示 Key-Value 時的縮排。
    - ensure_ascii：
        - True：以 `\uxxxx` 格式寫入。
        - False：以`你設定的`格式寫入。
### Ex：
- .py
	```python=
    import json

	data = {
	    "name": "Hank",
	    "score": 80,
	    "tel": "0987-987-987"
	}
    
	json_str = json.dumps(data, sort_keys=True, indent=4)
	print("JSON Object：", json_str)
	print("JSON Object Type：", type(json_str))
	```
- out
    ![](https://i.imgur.com/octlAM2.png)

## JSON 字串 -> Python 字典
```python=
json.loads(json_str)
```
- 說明
    - json_str：JSON 字串。
    - fp：要讀取的.json檔案名稱
        - EX："example.json"
### Ex：
- .py
	```python=
    import json

	data = {
	    "name": "Hank",
	    "score": 80,
	    "tel": "0987-987-987"
	}

	json_str = json.dumps(data)

	data2 = json.loads(json_str)
	print("Python Dict：", data2)
	print("Python Dict Type：", type(data2))
	print("Name：", data2["name"])
	print("Score：", data2["score"])
	```
- out
    ![](https://i.imgur.com/yKNQURe.png)
        
## 寫入 & 讀取 .json 檔案
### 寫入 .json 檔案
- 將 python 資料轉成 .json 檔案
	```python=
	json.dump(data, fp, sort_keys=False, indent=None, ensure_ascii=True)
	```
- Ex：
    - .py：
        ```python=
        import json

		jsonfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/Example.json"
		# jsonfile = "./Example.json"

		json_str = '{"name": "Hank","score": 80,"tel": "0987-987-987"}'
		data = json.loads(json_str)

		with open(jsonfile, 'w', encoding='utf-8', newline='') as fp:
		    json.dump(data, fp)
        ```
    - .json：
        ```json=
        {
		    "name": "Hank",
		    "score": 80,
		    "tel": "0987-987-987"
		}
        ```
### 讀取 .json 檔案
- 讀取 .json 檔案，讀完後將此 .json 檔案轉換成 python 的資料格式
	```python=
	json.load(fp)
	```
- Ex：
    - .py：
        ```python=
        import json

		jsonfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/Example.json"
		# jsonfile = "./Example.json"

		with open(jsonfile, mode='r', newline='') as fp:
		    data = json.load(fp)

		print("Name：", data["name"])
		print("Score", data["score"])
        ```
    - out：
        ![](https://i.imgur.com/fhzofNj.png)