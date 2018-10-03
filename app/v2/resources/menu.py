from flask  import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse, inputs
from ..models.decorators import admin_required, token_required, jwt_required
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
        menu = []
        for meal in meals:
            # IT COMES BACK AS A TUPLE. IS THERE A WAY TO  MAKE THIS NICE?
            if meal[3]:
                meal = MealsModel.meal_details(meal)
                menu.append(meal)
        return jsonify({'all_menu': menu})

    def delete(self, meal_id):
        response = MealsModel.remove_from_menu(meal_id=meal_id)
        return response
 


menu_api = Blueprint('resources.menu', __name__)
api = Api(menu_api)
api.add_resource(MenuList, '/menu', '/menu/<int:meal_id>')
# api.add_resource(Menu, '/menu/<int:menu_id>')
