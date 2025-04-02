from ..models.book import Book
from ..extensions import db
from .exceptions.database_exception import DatabaseError
from .exceptions.resource_not_found__exception import  ResourceNotFound

class BookService:
    @staticmethod
    def find_all():
        return Book.query.all()

    @staticmethod
    def find_by_id(book_id):
        book = Book.query.get(book_id)
        if not book:
            raise ResourceNotFound(f"Book with id {book_id} not found")
        return book
