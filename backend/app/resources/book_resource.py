from flask import Blueprint, jsonify
from ..services.book_service import BookService
from ..services.exceptions.resource_not_found__exception import ResourceNotFound

book_bp = Blueprint('books', __name__, url_prefix='/books')

@book_bp.route('/', methods=['GET'])
def get_all_books():
    books = BookService.find_all()
    return jsonify([book.to_dict() for book in books])

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = BookService.find_by_id(book_id)
        return jsonify(book.to_dict())
    except ResourceNotFound as e:
        return jsonify({"error": str(e)}), 404