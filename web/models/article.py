from . import db

class Article(db.Model):

    __tablename__ = 'Articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))

    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return '<id {}'.format(self.id)