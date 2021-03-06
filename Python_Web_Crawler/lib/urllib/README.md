---
title: urllib
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/gAiL1VS9RHCiYsnc025YbA/badge)](https://hackmd.io/gAiL1VS9RHCiYsnc025YbA)


{%hackmd theme-dark %}

# parse
## urlparse()
```python=
from urllib.parse import urlparse
```
- 用來剖析 URL
- 用法：
    ```python=
    o = urlparse('your_URL')
    ```
- 屬性(attributes)：
    |屬性|說明|
    |---|----|
    |o.scheme|取得通訊協定|
    |o.netloc|取得網域名稱|
    |o.port|取得通訊埠的埠號|
    |o.path|取得網頁的路徑|
    |o.query|取得查詢字串|
- Ex：
    ```python=
    from urllib.parse import urlparse

    o = urlparse("http://example.com:80/test/index.php?user=hueyan")
    print("通訊設定：", o.scheme)
    print("網域名稱：", o.netloc)
    print("通訊埠號：", o.port)
    print("網頁路徑：", o.path)
    print("查詢字串：", o.query)
    ```

# request
```python=
from urllib import request
```
- Method：
    |method|說明|
    |------|---|
    |request.urlopen()|開啟網路上的檔案|
    |request.read()|讀取並下載|
    |request.close()|關閉網路上的檔案|
- Ex：
    ```python=
    from urllib import request

	url = "https://fchart.github.io/life.html"

	# ? 方法1
	response = request.urlopen(url)
	content = response.read()
	response.close()
	print(content.decode())
	
	# ? 方法2
	with request.urlopen(url) as response:
	    content = response.read()
	print(content.decode())
    ```

