import os

from flask import Flask
from flask_wtf import CSRFProtect

from flaskr.database import create_database
from flaskr.web import web_blueprint
from flaskr.api import api_blueprint


def create_app(testing: bool = False):
    app = Flask(__name__)
    app.testing = testing
    app.secret_key = "secret_key"
    CSRFProtect(app)

    if not os.path.isfile("database.db"):
        print("created empty database")
        create_database()

    app.register_blueprint(web_blueprint)
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
