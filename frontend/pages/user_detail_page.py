import streamlit as st
from api.user import get_user_details

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
