from datetime import datetime
from ..extensions import db

class Payment(db.Model):
    __tablename__ = "tb_payment"

    id = db.Column(db.Interger, primary_key=True)
    moment = db.Column(db.DateTime, nullabel=False, default=datetime.utcnow())
    order_id = db.Column(db.Integer, db.ForeignKey('tb_order.id'), unique=True)
    order = db.relationship("Order", back_populates="payment", uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "moment": self.moment.isoformat() + "Z",
        }