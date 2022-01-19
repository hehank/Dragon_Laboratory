#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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
