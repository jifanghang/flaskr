# jBlogger

A simple blogging web app project using [Flask](http://flask.pocoo.org/) with Python 2.7. 

Database is [SQLite](https://sqlite.org/about.html). Python has a built-in support for that in the SQLite3 module.

## Project layout:
```
├── jBlogger/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .gitignore
├── README.md
├── requirements.txt
├── run.sh
├── setup.py
└── MANIFEST.in
```

## How to run
### Initialization
First, install dependencies
```bash
pip install -r requirements.txt
```
then, initialize the database by
```bash
export FLASK_APP=jBlogger
flask init-db
```
> *Please only run the above command on the first time.*

### Run
```bash
bash run.sh
```