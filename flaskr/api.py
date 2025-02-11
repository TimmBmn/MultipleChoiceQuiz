from flask import Blueprint, render_template, request

from flaskr.database import Database

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/random_question", methods=["GET"])
def random_question():

    database = Database()
    database.cursor.execute("SELECT * FROM question ORDER BY RANDOM() LIMIT 1;")

    # only possible if there are no questions
    if (question_data := database.cursor.fetchone()) is None:
        return ""

    database.cursor.execute(
        "SELECT * FROM answer WHERE question_id = ?;", (question_data["question_id"],)
    )
    answers_data = database.cursor.fetchall()

    return render_template(
        "question.html", question=question_data, answers=answers_data
    )


@api_blueprint.route("/correct_answers", methods=["GET"])
def correct_answers():
    # TODO None handling
    question_id = request.args.get("question_id")
    selected_answers_id = request.args.getlist("answers[]")

    print(selected_answers_id)

    database = Database()
    database.cursor.execute(
        "SELECT * FROM answer WHERE question_id = ?;", (question_id,)
    )
    answer_data = database.cursor.fetchall()

    processed_answer_data = [
        {
            "answer": single_answer["answer"],
            "correct": single_answer["correct"] == 1,
            "selected": single_answer["answer_id"] in selected_answers_id,
        }
        for single_answer in answer_data
    ]

    return render_template("answer-solution-list.html", answers=processed_answer_data)
