from sqlalchemy import create_engine
import pandas as pd
import requests, json

url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

r = requests.get(url)
r.encoding = "utf-8"
data = json.loads(r.text)
df = pd.DataFrame.from_dict(data["retVal"], orient='index')

engine = create_engine("mysql+pymysql://root@localhost:3306/ubike")
df.to_sql("youbike", engine, index=False)
print("在 ubike 資料庫建立 youbike 資料表...")

