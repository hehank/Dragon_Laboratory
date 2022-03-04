import urllib.request
import json
 
url = "https://fchart.github.io/books.json"

response = urllib.request.urlopen(url)
contents = response.read()
response.close()
books = json.loads(contents.decode('utf-8-sig'))
print("共有: ", len(books), "本書")
for book in books:
    print("書號: ", book["id"], end="-")
    print("書名: ", book["title"])
