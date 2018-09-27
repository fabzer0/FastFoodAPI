from flask  import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse, inputs
from ..models.models import MenusModel

class MenusList(Resource):

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

        super(MenusList, self).__init__()

    def post(self):

        kwargs = self.reqparse.parse_args()
        menu_item = kwargs.get('menu_item')
        price = kwargs.get('price')

        menu = MenusModel.get_one('menu', menu_item=menu_item)
        if menu:
            return make_response(jsonify({'message': 'menu with that name already exist'}), 203)

        menu = MenusModel(menu_item=menu_item, price=price)
        menu.create_menu()
        menu = MenusModel.get_one('menu', menu_item=menu_item)
        return make_response(jsonify({'message': 'menu has been successfully posted', 'menu': MenusModel.menu_details(menu)}), 201)

    def get(self):
        menus = MenusModel.get_all('menu')
        return make_response(jsonify({'menu': [MenusModel.menu_details(menu) for menu in menus]}))

class Menus(Resource):

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

        super(Menus, self).__init__()

    def get(self, menu_id):
        menu = MenusModel.get_one('menu', id=menu_id)
        if menu:
            return make_response(jsonify({'menu': MenusModel.menu_details(menu)}))
        return make_response(jsonify({'message': 'menu item does not exist'}), 404)

    def put(self, menu_id):
        kwargs = self.reqparse.parse_args()
        menu_item = kwargs.get('menu_item')
        price = kwargs.get('price')

        menu = MenusModel.get_one('menu', id=menu_id)
        if not menu:
            return make_response(jsonify({'message': 'menu item does not exist'}), 404)
        data = {}
        if menu_item:
            data.update({'menu_item': str(menu_item)})
        if price:
            data.update({'price': str(price)})
        MenusModel.update('menu', id=menu[0], data=data)
        menu = MenusModel.get_one('menu', id=menu_id)
        return make_response(jsonify({'message': 'menu has been updated successfully', 'new_menu': MenusModel.menu_details(menu)}), 200)

    def delete(self, menu_id):

        menu = MenusModel.get_one('menu', id=menu_id)
        if menu:
            MenusModel.delete('menu', id=menu[0])
            return make_response(jsonify({'message': 'menu item has been deleted'}))
        return make_response(jsonify({'message': 'menu item does not exist'}))

menus_api = Blueprint('resources.menus', __name__)
api = Api(menus_api)
api.add_resource(MenusList, '/menus', endpoint='menus')
api.add_resource(Menus, '/menus/<int:menu_id>', endpoint='menu')
