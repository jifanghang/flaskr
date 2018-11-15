# flaskr

A simple [Flask](http://flask.pocoo.org/) project with Python 2. 
Database is [SQLite](https://sqlite.org/about.html). Python has a built-in support for that in the SQLite3 module.

### Project layout:
```
├── flaskr/
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
├── setup.py
└── MANIFEST.in
```

### How to run
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
or just `bash run.sh`