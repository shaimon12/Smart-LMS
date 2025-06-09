# utils/auth.py

import json
import os

USERS_FILE = "config/users.json"

def check_login(username_or_id, password):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    for user in users:
        if (user.get("username") == username_or_id or user.get("id") == username_or_id) and user.get("password") == password:
            return True
    return False

def get_user_role(username_or_id):
    if not os.path.exists(USERS_FILE):
        return None
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    for user in users:
        if user.get("username") == username_or_id or user.get("id") == username_or_id:
            return user.get("role")
    return None

def update_password(username_or_id, new_password):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    updated = False
    for user in users:
        if user.get("username") == username_or_id or user.get("id") == username_or_id:
            user["password"] = new_password
            updated = True
            break
    if updated:
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
    return updated

def get_user_object(username_or_id):
    if not os.path.exists(USERS_FILE):
        return None
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    for user in users:
        if user.get("username") == username_or_id or user.get("id") == username_or_id:
            return user
    return None
