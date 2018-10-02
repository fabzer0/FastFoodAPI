
from flask  import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse, inputs
from ..models.models import OrdersModel, MealsModel
from ..models.decorators import admin_required, token_required

class UserOrders(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'item',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='item field is required',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'quantity',
            required=True,
            type=int,
            help='quantity field is required',
            location=['form', 'json'])
        super(UserOrders, self).__init__()

    @token_required
    def post(self, user_id):

        kwargs = self.reqparse.parse_args()
        item = kwargs.get('item')
        quantity = kwargs.get('quantity')
        meal = MealsModel.get_one('meals', mealname=item)
        if not meal:
            return {'message': 'order not in menu'}
        if meal[3]:
            price = meal[2]
            totalprice = price * quantity
            order = OrdersModel(user_id=user_id, item=item, totalprice=totalprice)
            order.create_order()
            order = OrdersModel.get_one('orders', item=item)
            return make_response(jsonify({'message': 'order has been successfully added', 'order': OrdersModel.order_details(order)}), 201)
        
        
    @token_required
    def get(self, user_id, order_id=None):
        if order_id:
            user_order = OrdersModel.get(user_id=user_id, order_id=order_id)
            if user_order:
                return {'order': OrdersModel.order_details(user_order)}, 200
            return {'message': 'order not found'}, 404
        user_orders = OrdersModel.get(user_id=user_id)
        if not user_orders:
            return make_response(jsonify({'message': 'you have no orders yet'}), 404)
        return make_response(jsonify({'orders': [OrdersModel.order_details(order) for order in user_orders]}), 200)

    @token_required
    def delete(self, user_id, order_id):
        user_order = OrdersModel.get(user_id=user_id, order_id=order_id)
        if user_order:
            OrdersModel.delete('orders', id=user_order[0])
            return {'message', 'order successfully deleted'}, 200
        return {'message': 'order does not exist'}, 404

class AdminGetAllOrders(Resource):

    @admin_required
    def get(self):
        orders = OrdersModel.get_all('orders')
        if not orders:
            return make_response(jsonify({'message': 'no orders yet'}), 404)
        return make_response(jsonify({'all_orders': [OrdersModel.order_details(order) for order in orders]}), 200)

class AdminGetSingleOrder(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'status',
            required=True,
            type=str,
            help='please insert the status of an order',
            location=['form', 'json']
        )

    @admin_required
    def get(self, order_id):
        order = OrdersModel.get_one('orders', id=order_id)
        if not order:
            return make_response(jsonify({'message': 'order does not exist'}), 404)
        return make_response(jsonify({'order': OrdersModel.order_details(order)}), 200)

    @admin_required
    def put(self, order_id):

        kwargs = self.reqparse.parse_args()
        status = kwargs.get('status')
        statuses = ['new', 'processing', 'cancelled', 'complete']

        order = OrdersModel.get_one('orders', id=order_id)
        if not order:
            return make_response(jsonify({'message': 'order item does not exist'}), 404)
        data = {}
        if status:
            if status not in statuses:
                return make_response(jsonify({'message': 'status should either be new, processing, cancelled or complete'}), 400)
            data.update({'status': str(status)})

        OrdersModel.update('orders', id=order[0], data=data)
        order = OrdersModel.get_one('orders', id=order_id)
        return make_response(jsonify({'message': 'order has been updated successfully', 'new_order': OrdersModel.order_details(order)}), 200)


orders_api = Blueprint('resources.orders', __name__)
api = Api(orders_api)
api.add_resource(UserOrders, '/user/orders', '/user/orders/<int:order_id>')
api.add_resource(AdminGetAllOrders, '/orders')
api.add_resource(AdminGetSingleOrder, '/orders/<int:order_id>')
