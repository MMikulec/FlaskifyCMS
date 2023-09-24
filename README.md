# My CMS Project

## Description

This is a Content Management System (CMS) built with Python using Flask and MongoDB. The project aims to provide a flexible and extendable platform for content management, including user authentication, role-based access control, and various content types.

## Features

- User Authentication
  - Login
  - Logout
  - Role-based Access Control
  
- Content Management
  - Create, Read, Update, Delete (CRUD) operations for various content types
  
- API Support
  - JSON API for integration with other platforms and services
  
## Installation

Clone the repository and navigate into the project directory.

```bash
git clone https://github.com/MMikulec/FlaskifyCMS.git
```

Install the required Python packages.

```bash
pip install -r requirements.txt
```

Run the project.

```bash
python run.py
```

## Usage

After running the project, navigate to `http://localhost:5000` in your web browser to access the CMS.

## Contributing

If you would like to contribute, please fork the repository and submit your changes via a pull request.

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
```

# Git Branching Strategy for Dynamic CMS Project

## Branching Overview

Our project employs a structured Git branching strategy to ensure that the codebase remains clean and organized. Here are the main types of branches we'll be working with:

### Main Branches

- **`main`:** Production-ready code resides here.
- **`develop`:** Development code resides here. All feature branches branch off from here.

### Supporting Branches

- **Feature Branches:** For new features and non-emergency bugfixes.
- **Release Branches:** For final tasks before a production release.
- **Hotfix Branches:** For urgent production fixes.

---

## Branch Naming Conventions

### Feature Branches

- Prefix: `develop/feature/`
- Example: `develop/feature/user-authentication`

### Version Branches

- Prefix: `release/`
- Example: `release/v1.0.0`

### Hotfix Branches

- Prefix: `hotfix/`
- Example: `hotfix/v1.0.1`

### Experimental/Research Branches

- Prefix: `experiment/` or `research/`
- Example: `experiment/new-algorithm`

---

## Git Commands

### Creating a New Feature Branch

```bash
# Switch to the develop branch
git checkout develop

# Create and switch to a new feature branch
git checkout -b develop/feature/user-authentication
```

### Creating a New Version Branch

```bash
# Switch to the develop branch
git checkout develop

# Create and switch to a new release branch
git checkout -b release/v1.0.0
```

### Creating a Hotfix Branch

```bash
# Switch to the main branch
git checkout main

# Create and switch to a new hotfix branch
git checkout -b hotfix/v1.0.1
```

---

## Merging Strategy

- Merge feature branches back into `develop` once the feature is complete.
- Merge `develop` into `main` via a release branch when the release is ready.
- Merge hotfix branches into both `main` and `develop`.

By adhering to this branching strategy, we can ensure a clean and manageable codebase.
