from flask import Blueprint, request, jsonify, make_response
from .services.user_service import UserService
from .exceptions import ResourceNotFound, DatabaseError

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = UserService.find_all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = UserService.find_by_id(user_id)
        return jsonify(user.to_dict())
    except ResourceNotFound as e:
        return make_response(jsonify({"error": str(e)}), 404)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create(data)
    return jsonify(user.to_dict()), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    try:
        user = UserService.update(user_id, data)
        return jsonify(user.to_dict())
    except ResourceNotFound as e:
        return make_response(jsonify({"error": str(e)}), 404)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        UserService.delete(user_id)
        return '', 204
    except ResourceNotFound as e:
        return make_response(jsonify({"error": str(e)}), 404)
    except DatabaseError as e:
        return make_response(jsonify({"error": str(e)}), 400)