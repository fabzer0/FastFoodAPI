from flask  import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse, inputs
from ..models.models import OrdersModel

class OrderList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'ordername',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a valid name',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'price',
            required=True,
            type=int,
            help='kindly provide a price(should be a valid number)',
            location=['form', 'json'])

        super(OrderList, self).__init__()

    def post(self):

        kwargs = self.reqparse.parse_args()
        ordername = kwargs.get('ordername')
        price = kwargs.get('price')

        order = OrdersModel.get_one('orders', ordername=ordername)
        if order:
            return make_response(jsonify({'message': 'order with that name already exist'}), 203)

        order = OrdersModel(ordername=ordername, price=price)
        order.create_order()
        order = OrdersModel.get_one('orders', ordername=ordername)
        return make_response(jsonify({'message': 'order has been successfully posted', 'order': OrdersModel.order_details(order)}), 201)

    def get(self):
        orders = OrdersModel.get_all('orders')
        if not orders:
            return make_response(jsonify({'message': 'you have no orders yet'}))

        return make_response(jsonify({'orders': orders}))


class AdminGetAllOrders(Resource):

    def get(self):
        orders = OrdersModel.get_all('orders')
        if not orders:
            return make_response(jsonify({'message': 'no orders yet'}), 404)
        return make_response(jsonify({'all_orders': orders}), 200)

class AdminGetAllSingleOrder(Resource):

    def get(self, order_id):
        order = OrdersModel.get_one('orders', id=order_id)
        if not order:
            return make_response(jsonify({'message': 'order does not exist'}), 404)
        return make_response(jsonify({'order': order}), 200)

# class Order(Resource):
#
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument(
#             'status',
#             required=True,
#             type=inputs.regex(r"(.*\S.*)"),
#             help='kindly provide a valid name',
#             location=['form', 'json'])
#         super(Order, self).__init__()
#
#     def get(self, order_id):
#         order = OrdersModel.get_one('orders', id=order_id)
#         return make_response(jsonify({'order': order}))
#
#     def put(self, order_id):
#
#         order = OrdersModel.get_one('orders', id=order_id)
#         if not order:
#             return make_response(jsonify({'message': 'order item does not exist'}), 404)
#         post_data = request.get_json()
#         status = post_data.get('status')
#         data = {}
#         if status:
#             data.update({'status': str(status)})
#         OrdersModel.update('orders', id=order[0], data=data)
#         order = OrdersModel.get_one('orders', id=order_id)
#         return make_response(jsonify({'message': 'order has been updated successfully', 'new_order': OrdersModel.order_details(order)}), 200)
#
#     def delete(self, order_id):
#         order = OrdersModel.get_one('orders', id=order_id)
#         if order:
#             OrdersModel.delete('orders', id=order[0])
#             return make_response(jsonify({'message': 'order item has been deleted'}))
#         return make_response(jsonify({'message': 'order item does not exist'}))


orders_api = Blueprint('resources.orders', __name__)
api = Api(orders_api)
api.add_resource(OrderList, '/users/orders', endpoint='orders')
api.add_resource(AdminGetAllOrders, '/orderss', endpoint='orderss')
api.add_resource(AdminGetAllSingleOrder, '/orders/<int:order_id>', endpoint='order')
# api.add_resource(Order, '/orders/<int:order_id>', endpoint='order')
