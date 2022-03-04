import hashlib, requests, os
import pandas as pd

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
path = "xrt_md5.txt"
old_md5 = ""
if os.path.exists(path):
    with open(path, 'r') as fp:
        old_md5 = fp.read()
html = requests.get(url).text.encode("utf-8")
m = hashlib.md5()
m.update(html)
new_md5 = m.hexdigest()
with open(path, "w") as fp:
    fp.write(new_md5)
def split_name(name):
    pos = name.find(')')
    return pd.Series({
        '"幣別"': name[0:pos] + ")"
    })        
if new_md5 != old_md5:
    print("台銀匯率資料已經更新")
    df = pd.read_html(url)
    xrt = df[0]
    xrt = xrt.iloc[:,0:5]
    xrt.columns = ["幣別","現金(買)",
                   "現金(賣)","即期(買)",
                   "即期(賣)"]
    xrt["幣別"] = xrt["幣別"].apply(split_name)
    xrt.to_csv('xrt.csv',index=False,encoding="utf8")
    print(xrt.head())     
else:
    print("台銀匯率資料沒有更新")

