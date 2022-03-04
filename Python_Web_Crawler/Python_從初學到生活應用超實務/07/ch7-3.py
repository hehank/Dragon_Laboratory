#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import requests
import os
import pandas as pd


def split_name(name):
    pos = name.find(')')
    return pd.Series({"幣別": name[0:pos] + ")"})


URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
md5file = "./Python_Web_Crawler/Python_從初學到生活應用超實務/07/xrt_md5.txt"
csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/07/xrt.csv"

html = requests.get(URL).text.encode('utf-8')
m = hashlib.md5(html)
new_md5 = m.hexdigest()
old_md5 = ""

if os.path.exists(md5file):
    with open(md5file, 'r') as fp:
        old_md5 = fp.read()
else:
    with open(md5file, 'w') as fp:
        fp.write(new_md5)

if new_md5 != old_md5:
    print("台銀匯率資料已更新")
    DF = pd.read_html(html)

    # ? 讀取到的 HTML 內容會以每個 <table> 去建立一個 DataFrame，我們只需要第一個
    xrt = DF[0]

    # ? 每一列只需要第 0-4個欄位的內容
    xrt = xrt.iloc[:, 0:5]

    xrt.columns = ["幣別", "現金(買)", "現金(賣)", "即期(買)", "即期(賣)"]

    # ? 刪除欄位重複的幣別名稱(如果沒有刪除會多出一行重複的幣別名稱)
    xrt["幣別"] = xrt["幣別"].apply(split_name)

    xrt.to_csv(csvfile, index=False, encoding="utf-8")

    # ? 從 DataFrame 的頭開始算，預設只取五列
    print(xrt.head())
else:
    print("台銀匯率資料沒有更新")
