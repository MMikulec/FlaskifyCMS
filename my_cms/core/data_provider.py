"""
core/data_provider.py

This module serves as a data provider for the application. It contains
functions to interact with the MongoDB database to perform CRUD operations
on posts.

Functions:
- get_posts(): Fetch all posts from the database.
- create_post(title, content): Create a new post in the database.
- update_post(post_id, title, content): Update an existing post in the database.
- delete_post(post_id): Delete a post from the database.
"""
from flask_pymongo import PyMongo


class ContentService:
    def __init__(self, db: PyMongo):
        if not isinstance(db, PyMongo):
            raise TypeError("db must be an instance of PyMongo")
        self.db = db
