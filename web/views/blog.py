from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

from ..services import ArticlesService

blog_views = Blueprint('blog_views', __name__)
articles_service = ArticlesService()

@blog_views.route('/blog')
def home_page():
    articles = articles_service.listArticles()
    return render_template('blog.html',
        articles=articles,
        current_page="blog",
    )

@blog_views.route('/api/articles', methods=["GET", "POST"])
def display_articles_list():
    if request.method == 'GET':
        articles = articles_service.listArticles()
        return jsonify(articles)
    elif request.method == 'POST':
        article_title = request.json['title']
        article_content = request.json['content']
        articles_service.addArticle(article_title, article_content)
        return "ok", 200