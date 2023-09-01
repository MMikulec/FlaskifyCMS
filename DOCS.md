# MongoDB Collections for Dynamic CMS

## Collections

### 1. ContentTypes Collection
- `_id`: Unique identifier for each content type
- `name`: The name of the content type (e.g., "Article", "Blog", "News")
- `fields`: An array of field objects that define the structure of this content type

### 2. Contents Collection
- `_id`: Unique identifier for each content
- `type_id`: Reference to the content type this content belongs to
- `data`: An object containing key-value pairs for each field defined in the content type
- `author_id`: Reference to the user who created the content
- `created_at`: Timestamp when the content was created
- `updated_at`: Timestamp when the content was last updated

### 3. Users Collection
- `_id`: Unique identifier for each user
- `username`: Username of the user
- `email`: Email of the user
- `password_hash`: Hashed password for security
- `role`: Role of the user (e.g., admin, editor, viewer)
- `settings`: Object containing user-specific settings

### 4. Settings Collection
- `_id`: Identifier for each setting group ("system" for system-wide settings)
- `general`: Object containing general settings like site name, description, etc.
- `api`: Object containing API-related settings
- `modules`: Object containing active module names

## ASCII Representation

```
ContentTypes Collection
-------------------------
| _id |     name     |                fields                  |

Contents Collection
----------------------------------------------------------
| _id | type_id |           data           | author_id | created_at | updated_at |

Users Collection
--------------------------------------------------------
| _id | username | email | password_hash | role | settings |

Settings Collection
-----------------------------------------
| _id | general | api | modules |
```

## Example Document for ContentTypes

```json
{
  "_id": "some_id",
  "name": "Article",
  "fields": [
    { "name": "title", "type": "string" },
    { "name": "content", "type": "text" },
    { "name": "image", "type": "image" }
  ]
}
```

## Example Document for Contents

```json
{
  "_id": "some_content_id",
  "type_id": "some_id",
  "data": {
    "title": "My Article",
    "content": "This is the content of my article.",
    "image": "/path/to/image.jpg"
  },
  "author_id": "some_author_id",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## Example Document for Users

```json
{
  "_id": "user_id",
  "username": "JohnDoe",
  "email": "john@example.com",
  "password_hash": "hashed_password",
  "role": "admin",
  "settings": {
    "dashboard": {
      "widgetLayout": ["widget1", "widget2"]
    },
    "notifications": {
      "email": true,
      "push": false
    },
    "account": {
      "language": "en-US",
      "privacy": "public"
    }
  }
}
```

## Example Document for Settings

```json
{
  "_id": "system",
  "general": {
    "siteName": "My Awesome CMS",
    "siteDescription": "This is an awesome CMS",
    "maintenanceMode": false,
    "timezone": "UTC"
  },
  "api": {
    "rateLimit": 1000,
    "accessRestrictions": []
  },
  "modules": {
    "activeModules": ["Blog", "Forum"]
  }
}
