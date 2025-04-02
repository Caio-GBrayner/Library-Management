from ..extensions import db
from ..models.category import Category
from .exceptions.resource_not_found__exception import ResourceNotFound


class CategoryService:
    @staticmethod
    def find_all():
        return Category.query.all()

    @staticmethod
    def find_by_id(category_id):
        category = Category.query.get(category_id)
        if not category:
            raise ResourceNotFound(f"Category with id {category_id} not found")
        return category