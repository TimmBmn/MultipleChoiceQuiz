from flask import Blueprint

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/", methods=["GET"])
def index():
    return "TODO"
