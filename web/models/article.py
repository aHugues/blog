from . import db

class Article(db.Model):

    __tablename__ = 'Articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text())
    date = db.Column(db.Date())
    image = db.Column(db.String(64))

    def __init__(self, title, content, date, image):
        self.title = title
        self.content = content
        self.date = date
        self.image = image
    
    def __repr__(self):
        return '<id {}>'.format(self.id)