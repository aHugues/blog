from flask import Blueprint
from flask import render_template
from flask import request
from flask_bcrypt import Bcrypt
import flask_login
from flask import Flask

app = Flask(__name__)

admin_views = Blueprint('admin_views', __name__)

bcrypt = Bcrypt(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

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



@admin_views.route('/admin')
def home_page():
    return render_template('admin.html',
    )

@admin_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    password = request.form['password']
    if password == 'toto':
        user = User()
        user.id = 'admin'
        flask_login.login_user(user)
        return 'ok'
    
    return 'nope'