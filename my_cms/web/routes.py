"""
web/routes.py

This module defines the web routes for server-side rendering using Jinja2 templates.

Routes:
- GET, POST /posts: Display all posts or create a new post via form submission.
"""

from flask import Blueprint, render_template

web = Blueprint('web', __name__)

@web.route('/', methods=['GET'])
def index():
    return "OK"

@web.route('/posts', methods=['GET'])
def posts():
    return render_template('scratch.jinja2', title='All Posts')
