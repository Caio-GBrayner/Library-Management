from ..extensions import db
from sqlalchemy.orm import relationship, backref

class OrderItem(db.Model):
    __tablename__ = "tb_order_item"

    order_id = db.Column(db.Integer, db.ForeignKey('tb_order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('tb_book.id'), primary_key=True)

    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

    order = db.relationship("Order", backref=backref("items"))
    product = db.relationship("Book")

    @property
    def subtotal(self):
        return self.quantity * self.price
