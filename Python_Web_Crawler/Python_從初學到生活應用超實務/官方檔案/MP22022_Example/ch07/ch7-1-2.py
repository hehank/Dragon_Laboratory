import hashlib, requests, os

url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
path = "html_md5.txt"
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
if new_md5 != old_md5:
    print("台北的YouBike資料已經更新")
else:
    print("台北的YouBike資料沒有更新")
