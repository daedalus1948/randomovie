# app/__init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
print("app initialized - __init__.py")

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

# set sqlite database file path
db_utils.set_DB_PATH('movies.db')
