from flask import Blueprint

web_blueprint = Blueprint("web", __name__)

@web_blueprint.route("/", methods=["GET"])
def index():
    return "TODO"
