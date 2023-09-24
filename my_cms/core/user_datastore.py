# user_datastore.py
import uuid

from flask_security.datastore import UserDatastore
from flask_security import UserMixin, RoleMixin
from flask_security.utils import hash_password
from .schemas import (
    get_content_type_schema,
    get_system_settings_schema,
    get_role_schema,
    get_user_schema
)


class Role(dict, RoleMixin):
    pass


"""class User(dict, UserMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self['fs_uniquifier'] = str(self.get('_id', ''))

    def get_id(self):
        return str(self.get('_id', ''))

    def log_activity(self):
        # Just an example. You can write code here to log user activity.
        print(f"User {self.get('email', 'Unknown')} is active.")

    @property
    def fs_uniquifier(self):
        return str(self.get('_id', ''))


class UserWrapperOld(UserMixin):
    def __init__(self, user_dict):
        self.user_dict = user_dict

    @property
    def id(self):
        return str(self.user_dict.get('_id', ''))

    @property
    def email(self):
        return self.user_dict.get('email', '')

    @property
    def password(self):
        return self.user_dict.get('password', '')

    @property
    def fs_uniquifier(self):
        return str(self.user_dict.get('_id', ''))

    @property
    def active(self):
        return self.user_dict.get('active', True)  # Assuming True if 'active' not present
    # Add other attributes and methods as needed"""


class User(UserMixin):
    def __init__(self, user_dict):
        self.user_dict = user_dict

    id = property(lambda self: str(self.user_dict.get('_id', '')))
    email = property(lambda self: self.user_dict.get('email', ''))
    password = property(lambda self: self.user_dict.get('password', ''))
    fs_uniquifier = property(lambda self: str(self.user_dict.get('_id', '')))
    active = property(lambda self: self.user_dict.get('active', True))

    """def __getattr__(self, name):
        if name in ['id', 'email', 'password', 'fs_uniquifier', 'active']:
            return self.user_dict.get(name, '')
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")"""


class PyMongoUserDatastore(UserDatastore):
    def __init__(self, db, user_model, role_model):
        self.db = db
        super().__init__(user_model, role_model)

    def find_user(self, **kwargs):
        query_keys = ['email', 'username']
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in query_keys}

        data = self.db.Users.find_one(filtered_kwargs)
        if data:
            print(data)
            # user = User(**data)   Create an instance of the User class
            return User(data)
        else:
            return None

    def create_user(self, **kwargs):
        user_data = get_user_schema(
            kwargs.get('username', ''),
            kwargs.get('email', ''),
            kwargs.get('password', ''),
            kwargs.get('role', None)  # Here, get the role from the form data
        )

        # user_data.update(kwargs)
        user_id = self.db.Users.insert_one(user_data).inserted_id
        user_data['_id'] = user_id
        return User(user_data)

    def commit(self):
        pass  # PyMongo writes are committed automatically

    def get_all_users(self):
        users = self.db.Users.find()
        return [User(user_data) for user_data in users]
