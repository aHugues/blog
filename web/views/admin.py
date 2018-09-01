from flask import Blueprint
from flask import render_template

admin_views = Blueprint('admin_views', __name__)

@admin_views.route('/admin')
def home_page():
    return render_template('admin.html',
    )