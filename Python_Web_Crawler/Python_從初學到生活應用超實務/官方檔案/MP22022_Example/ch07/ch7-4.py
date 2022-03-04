import requests, json
import pandas as pd

url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

r = requests.get(url)
r.encoding = "utf-8"
data = json.loads(r.text)
df = pd.DataFrame.from_dict(data["retVal"], orient='index')
print("下載Youbike的JSON資料...")
df.to_csv("Youbike.csv",index=False,encoding="utf8")

