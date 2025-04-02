from ..extensions import db

class Category(db.Model):
    __tablename__= "tb_categoty"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullabel=False)
    books = db.relationship("Book", secondary="tb_book_category", back_populates="categories")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }