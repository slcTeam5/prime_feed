import requests

API_ENDPOINT = "http://34.207.10.230:3000/posts"

class Make_post:
    def __init__(self, title, body, user_id, id):
        data = {"userId": user_id,
                "id": id,
                'title': title,
                'body': body}
        r = requests.post(url=API_ENDPOINT, data=data)
        