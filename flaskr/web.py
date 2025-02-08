from http import HTTPStatus

from flask import Blueprint, render_template

from flaskr.database import Database

web_blueprint = Blueprint("web", __name__)


@web_blueprint.route("/", methods=["GET"])
def random_question():
    database = Database()
    database.cursor.execute(
        "SELECT question_id FROM question ORDER BY RANDOM() LIMIT 1;"
    )

    # only possible if there are no questions
    if (question_data := database.cursor.fetchone()) is None:
        return "", HTTPStatus.NOT_FOUND

    return specific_question(question_data["question_id"])


@web_blueprint.route("/<string:question_id>", methods=["GET"])
def specific_question(question_id: str):
    database = Database()
    database.cursor.execute(
        "SELECT * FROM question WHERE question_id = ?;", (question_id,)
    )

    if (question_data := database.cursor.fetchone()) is None:
        return "", HTTPStatus.NOT_FOUND

    database.cursor.execute(
        "SELECT * FROM answer WHERE question_id = ?;", (question_id,)
    )
    answers_data = database.cursor.fetchall()

    return render_template("index.html", question=question_data, answers=answers_data)
