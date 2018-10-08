from flask  import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse, inputs
from ..models.decorators import admin_required, token_required
from ..models.models import MealsModel

class MenuList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'meal_id',
            required=True,
            type=int,
            help='kindly provide a valid meal id',
            location=['form', 'json'])
        super(MenuList, self).__init__()

    @admin_required
    def post(self):

        kwargs = self.reqparse.parse_args()
        meal_id = kwargs.get('meal_id')
        response = MealsModel.add_to_menu(meal_id=meal_id)
        return response

    def get(self):
        meals = MealsModel.get_all('meals')
        if not meals:
            return make_response(jsonify({'message': 'meals not available'}), 404)
        menu = []
        for meal in meals:
            if not meal[3]:
                return make_response(jsonify({'message': 'no meals in menu yet'}), 404)
            else:
                meal = MealsModel.menu_details(meal)
                menu.append(meal)
        return menu, 200

class Menu(Resource):

    def get(self, meal_id):

        response = MealsModel.get_menu(meal_id)
        return response

    def delete(self, meal_id):

        response = MealsModel.remove_from_menu(meal_id=meal_id)
        return response

menu_api = Blueprint('resources.menu', __name__)
api = Api(menu_api)
api.add_resource(MenuList, '/menu')
api.add_resource(Menu, '/menu/<int:meal_id>')
