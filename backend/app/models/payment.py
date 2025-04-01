from datetime import datetime
from ..extensions import db

class Payment(db.Model):
    __tablename__ = "tb_payment"

    id = db.Column(db.Interger, primary_key=True)
    moment = db.Column(db.DateTime, nullabel=False, default=datetime.utcnow())