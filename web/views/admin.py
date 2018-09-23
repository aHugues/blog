from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
import os
from flask import flash
from flask import url_for
from flask_bcrypt import Bcrypt
import flask_login
from flask import Flask
import configparser

config = configparser.ConfigParser()
try:
    assert os.environ['SERVER_ENV'] == 'production'
    config.read('web/config/config.prod.ini')
except:
    config.read('web/config/config.dev.ini')

app = Flask(__name__)

admin_views = Blueprint('admin_views', __name__)

bcrypt = Bcrypt(app)
login_manager = flask_login.LoginManager()


class User(flask_login.UserMixin):

    def __init__(self):
        self.id = None


@login_manager.user_loader
def user_loader(user_id):
    if user_id != 'admin':
        return 
    user = User()
    user.id = 'admin'
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('admin_views.login'))


@admin_views.route('/admin')
@flask_login.login_required
def home_page():
    return render_template('admin.html',
    )


@admin_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    password = request.form['password']
    if password == config['AUTHENTICATION']['admin_password']:
        user = User()
        user.id = 'admin'
        flask_login.login_user(user)
        return redirect(url_for('admin_views.home_page'))
    
    flash('Login failed')
    return redirect(url_for('admin_views.login'))


@admin_views.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('main_views.home_page'))