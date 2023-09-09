class Config:
    MONGO_URI = 'mongodb://root:rootpassword@localhost:27017/'
    MONGO_DB_NAME = 'cms_db'

    # ... flask security ...
    SECRET_KEY = 'my_super_secret_key'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'some_arbitrary_super_secret_string'