from flask_security import verify_password
from flask_security import login_user, logout_user, current_user

from my_cms.core.app import (user_datastore,
                             mongo)


def do_login_user(email, password):
    # user_datastore = PyMongoUserDatastore()
    user = user_datastore.find_user(email=email)

    if not user or not verify_password(password, user.password):
        return None

    login_user(user)
    return user


def do_handle_logout_user():
    logout_user()
    return not current_user.is_authenticated  # True if logout was successful, False otherwise


def do_create_user(**kwargs):
    return user_datastore.create_user(**kwargs)
