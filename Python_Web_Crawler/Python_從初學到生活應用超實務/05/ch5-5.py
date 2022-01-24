#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_media.asp"
csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/05/video_formats.csv"
# csvfile = "video_formats.csv"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    # ? 先找到符合 <table class="ws-table-all notranslate"> 的標籤物件
    tag_table = soup.find("table", class_="ws-table-all notranslate")

    # ? 再找出 <table> 裡面所有的 <tr>
    tags_tr = tag_table.find_all("tr")

    # ? 開啟 video_formats.csv
    with open(csvfile, mode="w", encoding="utf-8", newline='') as fp:
        writer = csv.writer(fp)

        for tag in tags_tr:
            lst = []

            # ? 再找出 <tr> 裡面所有的 <td> 跟 <th>
            for row in tag.find_all(["td", "th"]):
                lst.append(row.text.replace("\n", "").replace("\r", ""))

            # ? 寫入
            writer.writerow(lst)

else:
    print("HTTP Request Rrror")
