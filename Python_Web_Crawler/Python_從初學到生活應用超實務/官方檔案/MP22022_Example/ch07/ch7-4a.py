import requests, json
import pandas as pd
import time

url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

ubike_df = pd.DataFrame(columns=('mday', 'tot', 'sbi', 'bemp'))

for i in range(20):
    r = requests.get(url)
    r.encoding = "utf-8"
    data = json.loads(r.text)
    df = pd.DataFrame.from_dict(data["retVal"], orient='index')
    mday = df.iloc[0,5]
    print("更新時間: ", mday)
    tot = df.iloc[0,2]
    print("總停車格: ", tot)
    sbi = df.iloc[0,3]
    print("車輛數: ", sbi)
    bemp = df.iloc[0,12]
    print("空位數: ", bemp)
    print("----------------------------")
    s = pd.Series({'mday':mday,'tot':tot,'sbi':sbi,'bemp':bemp})
    ubike_df = ubike_df.append(s, ignore_index=True)
    time.sleep(120)

print("下載Youbike捷運市政府站的JSON資料...")
ubike_df.to_csv("Youbike0001.csv",index=False,encoding="utf8")
