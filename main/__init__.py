from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

app = Flask(__name__)
db = SQLAlchemy(app)
scheduler = APScheduler()

from main.app_page.routes import app_page

app.register_blueprint(app_page)
# app.register_blueprint(posts)
# app.register_blueprint(util)
