"""
Initializing the project:
 - Containing the application factory
 - Telling Python that the /jBlogger directory should be treated as a package
"""
import os
from flask import Flask


def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'jBlogger.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # database
    from . import db
    db.init_app(app)

    # MySQL database
    from . import db_mysql
    # mysql username: 'jBlogger'
    # password: 'password'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jBlogger:password@127.0.0.1/jBlogger'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

