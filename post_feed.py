import requests

API_ENDPOINT = "http://34.207.10.230:3000/posts"

def post_feed(title, body, user_id, id):
    # data to be sent to api
    data = {"userId": user_id,
            "id": id,
            'title': title,
            'body': body}
    return data


r = requests.post(url = API_ENDPOINT, data = data)
