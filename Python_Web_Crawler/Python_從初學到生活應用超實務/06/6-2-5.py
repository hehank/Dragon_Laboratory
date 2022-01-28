#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

url = "https://fchart.github.io/books.json"
jsonfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/books.json"

try:
    response = requests.get(url)
    if response.status_code == 200:
        books = json.loads(response.text)
    else:
        print("HTTP Request Error")
except:
    books = None

if books is None:
    print("No books found....")

else:
    print(f"Dump book data to {jsonfile}....")
    with open(jsonfile, mode='w', encoding='utf-8', newline='') as fp:
        json.dump(books, fp, indent=4, ensure_ascii=False)

    print(f"{jsonfile} content：")
    print(f"{len(books)} books in total")
    for book in books:
        id = book["id"]
        title = book["title"]
        print(f"Book Number：{id} -> Book Name：{title}")
