from . import db

class Article(db.Model):

    __tablename__ = 'Articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text())
    date = db.Column(db.Date())

    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date
    
    def __repr__(self):
        return '<id {}>'.format(self.id)