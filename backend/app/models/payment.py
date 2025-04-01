from datetime import datetime
from ..extensions import db

class Payment(db.Model):
    __tablename__ = "TB_PAYMENT"

    id = db.Column(db.Interger, primary_key=True)
    moment = db.Column(db.DateTime, nullabel=False, default=datetime.utcnow())