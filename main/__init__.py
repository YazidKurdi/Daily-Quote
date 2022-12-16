from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()

from main.app_page.routes import app_page

app.register_blueprint(app_page)
# app.register_blueprint(posts)
# app.register_blueprint(util)
