import requests

cURL = "https://graph.facebook.com/v6.0/me/posts?fields=id%2Cmessage&since=2020-01-01&until=2020-12-30&access_token=EAAk7weaWG7ABAApoZBi1QLJ7je05PaxCHMvb0NUDOZBu0wZANAfiiYqH9CgmqMnnf7FvXxvSAlNIudvJHX747CWaV2n8vCnnZBOYDe1hjdnTQdu0kV1dTgY2iqmvw0zMN8mCwjPXDJIslZCdZCQAPGyuW1iXkZBCkJXoGIs0i2DjkSzKhqHZBLb3AZCAImV4QhAtCNVKR7OGqq5fQqY1qzTDNuHM8gpTEUK0m43PKZARd2ZBQZDZD"

response = requests.get(cURL)
parsed = response.json()
for post in parsed["data"]:
    if "message" in post:
        print("message:", post["message"][0:25])
        print("id:", post["id"])
    