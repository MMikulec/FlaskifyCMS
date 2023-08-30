from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from .db_init import initialize_db

# Import the blueprints here to avoid circular imports
from my_cms.web.routes import web as web_blueprint
from my_cms.api.routes import api as api_blueprint
from my_cms.main.routes import main as main_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Combine URI and DB_NAME
app.config["MONGO_URI"] = f"{Config.MONGO_URI}{Config.MONGO_DB_NAME}?authSource=admin"
mongo = PyMongo(app)


# Function to check if the database is empty
def is_db_empty():
    return mongo.db.ContentTypes.count_documents({}) == 0


@app.before_request
def before_first_request():
    if is_db_empty():
        initialize_db(mongo)


app.register_blueprint(web_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(main_blueprint)
