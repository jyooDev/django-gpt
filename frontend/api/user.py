import requests
from config import settings 

def get_user_details(access_token):
    url = f"{settings.BASE_URL}profile/" 
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  
    else:
        return None  