import random

from flask import Blueprint, redirect, render_template

from flaskr.database import Database

web_blueprint = Blueprint("web", __name__)


@web_blueprint.route("/", methods=["GET"])
def random_question():
    database = Database()
    database.cursor.execute(
        "SELECT question_id FROM question ORDER BY RANDOM() LIMIT 1;"
    )

    question_data = database.cursor.fetchone()
    return redirect(f"/{question_data['question_id']}")


@web_blueprint.route("/<string:question_id>", methods=["GET"])
def specific_question(question_id: str):
    database = Database()
    database.cursor.execute(
        "SELECT * FROM question WHERE question_id = ?;", (question_id,)
    )
    question_data = database.cursor.fetchone()

    database.cursor.execute(
        "SELECT * FROM answer WHERE question_id = ?;", (question_id,)
    )
    answers_data = database.cursor.fetchall()
    random.shuffle(answers_data)

    return render_template("index.html", question=question_data, answers=answers_data)
