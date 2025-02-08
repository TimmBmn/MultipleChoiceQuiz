import sqlite3


def create_database():
    connection = sqlite3.connect("database.db")
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


def create_testing_data():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.executemany(
        "INSERT INTO question(question_id, question) VALUES (?, ?);",
        (
            ["1", "who painted the mona lisa"],
            ["2", "what is heavier, a kilogram of steel or a kilogram of feathers"],
        ),
    )

    cursor.executemany(
        "INSERT INTO answer(answer_id, question_id, answer, correct) VALUES (?, ?, ?, ?);",
        (
            ["1", "1", "davinci?", True],
            ["2", "1", "leonardo", True],
            ["3", "1", "brad pit", False],
            ["4", "2", "but steels heavier than feathers", False],
            ["5", "2", "their the same", True],
            ["6", "2", "but how can feathers be heavier?", False],
        ),
    )
    connection.commit()


if __name__ == "__main__":
    create_database()
    create_testing_data()
