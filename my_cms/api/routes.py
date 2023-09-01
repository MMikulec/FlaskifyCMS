"""
api/routes.py

This module defines the API endpoints for the application.

Endpoints:
- GET /api/posts: Fetch all posts as a JSON response.
- POST /api/posts: Create a new post from JSON payload.
"""

from flask import Blueprint, jsonify, Response
import my_cms.core as core

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({"message": "All posts from API"})

