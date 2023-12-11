from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user
home = Blueprint('home', __name__, url_prefix='/')

# TODO DO NOT EDIT
@home.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return redirect(url_for('auth.landing_page'))