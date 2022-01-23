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
