"""
web/routes.py

This module defines the web routes for server-side rendering using Jinja2 templates.

Routes:
- GET, POST /posts: Display all posts or create a new post via form submission.
"""

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_security import login_user, current_user
from bson import ObjectId
from .forms import UserCreateForm
import my_cms.core as core
import os

template_dir = os.path.abspath('templates')
web = Blueprint('web', __name__, template_folder=template_dir)


@web.route('/', methods=['GET'])
def index():
    return "OK"


@web.route('/posts', methods=['GET'])
def posts():
    return render_template('scratch.jinja2', title='All Posts')


@web.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserCreateForm()

    # Populate role choices
    roles = core.mongo.db.Roles.find()
    form.role.choices = [(str(role['_id']), role['name']) for role in roles]

    if form.validate_on_submit():
        kwargs = {
            'email': form.email.data,
            'username': form.username.data,
            'password': form.password.data,
            'role': ObjectId(form.role.data)
        }

        # Create the user
        # new_user = core.user_datastore.create_user(**kwargs)
        new_user = core.do_create_user(**kwargs)

        # Redirect to a new page after successfully creating the user
        return redirect(url_for('web.index'))  # Replace 'web.index' with your index route

    return render_template('signup.jinja2', form=form)


@web.route('/info')
def info():
    if current_user.is_authenticated:
        return f"Hello, {current_user.email} {current_user.password}"
    else:
        return "You are not logged in."
