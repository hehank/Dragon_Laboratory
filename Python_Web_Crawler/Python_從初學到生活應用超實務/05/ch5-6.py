#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup


def write_to_csv(items, csv_filename):
    with open(csv_filename, mode='w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        for item in items:
            writer.writerow(item)


url = "https://movies.yahoo.com.tw/movie_thisweek.html?page=1"
csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/05/movies.csv"
# csvfile = "./movies.csv"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    # ? 初始化格式
    movies = [["中文片名", "英文片名", "期待度", "海報圖片", "上映日"]]

    root = soup.select_one("#content_l > div.release_box > ul")

    tag_li = root.find_all("li")

    # ? 擷取所有電影資訊
    for row in tag_li:
        # ? 擷取海報圖片
        photo = row.find("div", class_="release_foto")
        photo_src = photo.find("img")["src"].strip()

        # ? 擷取其他資訊
        info = row.find("div", class_="release_info_text")

        # ? 電影中、英文名稱
        name = info.find("div", class_="release_movie_name")
        c_name = name.find("a").text.strip()
        e_name = name.find("div", class_="en").find("a").text.strip()

        # ? 電影期待度
        expect = info.find("div", class_="leveltext")
        if (expect):
            expect = expect.find("span").text.strip()
        else:
            expect = None

        # ? 電影上映日
        release = info.find("div", class_="release_movie_time").text.strip()

        movies.append([c_name, e_name, expect, photo_src, release])

    # ? 寫入到 movies.csv
    write_to_csv(movies, csvfile)

else:
    print("HTTP Request Rrror")
