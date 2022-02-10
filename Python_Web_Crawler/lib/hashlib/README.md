---
title: hashlib
tags: Python lib
lang: zh-tw
---

[![hackmd-github-sync-badge](https://hackmd.io/CJdudwLjTcKh10KGvMG6-A/badge)](https://hackmd.io/CJdudwLjTcKh10KGvMG6-A)

{%hackmd theme-dark %}

# Usage
```python=
import hashlib
```

# SHA
## 256
```python=
m = hashlib.sha256([data])
```

## 512
```python=
m = hashlib.sha512([data])
```

# SHA3
## 256
```python=
m = hashlib.sha3_256([data])
```

## 512
```python=
m = hashlib.sha3_512([data])
```

# MD5
```python=
m = hashlib.md5([data])
```

## EX1
- .py：
	```python=
	import hashlib

	data = b"My name is HankHe"
	# data = "My name is HankHe".encode("utf-8")

	# TODO: Calculate hash code
	# ? Method 1：
	m = hashlib.md5(data)

	# ? Method 2：
	# m = hashlib.md5()
	# m.update(data)

	# TODO: Get hash code
	md5_hexstr = m.hexdigest()
	print(md5_hexstr)
	```
- output：
    ![](https://i.imgur.com/JbXB4Vl.png)

## EX2
- .py：
	```python=
	import hashlib
	import requests
	import os

	URL = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
	md5file = "./Python_Web_Crawler/Python_從初學到生活應用超實務/07/html_md5.txt"
	# md5file = "./html_md5.txt"

	# TODO: Calculate new md5 code
	html_content = requests.get(URL).text.encode('utf-8')
	m = hashlib.md5(html_content)
	new_md5 = m.hexdigest()

	# TODO: Determine md5file is exist or not
	old_md5 = ""
	if os.path.exists(md5file):
	    with open(md5file, 'r') as fp:
	        old_md5 = fp.read()

	    if old_md5 != new_md5:
	        print("Taipei TouBike Data has been updated")
	        with open(md5file, 'w') as fp:
	            fp.write(new_md5)

	    else:
	        print("Taipei TouBike Data not updated")

	else:
	    with open(md5file, 'w') as fp:
	        fp.write(new_md5)
	    print("Taipei TouBike Data has been updated")
	```
- output：
    ![](https://i.imgur.com/sX85hVS.png)
- html_md5.txt：
    ```txt=
    f93c57592caf5e3676d2c77ced7f1946
    ```