import hashlib

m = hashlib.md5()
data = "Python程式設計"
m.update(data.encode("utf-8"))
md5_str = m.hexdigest()
print(md5_str)
