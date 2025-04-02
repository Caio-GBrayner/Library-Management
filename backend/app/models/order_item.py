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

    def to_dict(self, include_product=False, include_order=False):
        data = {
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price": self.price,
            "subtotal": self.subtotal
        }

        if include_product and self.product:
            data["product"] = self.product.to_dict()

        if include_order and self.order:
            data["order"] = {
                "id": self.order.id,
                "moment": self.order.moment.isoformat() + "Z" if self.order.moment else None
            }

        return data
