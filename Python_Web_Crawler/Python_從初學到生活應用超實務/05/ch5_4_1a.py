#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup

csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/05/Elements.csv"
# csvfile = "./Elements.csv"
url = "https://fchart.github.io/Elements.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    with open(csvfile, encoding="utf-8", mode="w", newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(["Qestion", "Answer1", "Answer2"])

        tags = soup.find_all("li", class_="question")

        for tag in tags:
            tag_q = tag.find("b")
            ques = tag_q.text
            tag_a = tag.find_all("li", class_="response")
            writer.writerow([ques, tag_a[0].text, tag_a[1].text])

else:
    print("HTTP Request Rrror")
