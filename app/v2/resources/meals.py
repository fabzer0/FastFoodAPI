from flask import jsonify, Blueprint, make_response
from flask_restful import Resource, inputs, reqparse, Api
from ..models.models import MealsModel
from ..models.decorators import token_required, admin_required


class MealList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'mealname',
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
        super(MealList, self).__init__()

    @admin_required
    def post(self):
        kwargs = self.reqparse.parse_args()
        mealname = kwargs.get('mealname')
        price = kwargs.get('price')
        if price < 0:
            return make_response(jsonify({'message': 'price field cannot be a negative number'}), 400)
        meal = MealsModel.get_one('meals', mealname=mealname)
        if meal:
            return make_response(jsonify({'message': 'meal with that name already exist'}), 409)
        meal = MealsModel(mealname=mealname, price=price)
        meal.create_meal()
        meal = MealsModel.get_one('meals', mealname=mealname)
        return make_response(jsonify({'message': 'meal successfully created', 'meal': MealsModel.meal_details(meal)}), 201)

    @admin_required
    def get(self):
        meals = MealsModel.get_all('meals')
        if not meals:
            return make_response(jsonify({'message': 'no meals yet'}), 404)
        return [MealsModel.meal_details(meal) for meal in meals], 200

class Meal(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'mealname',
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
        super(Meal, self).__init__()

    @admin_required
    def get(self, meal_id):
        meal = MealsModel.get_one('meals', id=meal_id)
        if meal:
            return make_response(jsonify({'meal': MealsModel.meal_details(meal)}), 200)
        return make_response(jsonify({'message': 'meal item does not exist'}), 404)

    @admin_required
    def put(self, meal_id):
        kwargs = self.reqparse.parse_args()
        mealname = kwargs.get('mealname')
        price = kwargs.get('price')
        if price < 0:
            return make_response(jsonify({'message': 'price field cannot be a negative number'}), 400)
        meal = MealsModel.get_one('meals', id=meal_id)
        if not meal:
            return make_response(jsonify({'message': 'meal item does not exist'}), 404)
        data = {}
        if mealname:
            data.update({'mealname': str(mealname)})
        if price:
            data.update({'price': str(price)})
        MealsModel.update('meals', id=meal[0], data=data)
        meal = MealsModel.get_one('meals', id=meal_id)
        return make_response(jsonify({'message': 'meal has been updated successfully', 'new_meal': MealsModel.meal_details(meal)}), 200)

    @admin_required
    def delete(self, meal_id):

        meal = MealsModel.get_one('meals', id=meal_id)
        if meal:
            MealsModel.delete('meals', id=meal[0])
            return make_response(jsonify({'message': 'meal item has been deleted'}), 200)
        return make_response(jsonify({'message': 'meal item does not exist'}), 404)

meals_api = Blueprint('resources.meals', __name__)
api = Api(meals_api)
api.add_resource(MealList, '/meals')
api.add_resource(Meal, '/meals/<int:meal_id>')
