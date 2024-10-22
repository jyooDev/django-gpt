import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/users/"

def login(username, password):
    url = f"{BASE_URL}login/"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None  

def register(username, email, password, first_name, last_name):
    url = f"{BASE_URL}register/"
    data = {
        "username": username,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return True  
    elif response.status_code == 400:
        return response.json() 
    else:
        return None