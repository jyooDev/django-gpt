import streamlit as st
from pages.login import main as login_main
from pages.user_detail import main as user_detail_main
from pages.register import main as register_main

def main():
    st.title("Welcome to This App")

    if "access_token" in st.session_state:
        st.write(f"Hello, {st.session_state.get('username', 'User')}! Here are your conversations:")
        # conversation_ui()  # Show conversation history if logged in
if __name__ == "__main__":
    main()
