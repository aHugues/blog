from flask import Flask
import os
from .views import main_views
from .views import blog_views
from .views import admin_views
from .views import login_manager
from .models import db
import configparser

config = configparser.ConfigParser()

def create_app(debug=False):
    try:
        assert os.environ['SERVER_ENV'] == 'production'
        config.read('web/config/config.prod.ini')
    except:
        config.read('web/config/config.dev.ini')
    app = Flask(__name__)
    login_manager.init_app(app)
    app.debug = debug
    app.secret_key = config['AUTHENTICATION']['app_secret_key']
    app.register_blueprint(main_views)
    app.register_blueprint(blog_views)
    app.register_blueprint(admin_views)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['SQLAlchemy_uri']
    db.init_app(app)
    return app