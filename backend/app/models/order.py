from datetime import datetime
from ..extensions import db
from sqlalchemy.orm import relationship, backref
from .enum.order_status import OrderStatus

class Order(db.Model):
    __tablename__ = "tb_order"

    id = db.Column(db.Integer, primary_key=True)
    moment = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    client_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    client = db.relationship("User", backref=backref("orders", lazy=True))
    items = db.relationship("OrderItem", backref="order", lazy=True, cascade="all, delete-orphan")
    order_status = db.Column(db.Integer, nullable=False, default=OrderStatus.PENDING.value)
    payment = db.relationship("Payment", uselist=False, back_populates="order", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "moment": self.moment.isoformat() + "Z",
            "client_id": self.client_id,
            "order_status": OrderStatus(self.order_status).name,
            "client": self.client.to_dict() if self.client else None
        }