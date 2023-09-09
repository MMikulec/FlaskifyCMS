import pkgutil
import importlib

from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from flask_security import Security
from .db_init import initialize_db

# Import the blueprints here to avoid circular imports
from my_cms.web import web as web_blueprint
from my_cms.api import api as api_blueprint

# Initialize Flask-Security
from .user_datastore import PyMongoUserDatastore
from .user_datastore import User
from .user_datastore import Role

app = Flask(__name__)
app.config.from_object(Config)

# Combine URI and DB_NAME
app.config["MONGO_URI"] = f"{Config.MONGO_URI}{Config.MONGO_DB_NAME}?authSource=admin"
mongo = PyMongo(app)


user_datastore = PyMongoUserDatastore(mongo.db, User, Role)
security = Security(app, user_datastore)


# Function to check if the database is empty
def is_db_empty():
    return mongo.db.ContentTypes.count_documents({}) == 0


@app.before_request
def before_first_request():
    if is_db_empty():
        print("Initialize database")
        initialize_db(mongo)


# Dynamically import all modules in the 'modules' package
def load_modules(my_app):
    # Fetch active modules from MongoDB Settings collection
    settings = mongo.db.Settings.find_one({"_id": "system"})
    active_modules = settings.get('modules', {}).get('activeModules', []) if settings else []

    print(f"Active Modules from DB: {active_modules}")

    # Dynamically load modules
    for _, module_name, _ in pkgutil.iter_modules(['modules']):
        print(f"Checking module: {module_name}")
        if module_name in active_modules and module_name not in my_app.blueprints:
            module = importlib.import_module(f'modules.{module_name}')
            if hasattr(module, 'bp'):
                print(f"Loading module: {module_name}")
                my_app.register_blueprint(module.bp)


load_modules(app)
app.register_blueprint(web_blueprint)
app.register_blueprint(api_blueprint)
print(f"Running modules: {app.blueprints}")
print(app.url_map)
