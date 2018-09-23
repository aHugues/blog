from ..models import Article
from . import db
import datetime


def convert_to_dict(article):
    dict_article = {
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'date': article.date
    }
    return dict_article


class ArticlesService:

    def __init__(self):
        pass
    
    def listArticles(self):
        articles = Article.query.all()
        return [convert_to_dict(x) for x in articles]
    
    def addArticle(self, title, content):
        now = datetime.datetime.now()
        article = Article(title=title, content=content, date=now)
        db.session.add(article)
        db.session.commit()
    
    def get_article(self, articleid):
        article = Article.query.filter(Article.id == articleid).first()
        return article

