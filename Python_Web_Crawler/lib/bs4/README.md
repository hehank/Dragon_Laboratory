---
title: bs4
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/Xr2gbXW8Q7uCBT6PUfkGow/badge)](https://hackmd.io/Xr2gbXW8Q7uCBT6PUfkGow)

{%hackmd theme-dark %}

# Install bs4
```python=
pip3 install bs4
```

# BeautifulSoup
```python=
from bs4 import BeautifulSoup
```
- 用於剖析 HTML 網頁的內容
- 用法：
    ```python=
    soup = BeautifulSoup(content, 'html.parser')
    ```
    - content：網頁內容。
    - html.parser：指定使用 HTML 剖析器(Parser)。
## 讀取指定的 HTML 標籤
```python=
tags = soup("Specific_HTML_tag")
```
> tags => list(串列)
- Ex：
    ```python=
    tags = soup("a")
    ```
## 讀取 HTML 標籤的屬性值和標籤內容
- 以 tags 串列中的其中一個讀取到的 \<a\> 標籤來講
    ```python=
    tag = tags[12] # => 第 13 個
    ```
- 屬性或方法：
    | 屬性或方法 | 說明 |
    | -------- | ---- |
    | tag.text | 取得 HTML 標籤內容 |
    | tag.attrs | 取得所有 HTML 標籤屬性和值(以字典類型儲存) |
    | tag["HTML_Tag_Attribute"] | 取得 HTML 標籤內屬性為 HTML_Tag_Attribute 的值 |
    | tag.get("HTML_Tag_Attribute", None) | 取得 HTML 標籤內屬性為 HTML_Tag_Attribute 的值，若沒有此屬性，就傳回第二個參數 None |
- Ex1：
    ```python=
    import requests
	from bs4 import BeautifulSoup

	url = "https://fchart.github.io"
	response = requests.get(url)
	
	if response.status_code == 200:
	    soup = BeautifulSoup(response.text, "html.parser")
	    tags = soup("a")
	
	    for tag in tags:
	        href = tag.get("href", None)
	        print(href)

	else:
	    print("HTTP Request Rrror")
    ```
- Ex2：
    ```python=
    #! /usr/bin/env python3
	# -*- coding: utf-8 -*-

	import requests
	from bs4 import BeautifulSoup
	
	url = "https://fchart.github.io"
	response = requests.get(url)

	if response.status_code == 200:
	    soup = BeautifulSoup(response.text, "lxml")
	
	    tags1 = soup("a")
	    tag = tags1[12]
	
	    print("URL 網址：", url)
	    print("標籤內容：", tag.text)
	    print("target 屬性：", tag["target"])
	
	    tags2 = soup("img")
	    tag = tags2[1]
	
	    print("圖片網址：", tag.get("src", None))
	    print("alt 屬性：", tag["alt"])
	    print("屬性和值：", tag.attrs)
	else:
	    print("HTTP Request Rrror")
    ```
## 搜尋 HTML 標籤
- 測試 URL：
    ```txt=
    https://fchart.github.io/Elements.html
    ```
- 方法：
    | 方法 | 說明 |
    | --- | ---- |
    | select_one() | 使用 CSS 選擇器(selector)的觀念尋找元素，回傳`第一個`符合的物件 |
    | select() | 使用 CSS 選擇器(selector)的觀念尋找元素，回傳`所有`符合的物件串列  |
    | find() | 使用標籤名稱和屬性值來搜尋 HTML 標籤，回傳`第一個`符合的 HTML 標籤物件 |
    | find_all() | 使用標籤名稱和屬性值來搜尋 HTML 標籤，回傳`所有`符合的 HTML 標籤物件的串列 |
### select() & select_one()：
```python=
# select()
tag = soup.select("[HTML_Tag_Name][[ ].class_Name][[ ]#id_Name]")

# select_one()
tags = soup.select_one("[HTML_Tag_Name][[ ].class_Name][[ ]#id_Name]")
```
- Ex：
    ```python=
    # select()
    tags = soup.select("a")
    tags = soup.select("a #author")
    tags = soup.select("a .happy")
    tags = soup.select(".happy #author")
    tags = soup.select("a #author .happy")
    tags = soup.select(".happy")
    tags = soup.select("#author")

    # select_one()
    tag = soup.select_one("a")
    tag = soup.select_one("a #author")
    tag = soup.select_one("a .happy")
    tag = soup.select_one("a #author .happy")
    tag = soup.select_one(".happy")
    tag = soup.select_one("#author")
    ```
### find() & find_all()：
```python=
# find()
tag = soup.find(["HTML_Tag_Name" | ["HTML_Tag_Name"] | {attribute:"value"}], [class_="class_Name"], [attribute="value" | re.compile("value") | True], [attrs={attribute:"value"}], [recursive=False], [string="str" | ["str"] | re.compile("value")])
    
# find_all()
tags = soup.find_all(["HTML_Tag_Name" | ["HTML_Tag_Name"] | {attribute:"value"}], [class_="class_Name"], [attribute="value" | re.compile("value") | True], [attrs={attribute:"value"}], [limit=n], [recursive=False], [string="str" | ["str"] | re.compile("value")])
```
- 說明：
    |參數|說明|
    |---|----|
    |"HTML_Tag_Name"|HTML 標籤名稱|
    |["HTML_Tag_Name"]|可用來搜尋多個符合的 HTML 標籤(只要符合其中一個就算)，例：[td","th"]|
    |{attribute:"value"}|利用 HTML 標籤的屬性來搜尋(要全部符合)，例：{"class":"sister","name":"title"}|
    |class_="class_Name"|標籤中的 class 名稱|
    |attribute="value"|例：id="link"|
    |attribute=re.compile("regular_expression_str")|例：href=re.compile("elsie"))|
    |attribute=True|所有包含此 attribute 的標籤，例：class=True|
    |attrs={attribute:"value"}|只能用來搜尋自訂義的屬性和一般搜尋時無法搜尋到的標籤，例：attrs={"data-foo": "value"}|
    |limit=n|限制指搜尋 n 個符合條件的|
    |recursive=False|指搜尋某個標籤的第一層子節點，預設 True|
    |string="str"|例：string="Hank"|
    |string=["str"]|例：string=["Hank", "Jack"]|
    |string=re.compile("value")|例：string=re.compile("Dormouse")|
- Ex：
```python=
# find()
tag = soup.find("a")
    
# find_all()
tags = soup.find_all("a")
```
### Ex：
```python=
import requests
from bs4 import BeautifulSoup

url = "https://fchart.github.io/Elements.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
    
# select_one()
tag = soup.select_one("h2")
print("h2：", tag.text)

tag = soup.select_one("#q1")
tag2 = tag.select_one("b")
print("Question 1：", tag.text)
    
# select()
tags = soup.select("b")
for tag in tags:
	    print("b：", tag.text)

# find()
tag = soup.find("h2")
print("h2：", tag.text)
    
tag = soup.find("li", id="q2")
tag2 = tag.find("b")
print("Question 2：", tag2.text)

# find_all()
tags = soup.find_all("b")
for tag in tags:
    print("b：", tag.text)
```
### Reference：
- [Beautiful Soup 4.4.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all)
- [Beautiful Soup — Python 的網路爬蟲套件](https://medium.com/@yuhsienyeh/beautiful-soup-python-%E7%9A%84%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%E5%A5%97%E4%BB%B6-be09be3d1a21)