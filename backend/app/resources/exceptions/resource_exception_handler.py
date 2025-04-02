from flask import request
from .standard_error import StandardError
from ...services.exceptions.database_exception import DatabaseError
from ...services.exceptions.resource_not_found__exception import ResourceNotFound


def init_exception_handlers(app):
    @app.errorhandler(ResourceNotFound)
    def handle_resource_not_found(e):
        error = StandardError(
            status=e.status_code,
            error="Resource not found",
            message=str(e),
            path=request.path
        )
        return error.to_dict(), e.status_code

    @app.errorhandler(DatabaseError)
    def handle_database_error(e):
        error = StandardError(
            status=e.status_code,
            error="Database error",
            message=str(e),
            path=request.path
        )
        return error.to_dict(), e.status_code

    @app.errorhandler(Exception)
    def handle_generic_error(e):
        error = StandardError(
            status=500,
            error="Internal server error",
            message=str(e),
            path=request.path
        )
        return error.to_dict(), 500