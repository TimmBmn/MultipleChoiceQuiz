import random

from flaskr.database import Database


def random_question():
    database = Database()
    database.cursor.execute("SELECT * FROM question ORDER BY RANDOM() LIMIT 1;")

    question = database.cursor.fetchone()
    if question is None:
        return None, []

    return specific_question(question["question_id"])


def specific_question(question_id: str):
    database = Database()
    database.cursor.execute(
        "SELECT * FROM question WHERE question_id = ?;", (question_id,)
    )
    question = database.cursor.fetchone()
    if question is None:
        return None, []

    database.cursor.execute(
        "SELECT * FROM answer WHERE question_id = ?;", (question_id,)
    )
    answers = database.cursor.fetchall()
    random.shuffle(answers)

    return question, answers
