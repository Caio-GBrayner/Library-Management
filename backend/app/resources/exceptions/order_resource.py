from flask import Blueprint, request, jsonify, make_response
from ...services.order_service import OrderService
from ...services.exceptions.resource_not_found__exception import ResourceNotFound
from ...services.exceptions.database_exception import DatabaseError

order_bp = Blueprint('orders', __name__, url_prefix='/orders')

@order_bp.route('/', methods=['GET'])
def get_all_orders():
    orders = OrderService.find_all()
    return jsonify([order.to_dict() for order in orders])

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = OrderService.find_by_id(order_id)
        return jsonify(order.to_dict())
    except ResourceNotFound as e:
        return make_response(jsonify({"error": str(e)}), 404)

@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        order = OrderService.create(data)
        return jsonify(order.to_dict()), 201
    except DatabaseError as e:
        return make_response(jsonify({"error": str(e)}), 400)

@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    try:
        order = OrderService.update(order_id, data)
        return jsonify(order.to_dict())
    except ResourceNotFound as e:
        return make_response(jsonify({"error": str(e)}), 404)
    except DatabaseError as e:
        return make_response(jsonify({"error": str(e)}), 400)

@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        OrderService.delete(order_id)
        return '', 204
    except ResourceNotFound as e:
        return make_response(jsonify({"error": str(e)}), 404)
    except DatabaseError as e:
        return make_response(jsonify({"error": str(e)}), 400)