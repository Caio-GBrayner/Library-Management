from datetime import datetime
from ..extensions import db

class Payment(db.Model):
    __tablename__ = "tb_payment"

    id = db.Column(db.Integer, primary_key=True)
    moment = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    order_id = db.Column(db.Integer, db.ForeignKey('tb_order.id'), unique=True)
    order = db.relationship(
        "Order",
        back_populates="payment",
        uselist=False,
        single_parent=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "moment": self.moment.isoformat() + "Z" if self.moment else None,
            "order_id": self.order_id
        }

    def __repr__(self):
        return f"<Payment {self.id} for Order {self.order_id}>"