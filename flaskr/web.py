from flask import Blueprint, render_template

from flaskr import logic

web_blueprint = Blueprint("web", __name__)


@web_blueprint.route("/", methods=["GET"])
def random_question():
    question_data, answers_data = logic.random_question()
    return render_template("index.html", question=question_data, answers=answers_data)


@web_blueprint.route("/<string:question_id>", methods=["GET"])
def specific_question(question_id: str):
    question_data, answers_data = logic.specific_question(question_id)
    return render_template("index.html", question=question_data, answers=answers_data)
