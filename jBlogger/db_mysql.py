from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import click
from flask.cli import with_appcontext

"""
TODO: 
0. Add DB - done
1. Create table models
2. Add Data
3. Add query to show in templates
4. Show tables using WTF
5. CRUD
"""

def init_mysql(app):
    db = SQLAlchemy(app)


@click.command('init-mysql')
@with_appcontext
def init_mysql_db_command():
    init_mysql_db()
    click.echo('Initialized the MySQL database.')
