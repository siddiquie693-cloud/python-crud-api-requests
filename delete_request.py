import requests
from config import BASE_URL, HEADERS

def delete_post():
    post_id = 1
    url = f"{BASE_URL}/posts/{post_id}"
    response =requests.delete(url, headers=HEADERS)
    print("status code:", response.status_code)
    print("Response Text:", response.text)
    return response.status_code