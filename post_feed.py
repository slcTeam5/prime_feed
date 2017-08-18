import requests

API_ENDPOINT = "http://34.207.10.230:3000/posts"

def post_feed(title, body, user_id, id):
    # data to be sent to api
    data = {"userId": user_id,
            "id": id,
            'title': title,
            'body': body}
    return data

data = post_feed('Three People win awrds', 'hsdkfshkdfhasdf', 1, 1)
r = requests.post(url = API_ENDPOINT, data = data)
