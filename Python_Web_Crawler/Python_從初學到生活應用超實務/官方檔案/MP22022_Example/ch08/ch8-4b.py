import pandas as pd

df = pd.read_csv("2330.TW.csv", encoding="utf8")
df = df.dropna()
df["Date"] = pd.to_datetime(df["Date"])
df.plot(kind="line", x="Date", y="Close", 
        title="台積電2017年的每日收盤價")





