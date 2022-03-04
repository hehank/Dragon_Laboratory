import requests

url = "http://graph.facebook.com/{}/picture?type=large"
default = "https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/HsTZSDw4avx.gif"

for user_id in range(4, 50, 3):
    response = requests.get(url.format(str(user_id)))
    if response.status_code == requests.codes.ok:
        if response.url != default:
            print(response.url)
