import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/users/"

def get_user_details(access_token):
    url = f"{BASE_URL}profile/" 
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  
    else:
        return None  