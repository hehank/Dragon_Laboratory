#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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
