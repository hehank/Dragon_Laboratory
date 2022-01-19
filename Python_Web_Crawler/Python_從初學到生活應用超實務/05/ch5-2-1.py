#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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
