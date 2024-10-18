import streamlit as st
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


def get_user_details(access_token):
    url = f"{BASE_URL}profile/" 
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  
    else:
        return None  


def login_ui():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login(username, password)
        if result:
            st.success("Logged in successfully!")
            st.session_state["access_token"] = result["access"]
            st.session_state["refresh_token"] = result["refresh"]
            st.session_state.page = "user_detail"
        else:
            st.error("Invalid username or password. Try again.")

    if st.button("Register here"):
        st.session_state.page = "register"


def register_ui():
    st.title("Register")

    username = st.text_input("Username", key="username_input")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password", key="password_input")
    first_Name = st.text_input("Firstname")
    last_Name = st.text_input("Lastname")

    if st.button("Register"):
        result = register(username, email, password, first_Name, last_Name)
        if result is True:
            st.success("Registration successful! Please log in.")
            st.session_state.page = "login" 
        elif result and isinstance(result, dict):
            st.error(f"Error: {result}")
        else:
            st.error("An error occurred. Please try again.")

    if st.button("Login here"):
        st.session_state.page = "login"


def user_detail_ui():
    st.title("User Details")

    access_token = st.session_state.get("access_token")
    
    if access_token:
        user_details = get_user_details(access_token)
        if user_details:
            st.write(f"Username: {user_details['username']}")
            st.write(f"Email: {user_details['email']}")
        else:
            st.error("Failed to fetch user details. Please try again.")
    else:
        st.error("You are not logged in.")

    if st.button("Logout"):
        st.session_state.pop("access_token")
        st.session_state.pop("refresh_token")
        st.session_state.page = "login"
        st.success("You have logged out.")


def main():
    if "page" not in st.session_state:
        st.session_state.page = "login" 

    if st.session_state.page == "login":
        login_ui()
    
    if st.session_state.page == "user_detail":
        user_detail_ui()
    
    elif st.session_state.page == "register":
        register_ui()

if __name__ == "__main__":
    main()
