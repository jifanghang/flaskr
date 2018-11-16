# Blueprints and Views
import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
