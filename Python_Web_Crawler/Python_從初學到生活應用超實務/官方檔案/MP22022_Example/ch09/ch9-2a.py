from facebook import GraphAPI

token = "EAAk7weaWG7ABAJQrK6yolnjUhcAq3XYZCWG4mBUtgrrCZCkbsicnNzZAYzcaFumhCT4WIEHZCAyZCI9nBPQfgZAneCTw59capGjk5ziUmL6w5weg1meHvkMjQmY6IPgTPXYit7rcxnArGegwyM7qI4bWyCXjZCyFHYI2qzL9wpZAQUXyp3dCLZCzv0JWIviNfapgPlpS0obFXGJRjRm5fGEyRjYmlsZCdertGggRZAT7lLeLAZDZD"

graph = GraphAPI(access_token=token)
page = graph.get_connections(id="me", connection_name="posts")
posts = page["data"]
print ("共有", len(posts), "篇PO文")
for post in posts:
    if "message" in post:        
        print ("post_id:", post["id"])


