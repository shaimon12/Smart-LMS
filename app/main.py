# app/main.py

import streamlit as st
from datetime import datetime, timedelta
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import utility functions and routing
from utils.auth import check_login, get_user_role, get_user_object
from utils.routing import show_student_panel, show_teacher_panel, show_admin_panel

# Session timeout configuration
SESSION_TIMEOUT_MINUTES = 30

# Page setup
st.set_page_config(page_title="Smart LMS Assistant", layout="wide")
st.title("Smart LMS Assistant")

# Check session timeout
def session_expired():
    if "last_active" in st.session_state:
        elapsed = datetime.now() - st.session_state["last_active"]
        return elapsed > timedelta(minutes=SESSION_TIMEOUT_MINUTES)
    return False

# Show login form
from utils.auth import check_login, get_user_role, get_user_object

def show_login_form():
    st.sidebar.header("Login")
    with st.sidebar.form("login_form"):
        username_or_id = st.text_input("Username or ID")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted and username_or_id and password:
            if check_login(username_or_id, password):
                user = get_user_object(username_or_id)
                st.session_state["username"] = user.get("username")
                st.session_state["user_id"] = user.get("id")
                st.session_state["role"] = user.get("role")
                st.session_state["logged_in"] = True
                st.session_state["last_active"] = datetime.now()
                st.rerun()
            else:
                st.error("Invalid credentials.")

# Handle login or expired session
if not st.session_state.get("logged_in") or session_expired():
    for key in ["username", "user_id", "role", "logged_in", "last_active"]:
        st.session_state.pop(key, None)
    show_login_form()
else:
    st.session_state["last_active"] = datetime.now()
    role = st.session_state["role"]
    username = st.session_state["username"]

    st.sidebar.success(f"Logged in as {role.capitalize()}")
    if st.sidebar.button("Logout"):
        for key in ["username", "user_id", "role", "logged_in", "last_active"]:
            st.session_state.pop(key, None)
        st.rerun()

    # Route to appropriate dashboard
    if role == "student":
        show_student_panel()
    elif role == "teacher":
        show_teacher_panel()
    elif role == "admin":
        show_admin_panel()
