from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
app.config['SECRET_KEY'] = os.environ.get('0PY_SECRET_KEY')
app.SQLALCHEMY_TRACK_MODIFICATIONS = False
app.DEBUG = False
db = SQLAlchemy(app)

from new_app import routes
