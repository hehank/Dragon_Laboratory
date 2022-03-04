import json
 
jsonfile = "Example.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp)
print("姓名: ", data["name"])
print("分數: ", data["score"])
print("電話: ", data["tel"])


