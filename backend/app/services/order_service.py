from ..extensions import db
from ..models import Order
from exceptions.resource_not_found__exception import ResourceNotFound

class OrderService:
    @staticmethod
    def find_all():
        return Order.query.all()

    @staticmethod
    def find_by_id(order_id):
        order = Order.query.get(order_id)
        if not order:
            raise ResourceNotFound(f"Order with id {order_id} not found")
        return order

    @staticmethod
    def create(order_data):
        order = Order(**order_data)
        db.session.add(order)
        db.session.commit()
        return order

    def update(order_id, order_data):
        order = Order.query.get(order_id)
        if not order:
            raise ResourceNotFound(f"Order with id {order_id} not found")

        if 'client_id' in order_data:
            order.client_id = order_data['client_id']
        if 'order_status' in order_data:
            order.order_status = order_data['order_status']

        db.session.commit()
        return order

    @staticmethod
    def delete(order_id):
        order = Order.query.get(order_id)
        if not order:
            raise ResourceNotFound(f"Order with id {order_id} not found")

        db.session.delete(order)
        db.session.commit()