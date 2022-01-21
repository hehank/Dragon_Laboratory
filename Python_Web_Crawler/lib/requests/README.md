---
title: requests
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/iPfZHdx0SuGli_sm_AAK5Q/badge)](https://hackmd.io/iPfZHdx0SuGli_sm_AAK5Q)

{%hackmd theme-dark %}

# get
```python=
from requests import get
```
- 用來發送 HTTP request
- 用法：
    ```python=
    response = get(URL)
    ```
- 屬性(attributes)：
    |屬性|說明|
    |---|----|
    |response.text|編碼過後的檔案內容|
    |response.contents|未編碼過(Bytes)的檔案內容，適用非文字內容的 HTTP 請求|
    |response.encoding|取得檔案內容的編碼|
    |response.status_code|狀態碼，值 200 或 requests.codes.ok 表示請求成功|
- Ex：
    ```python=
    from requests import get

	url = "https://fchart.github.io/test.html"
	response = get(url)

	if response.status_code == 200:
	    print(response.text)
	    print("--------------------------------------------------------")
	    print(response.content.decode())
	    print("編碼：", response.encoding)
	else:
	    print("HTTP Request Rrror")
	    ```