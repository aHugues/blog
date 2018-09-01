from flask import Flask
from .views import main_views
from .views import blog_views
from .views import admin_views
from .models import db
import configparser

config = configparser.ConfigParser()

def create_app(debug=False, production=False):
    if production:
        config.read('web/config/config.prod.ini')
    else:
        config.read('web/config/config.dev.ini')
    print(config)
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(main_views)
    app.register_blueprint(blog_views)
    app.register_blueprint(admin_views)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['SQLAlchemy_uri']
    db.init_app(app)
    return app