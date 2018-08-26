from flask import Blueprint
from flask import render_template

blog_views = Blueprint('blog_views', __name__)

@blog_views.route('/blog')
def home_page():
    articles = ['article ' + str(x) for x in range(10)]
    return render_template('blog.html',
        articles=articles,
        current_page="blog",
    )