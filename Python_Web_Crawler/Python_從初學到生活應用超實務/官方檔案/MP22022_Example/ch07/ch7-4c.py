import requests, json
import pandas as pd

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=1000"

r = requests.get(url)
r.encoding = "utf-8"
data = json.loads(r.text)
df = pd.DataFrame(data)
print("下載Youbike的JSON資料...")
df.to_csv("Youbike_newTP.csv",index=False,encoding="utf8")

