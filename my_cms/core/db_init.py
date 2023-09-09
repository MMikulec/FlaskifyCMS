from flask_security.utils import hash_password
from .schemas import (
    get_content_type_schema,
    get_system_settings_schema,
    get_role_schema,
    get_user_schema
)


def initialize_db(mongo):
    # Create 'ContentTypes' Collection and Add Sample Data
    article_schema = get_content_type_schema("Article", [
        {"name": "title", "type": "string"},
        {"name": "content", "type": "text"},
        {"name": "image", "type": "image"}
    ])

    post_schema = get_content_type_schema("Post", [
        {"name": "title", "type": "string"},
        {"name": "content", "type": "text"}
    ])

    mongo.db.ContentTypes.insert_many([article_schema, post_schema])

    # Create 'Contents' Collection (Empty for Now)
    mongo.db.create_collection('Contents')

    # Initialize System Settings
    system_settings = get_system_settings_schema()
    mongo.db.Settings.insert_one(system_settings)

    # Create 'Roles' Collection and Add Roles
    roles_data = [
        get_role_schema("admin", "Administrator"),
        get_role_schema("editor", "Editor"),
        get_role_schema("viewer", "Viewer")
    ]
    mongo.db.Roles.insert_many(roles_data)

    # Fetch admin role ID
    admin_role_id = mongo.db.Roles.find_one({"name": "admin"})["_id"]

    # Create 'Users' Collection and Add Admin User
    admin_user = get_user_schema("admin", "admin@example.com", "admin_password", admin_role_id)
    mongo.db.Users.insert_one(admin_user)
