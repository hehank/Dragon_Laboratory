#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd

URL = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
csvfile = ".\\Python_Web_Crawler\\Python_從初學到生活應用超實務\\07\\Youbike.csv"

r = requests.get(URL)

if r.status_code == 200:
    r.encoding = "UTF-8"
    data = json.loads(r.text)
    DF = pd.DataFrame(data)
    print("下載 Youbike 的 JSON 資料...")
    DF.to_csv(csvfile, index=False, encoding="UTF-8")
