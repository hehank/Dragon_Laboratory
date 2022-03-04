# Python Program
import requests, json

token = "EAAHiNkMZBqmYBAOl0odwBmc0cl1lO977BCNDK1eGgetF7ecZAZACjJ5j93CRBlO5W4IvU4FfSPmMk304YwlLlwXhZCzxL8h3ZAh2sExi3ftjScXYffOvRuH7ZCawzMEFQR19WR6C9ckMHmEU3h9ItYG3prycZBd6leXzeqp4CP7dAnyfQoxJTOxZBbPRZA878ZBuh3R17RgXV5mupRALFJ3XOPzAEJZCrWDvBZCfuHvZCZCUKWgwZDZD"

cURL = "https://graph.facebook.com/v6.0/me/posts?fields=message%2Ccreated_time&since=2020-01-01&until=2020-12-31&access_token=" + token

response = requests.get(cURL).text
data = json.loads(response)

for d in data["data"]:
    if "message" in d:
        print("message:", d["message"])
        print("id:", d["id"])
    