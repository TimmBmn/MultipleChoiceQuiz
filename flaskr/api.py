from flask import Blueprint, Response, render_template, request

from flaskr import logic
from flaskr.database import Database

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/random_question", methods=["GET"])
def random_question():
    question_data, answers_data = logic.random_question()

    response = Response(
        render_template("question.html", question=question_data, answers=answers_data)
    )
    if question_data is not None:
        response.headers.add("HX-Replace-Url", f"/{question_data['question_id']}")
    return response


@api_blueprint.route("/correct_answers", methods=["GET"])
def correct_answers():
    # TODO None handling
    question_id = request.args.get("question_id")
    selected_answers_id = request.args.getlist("answers[]")

    ordering = {}
    for x in request.args.getlist("ordering[]"):
        index, answer_id = x.split(";")
        ordering[answer_id] = index

    database = Database()
    database.cursor.execute(
        "SELECT * FROM answer WHERE question_id = ?;", (question_id,)
    )
    answer_data = database.cursor.fetchall()

    processed_answer_data = [
        {
            "answer_id": single_answer["answer_id"],
            "answer": single_answer["answer"],
            "correct": single_answer["correct"] == 1,
            "selected": single_answer["answer_id"] in selected_answers_id,
        }
        for single_answer in answer_data
    ]

    processed_answer_data.sort(key=lambda x: ordering[x["answer_id"]])

    return render_template("answer-solution-list.html", answers=processed_answer_data)
