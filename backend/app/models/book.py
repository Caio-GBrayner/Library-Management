from ..extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullabel=False)
    description = db.Column(db.String(200))
    tag = db.Column(db.String(100))
    imgUrl = db.Column(db.String(300))

    def __repr__(self):
        return f"<Book{self.name}"