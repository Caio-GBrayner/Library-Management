from ..extensions import db

class Book(db.Model):
    __tablename__ = "tb_book"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    tag = db.Column(db.String(100))
    price = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String(300))

    categories = db.relationship(
        "Category",
        secondary="tb_book_category",
        back_populates="books",
        lazy='dynamic'
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="book",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "img_url": self.img_url,
            "categories": [cat.to_dict() for cat in self.categories]
        }

    def __repr__(self):
        return f"<Book {self.name}>"