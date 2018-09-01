from flask import Flask
from .views import main_views
from .views import blog_views
from .views import admin_views

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(main_views)
    app.register_blueprint(blog_views)
    app.register_blueprint(admin_views)
    return app