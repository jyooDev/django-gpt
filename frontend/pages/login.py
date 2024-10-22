import streamlit as st
from api.auth import login
from pages.register import main as register_main

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

def main():
    login_ui()

if __name__ == "__main__":
    main()