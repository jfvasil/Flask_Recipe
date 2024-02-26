from flask import Blueprint
from flask import render_template, redirect
import os
import psycopg2


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/all_recipes')
def all_recipes():
    return render_template('all_recipes.html')

@bp.route('/profile')
def profile():
    return render_template('profile.html')