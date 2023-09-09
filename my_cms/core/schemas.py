#  Copyright (c) 2023. Marek Mikulec
# schemas.py

from flask_security.utils import hash_password
import uuid


def get_content_type_schema(name, fields):
    return {
        "name": name,
        "fields": fields
    }


def get_system_settings_schema():
    return {
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


def get_role_schema(name, description):
    return {
        "name": name,
        "description": description
    }


def get_user_schema(username, email, password, role_id):
    return {
        "username": username,
        "email": email,
        "password": hash_password(password),
        "fs_uniquifier": str(uuid.uuid4()),
        "active": True,
        "roles": [role_id],
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
