"""
api/routes.py

This module defines the API endpoints for the application.

Endpoints:
- GET /api/posts: Fetch all posts as a JSON response.
- POST /api/posts: Create a new post from JSON payload.
"""

from flask import Blueprint, jsonify, Response, request
from flask_security import login_user, logout_user, current_user
from flask_security.utils import verify_password
import my_cms.core as core

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({"message": "All posts from API"})


@api.route('/login', methods=['POST'])
def api_login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = core.do_login_user(email, password)

    if user is None:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Logged in", "user_id": str(user.id)})


@api.route('/logout', methods=['POST'])
def api_logout():
    if core.do_handle_logout_user():
        return jsonify({"message": "Logout"})  # Logout was successful
    else:
        return jsonify({"error": "Logout error"})  # Logout failed


@api.route('/create_user', methods=['POST'])
def api_create_user():
    role_name = request.json.get('role')

    kwargs = {
        'email': request.json.get('email'),
        'username': request.json.get('username'),
        'password': request.json.get('password'),
        'role': core.mongo.db.Roles.find_one({"name": role_name})["_id"]
    }

    new_user = core.do_create_user(**kwargs)
    return jsonify({"message": "Created user"})


@api.route('/info', methods=['GET'])
def api_info():
    if not current_user.is_authenticated:
        return jsonify({"error": "Not logged in"}), 401

    user_info = {
        "user_id": str(current_user.id),
        "email": current_user.email,
        # "roles": current_user.roles  # This assumes that the user object has a 'roles' field
        # Add more fields as needed
    }

    return jsonify({"message": "User Info", "user_info": user_info})


@api.route('/users', methods=['GET'])
def api_get_all_users():
    users = core.get_all_users()  # or core.user_datastore.get_all_users() based on where you put it
    user_list = []

    # Loop through the list of User objects
    for user in users:
        user_dict = {
            "User ID": user.id,
            "Email": user.email,
            "Password": user.password,
            "Is Active": user.active
            # Add any other attributes you have
        }
        user_list.append(user_dict)

    # Convert to JSON
    return jsonify(user_list)
