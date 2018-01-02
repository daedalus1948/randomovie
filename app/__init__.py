from flask import Flask

# initialize the flask application object
app = Flask(__name__)
print("app initialized - __init__.py")

from app import controllers

# configurate the application based on config.py
app.config.from_object('config')

# set sqlite database file path
db_utils.set_DB_PATH('movies.db')
