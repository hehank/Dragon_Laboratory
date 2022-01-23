#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://fchart.github.io"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup("a")

    for tag in tags:
        href = tag.get("href", None)

        if ((href != "#") and (href != None) and ("#" not in href) and ("http" in href) and ("http" in href)):
            print(href)

else:
    print("HTTP Request Rrror")
