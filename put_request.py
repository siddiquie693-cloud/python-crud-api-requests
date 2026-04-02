import requests
from config import BASE_URL, HEADERS

def update_post():
    post_id = 1
    url = f"{BASE_URL}/posts/{post_id}"
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "This is PUT request",
        "userID": 1
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    print("status code:", response.status_code)
    print("Response JSON:", response.json())
    return response.json()