from facebook import GraphAPI
import json

token = "EAAk7weaWG7ABAJQrK6yolnjUhcAq3XYZCWG4mBUtgrrCZCkbsicnNzZAYzcaFumhCT4WIEHZCAyZCI9nBPQfgZAneCTw59capGjk5ziUmL6w5weg1meHvkMjQmY6IPgTPXYit7rcxnArGegwyM7qI4bWyCXjZCyFHYI2qzL9wpZAQUXyp3dCLZCzv0JWIviNfapgPlpS0obFXGJRjRm5fGEyRjYmlsZCdertGggRZAT7lLeLAZDZD"

graph = GraphAPI(access_token=token)
post = graph.get_object(id="2757671087664447_2655005734597650")
print(json.dumps(post, indent=4))
print("id:", post["id"])
print("message:", post["message"].rstrip())
print("created_time:", post["created_time"])

