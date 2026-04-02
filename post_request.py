import requests
from config import BASE_URL, HEADERS

def create_post():
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "Hello API",
        "body": "This is a POST request",
        "userID": 1
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    print("status code:", response.status_code)
    print("Response JSON:", response.json())
    return response.json()