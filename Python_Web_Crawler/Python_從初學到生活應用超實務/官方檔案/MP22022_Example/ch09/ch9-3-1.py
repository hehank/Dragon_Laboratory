import configparser

config = configparser.ConfigParser()
config.read('user.ini')

username = config.get("user", "username")
password = config.get("user", "password")
print(username, password)