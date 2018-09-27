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

class UsersOrder(Resource):

    def get(self, order_id):
        order = OrdersModel.get_one('orders', id=order_id)
        if not order:
            return make_response(jsonify({'message': 'order does not exist'}), 404)
        return make_response(jsonify({'order': OrdersModel.order_details(order)}), 200)

    def delete(self, order_id):
        order = OrdersModel.get_one('orders', id=order_id)
        if not order:
            return make_response(jsonify({'message': 'order does not exist'}), 404)
        else:
            OrdersModel.delete('orders', id=order_id)
            return make_response(jsonify({'message': 'order has been deleted'}), 200)



class AdminGetAllOrders(Resource):

    def get(self):
        orders = OrdersModel.get_all('orders')
        if not orders:
            return make_response(jsonify({'message': 'no orders yet'}), 404)
        return make_response(jsonify({'all_orders': orders}), 200)

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

    def get(self, order_id):
        order = OrdersModel.get_one('orders', id=order_id)
        if not order:
            return make_response(jsonify({'message': 'order does not exist'}), 404)
        return make_response(jsonify({'order': order}), 200)

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
api.add_resource(OrderList, '/users/orders')
api.add_resource(UsersOrder, '/users/orders/<int:order_id>')
api.add_resource(AdminGetAllOrders, '/orders')
api.add_resource(AdminGetSingleOrder, '/orders/<int:order_id>')
