from ..extensions import db

class User(db.Model):
    __tablename__ = "tb_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    identifier = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    password = db.Column(db.String(100),nullable=False)

    orders = db.relationship("Order", back_populates="client")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    def __repr__(self):
        return f"<User:{self.name} ({self.identifier}"
