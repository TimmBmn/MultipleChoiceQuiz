from flaskr.database import Answer, Question

Question(
    "who painted the mona lisa",
    [
        Answer("davinci?", True),
        Answer("leonardo", True),
        Answer("brad pit", False),
    ],
).create()

Question(
    "what is heavier, a kilogram of steel or a kilogram of feathers",
    [
        Answer("but steels heavier than feathers", False),
        Answer("their the same", True),
        Answer("but how can feathers be heavier?", False),
    ],
).create()
