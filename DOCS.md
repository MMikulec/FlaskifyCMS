
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

## ASCII Representation

```
ContentTypes Collection
-------------------------
| _id |     name     |                fields                  |

Contents Collection
----------------------------------------------------------
| _id | type_id |           data           | author_id | created_at | updated_at |

Users Collection
-------------------------------
| _id | username | email | password_hash | role |
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
