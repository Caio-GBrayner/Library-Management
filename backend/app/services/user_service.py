from ..models.user import User
from ..extensions import db
from .exceptions import ResourceNotFound, DatabaseError


class UserService:
    @staticmethod
    def find_all():
        return User.query.all()

    @staticmethod
    def find_by_id(user_id):
        user = User.query.get(user_id)
        if not user:
            raise ResourceNotFound(f"User with id {user_id} not found")
        return user

    @staticmethod
    def create(user_data):
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user_id, user_data):
        user = User.query.get(user_id)
        if not user:
            raise ResourceNotFound(f"User with id {user_id} not found")

        for key, value in user_data.items():
            setattr(user, key, value)

        db.session.commit()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if not user:
            raise ResourceNotFound(f"User with id {user_id} not found")

        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise DatabaseError(str(e))