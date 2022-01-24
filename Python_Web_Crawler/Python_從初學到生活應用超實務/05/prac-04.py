#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup

url = "https://fchart.github.io/vba/ex3_03.html"
csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/05/prac-04.csv"
# csvfile = "./prac-04.csv"

response = requests.get(url)

if response.status_code == 200:
    with open(csvfile, mode="w", encoding="utf-8", newline="") as fp:
        writer = csv.writer(fp)

        soup = BeautifulSoup(response.text, 'lxml')

        # ? 取得 <table class="tt"> 標籤物件
        tag_table = soup.find("table", class_="tt")

        # ? 找出所有 <tr>
        tags_tr = tag_table.find_all("tr")
        for tag in tags_tr:
            lst = []

            # ? 找出所有 <td> 和 <th>
            tags_th_td = tag.find_all(["td", "th"])
            for row in tags_th_td:
                lst.append(row.text.replace("\n", "").replace("\r", ""))

            # ? 寫入
            writer.writerow(lst)

else:
    print("HTTP Request Rrror")
