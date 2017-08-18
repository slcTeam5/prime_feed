import requests

API_ENDPOINT = "http://34.207.10.230:3000/posts/"


class MakePost:
    def __init__(self, title, body, author, id):
        data = {"author": author,
                "id": id,
                "title": title,
                "body": body}
        r = requests.post(url=API_ENDPOINT, json=data)
