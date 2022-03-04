import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2330.TW.csv", encoding="utf8")
df = df.dropna()
close = df["Close"]
volume = df["Volume"]
plt.scatter(close, volume)
plt.xlabel("收盤價")
plt.ylabel("成交量")
plt.title("台積電的收盤價與成交量")
plt.show()





