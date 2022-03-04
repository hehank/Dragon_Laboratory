from facebook import GraphAPI

token = "EAAk7weaWG7ABAJQrK6yolnjUhcAq3XYZCWG4mBUtgrrCZCkbsicnNzZAYzcaFumhCT4WIEHZCAyZCI9nBPQfgZAneCTw59capGjk5ziUmL6w5weg1meHvkMjQmY6IPgTPXYit7rcxnArGegwyM7qI4bWyCXjZCyFHYI2qzL9wpZAQUXyp3dCLZCzv0JWIviNfapgPlpS0obFXGJRjRm5fGEyRjYmlsZCdertGggRZAT7lLeLAZDZD"

postids = ["2757671087664447_2655005734597650",
           "2757671087664447_2650430408388516"]

graph = GraphAPI(access_token=token)
posts = graph.get_objects(ids=postids)
for pid in postids:
    post = posts[pid]
    print("id:", post["id"])
    print("message:", post["message"][0:29])
    print("created_time:", post["created_time"])

