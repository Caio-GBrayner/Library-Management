from ..extensions import db
from sqlalchemy.orm import relationship, backref

class OrderItem(db.Model):
    __tablename__ = "tb_order_item"

    order_id = db.Column(db.Integer, db.ForeignKey('tb_order.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('tb_book.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", backref=backref("items", cascade="all, delete-orphan"))
    book = db.relationship("Book", backref="order_items")

    @property
    def subtotal(self):
        return self.quantity * self.price

    def to_dict(self, include_book=False, include_order=False):
        data = {
            "order_id": self.order_id,
            "book_id": self.book_id,
            "quantity": self.quantity,
            "price": self.price,
            "subtotal": self.subtotal
        }

        if include_book and self.book:
            data["book"] = self.book.to_dict()

        if include_order and self.order:
            data["order"] = {
                "id": self.order.id,
                "moment": self.order.moment.isoformat() + "Z" if self.order.moment else None,
                "status": self.order.order_status
            }

        return data

    def __repr__(self):
        return f"<OrderItem order={self.order_id} book={self.book_id} qty={self.quantity}>"