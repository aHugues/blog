from flask import Flask
from .views import main_views
from .views import blog_views

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(main_views)
    app.register_blueprint(blog_views)
    return app