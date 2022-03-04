import urllib.request
import json

url = "https://fchart.github.io/books.json"
jsonfile = "Books.json"
try:
    response = urllib.request.urlopen(url)
    contents = response.read()
    response.close()
    books = json.loads(contents)
except:
    books = None
if not books:
    print("沒有圖書資料...")
else: 
    print("將圖書資料寫入檔案...")
    with open(jsonfile, 'w', encoding='utf-8') as fp:
        json.dump(books,fp, ensure_ascii=False)



