from flask  import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse, inputs

from ..models.models import MenuModel




class MenuList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'menu_item',
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

        super(MenuList, self).__init__()

    def post(self):

        kwargs = self.reqparse.parse_args()
        menu_item = kwargs.get('menu_item')
        price = kwargs.get('price')

        menu = MenuModel.get_one('menu', menu_item=menu_item)
        if menu:
            return make_response(jsonify({'message': 'menu with that name already exist'}), 203)

        menu = MenuModel(menu_item=menu_item, price=price)
        menu.create_meal()
        menu = MenuModel.get_one('menu', menu_item=menu_item)
        return make_response(jsonify({'message': 'menu has been successfully posted', 'menu': MenuModel.menu_details(menu)}), 201)

    def get(self):
        menu = MenuModel.get_all('menu')
        return make_response(jsonify({'menu': menu}))

class Menu(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'menu_item',
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

        super(Menu, self).__init__()

    def get(self, menu_id):
        menu = MenuModel.get_one('meanu', id=menu_id)
        return make_response(jsonify({'menu': menu}))

    def put(self, menu_id):

        menu = MenuModel.get_one('menu', id=menu_id)
        if not menu:
            return make_response(jsonify({'message': 'menu item does not exist'}), 404)
        post_data = request.get_json()
        menu_item = post_data.get('menu_item')
        price = post_data.get('price')
        data = {}
        if menu_item:
            data.update({'menu_item': str(menu_item)})
        if price:
            data.update({'price': str(price)})
        MenuModel.update('menu', id=menu[0], data=data)
        menu = MenuModel.get_one('menu', id=menu_id)
        return make_response(jsonify({'message': 'menu has been updated successfully', 'new_menu': MenuModel.menu_details(menu)}), 200)

    def delete(self, menu_id):

        menu = MenuModel.get_one('menu', id=menu_id)
        if menu:
            MenuModel.delete('meals', id=menu[0])
            return make_response(jsonify({'message': 'menu item has been deleted'}))
        return make_response(jsonify({'message': 'menu item does not exist'}))




menu_api = Blueprint('resources.menu', __name__)
api = Api(menu_api)
api.add_resource(MenuList, '/menu', endpoint='menu')
api.add_resource(Menu, '/menu/<int:menu_id>', endpoint='menu')
