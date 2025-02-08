from flask import Flask
from flask_wtf import CSRFProtect

def create_app(testing: bool = False):
    app = Flask(__name__)
    app.testing = testing
    app.secret_key = "secret_key"
    CSRFProtect(app)

    return app
