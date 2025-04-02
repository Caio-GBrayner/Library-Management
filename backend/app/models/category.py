from ..extensions import db


class Category(db.Model):
    __tablename__ = "tb_category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship(
        "Book",
        secondary="tb_book_category",
        back_populates="categories",
        lazy='dynamic'
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "book_count": self.books.count()
        }

    def __repr__(self):
        return f'<Category {self.name}>'