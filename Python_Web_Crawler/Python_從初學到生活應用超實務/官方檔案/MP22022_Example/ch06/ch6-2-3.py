import json

json_str = '{"name":"Joe Chen","score":95,"tel":"0933123456"}'
jsonfile = "Example.json"
data = json.loads(json_str)
with open(jsonfile, 'w') as fp:
    json.dump(data, fp)

