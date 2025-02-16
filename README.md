# Multiple Choice Quiz

Host your own multiple choice quiz online!

# How to setup

To create the database run

```bash
python flaskr/database.py
```

To then insert example questions run

```bash
python flaskr/create_questions/example.py
```

To then start the server either run
```bash
flask --app flaskr run --debug
```

to use the development server or

```bash
gunicorn -w 1 "flaskr:create_app()"
```

to use the production server
