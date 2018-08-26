from flask import Blueprint
from flask import render_template

main_views = Blueprint('main_views', __name__)

@main_views.route('/')
def home_page():
    return render_template('home.html',
        current_page="about")