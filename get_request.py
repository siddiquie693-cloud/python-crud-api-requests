import requests
from config import BASE_URL, HEADERS

def get_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url, headers=HEADERS)
    print("status code:", response.status_code)
    print("Response JSON:", response.json())
    return response.json()