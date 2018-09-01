from flask import Flask
from .views import main_views
from .views import blog_views
from .views import admin_views
from .models import db

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(main_views)
    app.register_blueprint(blog_views)
    app.register_blueprint(admin_views)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://blog:password@localhost/blog'
    db.init_app(app)
    return app