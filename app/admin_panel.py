import streamlit as st
import os
import json
from utils.auth import check_login, update_password

def show_admin_panel():
    USERS_FILE = "config/users.json"
    COURSES_FILE = "config/courses.json"
    DATA_FOLDER = "data"
    CHROMA_FOLDER = "chroma_db"

    st.title("Admin Panel")

    os.makedirs("config", exist_ok=True)
    os.makedirs(DATA_FOLDER, exist_ok=True)
    os.makedirs(CHROMA_FOLDER, exist_ok=True)

    # Load users
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            users = json.load(f)
    else:
        users = []

    # Load courses
    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "r") as f:
            courses = json.load(f)
    else:
        courses = []

    # === Change Password ===
    st.subheader("Change Your Password")
    current_user = st.session_state.get("username") or st.session_state.get("id")
    current_pwd = st.text_input("Current Password", type="password")
    new_pwd = st.text_input("New Password", type="password")
    confirm_pwd = st.text_input("Confirm New Password", type="password")

    if st.button("Update Password"):
        if not check_login(current_user, current_pwd):
            st.error("Current password is incorrect.")
        elif new_pwd != confirm_pwd:
            st.error("New passwords do not match.")
        elif not new_pwd.strip():
            st.error("New password cannot be empty.")
        else:
            update_password(current_user, new_pwd)
            st.success("Password updated successfully.")

    # === Create New Course ===
    st.subheader("Create a New Course")
    course_code = st.text_input("Course Code (e.g., COMP8420)")
    course_name = st.text_input("Course Name (optional)")

    if st.button("Create Course"):
        if course_code:
            course_path = os.path.join(DATA_FOLDER, course_code)
            chroma_path = os.path.join(CHROMA_FOLDER, course_code)
            os.makedirs(course_path, exist_ok=True)
            os.makedirs(chroma_path, exist_ok=True)

            for fname in ["announcements.json", "deadlines.json"]:
                fpath = os.path.join(course_path, fname)
                if not os.path.exists(fpath):
                    with open(fpath, "w") as f:
                        json.dump([], f)

            if not any(c["code"] == course_code for c in courses):
                courses.append({"code": course_code, "name": course_name})
                with open(COURSES_FILE, "w") as f:
                    json.dump(courses, f, indent=4)

            st.success(f"Course {course_code} created.")
        else:
            st.warning("Please enter a valid course code.")

    # === Create & Assign New User ===
    st.subheader("Create & Assign New User")

    if not courses:
        st.info("Please create a course first before assigning users.")
    else:
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        role = st.selectbox("Select Role", ["teacher", "student"])
        available_courses = [c["code"] for c in courses]
        course_to_assign = st.selectbox("Select Course", options=available_courses)

        if st.button("Assign Course"):
            if first_name and last_name and role and course_to_assign:
                cleaned_name = f"{first_name}{last_name}".lower().replace(" ", "")
                existing_ids = [int(u.get("id", 1000)) for u in users]
                next_id = max(existing_ids, default=1000) + 1

                generated_username = f"{cleaned_name}{next_id}.{role}@lms.edu"

                updated = False
                for user in users:
                    if user["username"] == generated_username and user["role"] == role:
                        if course_to_assign not in user.get("courses", []):
                            user.setdefault("courses", []).append(course_to_assign)
                            updated = True
                        break

                if not updated:
                    users.append({
                        "id": str(next_id),
                        "username": generated_username,
                        "password": "password123",
                        "role": role,
                        "courses": [course_to_assign]
                    })

                with open(USERS_FILE, "w") as f:
                    json.dump(users, f, indent=4)

                st.success(f"User {generated_username} assigned to {course_to_assign} as {role}.")
            else:
                st.warning("Please provide all details.")

    # === View All Users ===
    st.subheader("Current Users")
    if users:
        for u in users:
            st.markdown(
                f"- **{u.get('username')}** (ID: {u.get('id')}) — {u['role']}, "
                f"Courses: {', '.join(u.get('courses', []))}"
            )
    else:
        st.info("No users found.")

    # === View All Courses ===
    st.subheader("Current Courses")
    if courses:
        for c in courses:
            name_display = f" - {c['name']}" if c.get("name") else ""
            st.markdown(f"- **{c['code']}**{name_display}")
    else:
        st.info("No courses created yet.")
