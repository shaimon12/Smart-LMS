# app/teacher_panel.py

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import json
from datetime import datetime
from utils.auth import check_login, update_password
from utils.file_utils import save_uploaded_file, convert_to_txt, embed_txt_to_chroma

def show_teacher_panel():
    st.title("Teacher Panel")

    username = st.session_state.get("username")
    user_id = st.session_state.get("user_id")

    if not username or not user_id:
        st.warning("Please login to continue.")
        return

    # === Load assigned courses ===
    with open("config/users.json", "r") as f:
        user_data = json.load(f)

    assigned_courses = []
    for user in user_data:
        if (user.get("username") == username or user.get("id") == user_id) and user.get("role") == "teacher":
            assigned_courses = user.get("courses", [])
            break

    if not assigned_courses:
        st.warning("You are not assigned to any course. Please contact the admin.")
        return

    selected_course = st.selectbox("Select a course", options=assigned_courses)
    DATA_PATH = f"data/{selected_course}"
    CHROMA_PATH = f"chroma_db/{selected_course}"
    CONTENT_TYPES = ["lectures", "practicals", "assignments"]

    # === Upload Course Materials ===
    st.subheader("Upload Course Content")
    content_type = st.selectbox("Select content type", CONTENT_TYPES)
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

    if st.button("Upload") and uploaded_files:
        for uploaded_file in uploaded_files:
            try:
                raw_path = save_uploaded_file(uploaded_file, DATA_PATH, content_type)
                txt_path = convert_to_txt(raw_path)
                embed_txt_to_chroma(txt_path, CHROMA_PATH)
                st.success(f"✅ Uploaded and embedded successfully: {uploaded_file.name}")
            except Exception as e:
                st.error(f"❌ Failed to process {uploaded_file.name}: {e}")

    # === View, Download, and Delete Uploaded Files ===
    st.subheader(f"{content_type.capitalize()} Files")
    content_dir = os.path.join(DATA_PATH, content_type)
    if os.path.exists(content_dir):
        files = os.listdir(content_dir)
        if files:
            for file in files:
                file_path = os.path.join(content_dir, file)
                with open(file_path, "rb") as f:
                    st.download_button(label=f"⬇️ Download {file}", data=f, file_name=file, key=f"download_{file}")

                if st.button(f"🗑️ Delete {file}", key=f"delete_{file}"):
                    os.remove(file_path)
                    st.success(f"{file} deleted successfully.")
                    st.rerun()
        else:
            st.info("No files uploaded yet.")
    else:
        st.info("This content type folder has not been created yet.")

    # === Assignment Deadlines ===
    if content_type == "assignments":
        st.subheader("Add Assignment Deadline")
        assignment_name = st.text_input("Assignment Title")
        deadline = st.date_input("Deadline Date")

        if st.button("Save Deadline") and assignment_name:
            deadline_data = {
                "title": assignment_name,
                "due_date": deadline.strftime("%Y-%m-%d")
            }
            deadline_file = os.path.join(DATA_PATH, "deadlines.json")
            if os.path.exists(deadline_file):
                with open(deadline_file, "r") as f:
                    existing = json.load(f)
            else:
                existing = []

            existing.append(deadline_data)
            with open(deadline_file, "w") as f:
                json.dump(existing, f, indent=4)

            st.success("Deadline saved!")

    # === Announcements ===
    st.subheader("Post Course Announcement")
    title = st.text_input("Announcement Title")
    message = st.text_area("Announcement Message")
    if st.button("Post Announcement"):
        if title and message:
            announcement = {
                "title": title,
                "message": message,
                "author": username,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            announcement_file = os.path.join(DATA_PATH, "announcements.json")
            if os.path.exists(announcement_file):
                with open(announcement_file, "r") as f:
                    existing = json.load(f)
            else:
                existing = []

            existing.append(announcement)
            with open(announcement_file, "w") as f:
                json.dump(existing, f, indent=4)

            st.success("Announcement posted!")
        else:
            st.warning("Please provide both title and message.")

    # === Change Password ===
    st.subheader("Change Your Password")
    current_pwd = st.text_input("Current Password", type="password", key="teacher_current_pwd")
    new_pwd = st.text_input("New Password", type="password", key="teacher_new_pwd")
    confirm_pwd = st.text_input("Confirm New Password", type="password", key="teacher_confirm_pwd")

    if st.button("Update Password"):
        if not check_login(username, current_pwd):
            st.error("Current password is incorrect.")
        elif new_pwd != confirm_pwd:
            st.error("New passwords do not match.")
        elif not new_pwd.strip():
            st.error("New password cannot be empty.")
        else:
            update_password(username, new_pwd)
            st.success("Password updated successfully.")
