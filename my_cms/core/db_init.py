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
            "name": "Post",
            "fields": [
                {"name": "title", "type": "string"},
                {"name": "content", "type": "text"}
            ]
        }
    ]
    mongo.db.ContentTypes.insert_many(content_types_data)

    # Create 'Contents' Collection (Empty for Now)
    mongo.db.create_collection('Contents')

    # Initialize System Settings
    system_settings = {
        "_id": "system",
        "general": {
            "siteName": "My Awesome CMS",
            "siteDescription": "This is an awesome CMS",
            "maintenanceMode": False,
            "timezone": "UTC"
        },
        "api": {
            "rateLimit": 1000,
            "accessRestrictions": []
        },
        "modules": {
            "activeModules": ["blog", "forum"]
        }
    }
    mongo.db.Settings.insert_one(system_settings)

    # Create 'Users' Collection and Add Admin User with Settings
    admin_user = {
        "username": "admin",
        "email": "admin@example.com",
        "password_hash": "hashed_password_here",
        "role": "admin",
        "settings": {
            "dashboard": {
                "widgetLayout": ["widget1", "widget2", "widget3"]
            },
            "notifications": {
                "email": True,
                "push": False
            },
            "account": {
                "language": "en-US",
                "privacy": "public"
            }
        }
    }
    mongo.db.Users.insert_one(admin_user)
