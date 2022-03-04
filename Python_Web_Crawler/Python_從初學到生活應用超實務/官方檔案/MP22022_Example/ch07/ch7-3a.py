import pandas as pd

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
df = pd.read_html(url)
print(type(df))
xrt = df[0]
print(type(xrt))


