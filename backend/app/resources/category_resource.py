from flask import Blueprint, jsonify
from http import HTTPStatus
from ..services.category_service import CategoryService
from ..services.exceptions.resource_not_found__exception import ResourceNotFound

category_bp = Blueprint('categories', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def get_all_categories():
    categories = CategoryService.find_all()
    return jsonify([category.to_dict() for category in categories])

@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        category = CategoryService.find_by_id(category_id)
        return jsonify(category.to_dict())
    except ResourceNotFound as e:
        return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND
