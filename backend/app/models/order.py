from datetime import datetime
from ..extensions import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship, backref

class Order(db.Model):
    __tablename__ = "tb_order"

    id = db.Column(db.Integer, primary_key=True)
    moment = db.Column(db.DateTime, nullabel=False, default=datetime.utcnow)
    client_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    client = db.relationship("User", backref=backref("orders", lazy=True))
    items = db.relationship("OrderItem", backref="order", lazy=True, cascade="all, delete-orphan")
    order_status = db.Column(db.Integer, nullable=False)
    payment = db.relationship("Payment", uselist=False, back_populates="order", cascade="all, delete-orphan")