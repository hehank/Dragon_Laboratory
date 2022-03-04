from facebook import GraphAPI

token = "EAAk7weaWG7ABAJQrK6yolnjUhcAq3XYZCWG4mBUtgrrCZCkbsicnNzZAYzcaFumhCT4WIEHZCAyZCI9nBPQfgZAneCTw59capGjk5ziUmL6w5weg1meHvkMjQmY6IPgTPXYit7rcxnArGegwyM7qI4bWyCXjZCyFHYI2qzL9wpZAQUXyp3dCLZCzv0JWIviNfapgPlpS0obFXGJRjRm5fGEyRjYmlsZCdertGggRZAT7lLeLAZDZD"

graph = GraphAPI(access_token=token)
profile = graph.get_object("me")
print("名稱: ", profile["name"])
print("id: ", profile["id"])

