from facebook import GraphAPI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
token = config.get('facebook', 'access_token')

graph = GraphAPI(access_token=token)
post = graph.get_object(id="2757671087664447_2655005734597650")
print("id:", post["id"])
print("message:", post["message"].rstrip())
print("created_time:", post["created_time"])

