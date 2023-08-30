def initialize_db(mongo):
    # Create 'ContentTypes' Collection and Add Sample Data
    content_types_data = [
        {
            "name": "Article",
            "fields": [
                {"name": "title", "type": "string"},
                {"name": "content", "type": "text"},
                {"name": "image", "type": "image"}
            ]
        },
        {
            "name": "Blog",
            "fields": [
                {"name": "title", "type": "string"},
                {"name": "content", "type": "text"}
            ]
        }
    ]
    mongo.db.ContentTypes.insert_many(content_types_data)

    # Create 'Contents' Collection (Empty for Now)
    mongo.db.create_collection('Contents')

    # Create 'Users' Collection and Add Admin User
    admin_user = {
        "username": "admin",
        "email": "admin@example.com",
        "password_hash": "hashed_password_here",
        "role": "admin"
    }
    mongo.db.Users.insert_one(admin_user)
