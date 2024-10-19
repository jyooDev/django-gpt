import streamlit as st
from pages.login_page import login_ui
from pages.user_detail_page import user_detail_ui
from pages.register_page import register_ui

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
