import streamlit as st
from api.auth import register
    

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