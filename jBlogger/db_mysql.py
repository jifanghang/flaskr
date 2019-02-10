from flask_sqlalchemy import SQLAlchemy
# from flask import Blueprint
import click
from flask.cli import with_appcontext
from datetime import datetime
"""
TODO: 
0. Add DB - DONE
1. Create table models - DONE
2. Add Data
3. Add query to show in templates
4. Show tables using WTF
5. CRUD
"""


def init_mysql(app):
    db = SQLAlchemy(app)

    class User(db.Model):
        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(80), nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username

    class Post(db.Model):
        __tablename__ = 'posts'

        id = db.Column(db.Integer, primary_key=True)
        author_id = db.Column(db.Integer,
                              db.ForeignKey(users.id),
                              nullable=False)
        created = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.now())
        title = db.Column(db.String(80), nullable=False)
        body = db.Column(db.Text, nullable=False)
        # author = db.relationship('User',
        #                          backref=db.backref('posts', lazy=True))

        def __repr__(self):
            return '<Post %s. Title: %s>' % (self.username, self.title)

    db.drop_all()
    db.create_all()


@click.command('init-mysql')
@with_appcontext
def init_mysql_db_command():
    init_mysql()
    click.echo('Initialized the MySQL database.')
