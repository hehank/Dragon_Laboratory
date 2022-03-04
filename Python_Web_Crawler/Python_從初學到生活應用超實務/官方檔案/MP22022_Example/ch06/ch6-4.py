import urllib.request, urllib.parse
import json

surl = "https://www.googleapis.com/books/v1/volumes?"
keyword = input("輸入書名關鍵字: ")

options = {
     "q" : keyword,
     "maxResults" : "3",
     "projection": "lite" }
url = surl + urllib.parse.urlencode(options)
print(url)

try:
    response = urllib.request.urlopen(url)
    contents = response.read().decode('utf-8-sig')
    response.close()
    print("下載: ", len(contents), "字元")
    info = json.loads(contents)
except:
    info = None

if not info:
    print("沒有圖書資料")
else:    
    print("--------------------------")
    for item in info["items"]:
        book = item["volumeInfo"]
        print("圖書名: " , book["title"])
        print("出版商: ", book["publisher"])
        print("出版日: ", book["publishedDate"])
        print("--------------------------")

