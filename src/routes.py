from flask import Blueprint
from flask import render_template, redirect
import os
import psycopg2


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello World 3'

