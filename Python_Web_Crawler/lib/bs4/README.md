---
title: bs4
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/Xr2gbXW8Q7uCBT6PUfkGow/badge)](https://hackmd.io/Xr2gbXW8Q7uCBT6PUfkGow)

{%hackmd theme-dark %}

# BeautifulSoup
```python=
from bs4 import BeautifulSoup
```
- 用於剖析 HTML 網頁的內容
- 用法：
    ```python=
    variable_name = BeautifulSoup(content, 'html.parser')
    ```
    - content：網頁內容。
    - html.parser：指定使用 HTML 剖析器(Parser)。
- 
- Ex：
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