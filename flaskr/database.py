import sqlite3
import uuid


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = 1;")
        self.cursor = self.connection.cursor()

    def __del__(self) -> None:
        self.cursor.close()
        self.connection.close()


class Answer:
    def __init__(self, answer: str, correct: bool) -> None:
        self.answer_id = str(uuid.uuid4())
        self.answer = answer
        self.correct = correct


class Question:
    def __init__(self, question: str, answers: list[Answer]) -> None:
        self.question_id = str(uuid.uuid4())
        self.question = question
        self.answers = answers

    def create(self):
        database = Database()

        database.cursor.execute(
            "INSERT INTO question(question_id, question) VALUES (?, ?);",
            (self.question_id, self.question),
        )

        database.cursor.executemany(
            "INSERT INTO answer(answer_id, question_id, answer, correct) VALUES (?, ?, ?, ?);",
            [
                (answer.answer_id, self.question_id, answer.answer, answer.correct)
                for answer in self.answers
            ],
        )
        database.connection.commit()


def create_database():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = 1;")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS question (
            question_id TEXT NOT NULL,
            question TEXT NOT NULL,

            PRIMARY KEY (question_id)
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS answer(
           answer_id TEXT NOT NULL,
           question_id TEXT NOT NULL,
           answer TEXT NOT NULL,
           correct INTEGER NOT NULL CHECK(correct IN (0, 1)),

           PRIMARY KEY (answer_id),
           FOREIGN KEY (question_id) REFERENCES question(question_id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )
    connection.commit()


if __name__ == "__main__":
    create_database()
