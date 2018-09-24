"""
Contains all endpoints to manipulate meal information
"""
import sys
import os
import datetime
from flask import jsonify, Blueprint, make_response
from flask_restful import Resource, Api, reqparse, inputs
from ..models import models as data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MealList(Resource):
    """
    Has get and post methods
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'meal_item',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a meal item',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'price',
            required=True,
            type=float,
            help='kindly provide a price(should be a valid number)',
            location=['form', 'json'])
        super(MealList, self).__init__()

    def post(self):
        """
        Adds a new meal item
        """
        kwargs = self.reqparse.parse_args()
        for meal_id in data.ALL_MEALS:
            if data.ALL_MEALS.get(meal_id)['meal_item'] == kwargs.get('meal_item'):
                return jsonify({"message" : "meal item with that name already exist"})
        result = data.Meal.create_meal(**kwargs)
        return make_response(jsonify(result), 201)

    def get(self):
        """
        Returns all meals
        """
        return make_response(jsonify(data.ALL_MEALS), 200)

class Meal(Resource):
    """
    Contains get, put and delete method for manipulating single meal
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'meal_item',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a meal item',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'price',
            required=True,
            type=float,
            help='kindly provide a price(should be a valid number)',
            location=['form', 'json'])
        super(Meal, self).__init__()

    def get(self, meal_id):
        """
        Get a particular meal
        """
        try:
            meal = data.ALL_MEALS[meal_id]
            return make_response(jsonify(meal), 200)
        except KeyError:
            return make_response(jsonify({"message" : "meal item does not exist"}), 404)

    def put(self, meal_id):
        """
        Update a particular meal
        """
        kwargs = self.reqparse.parse_args()
        result = data.Meal.update_meal(meal_id, **kwargs)
        if result != {"message" : "meal item does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

    def delete(self, meal_id):
        """
        Delete a particular meal
        """
        result = data.Meal.delete_meal(meal_id)
        if result != {"message" : "meal item does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

class MenuList(Resource):
    """
    Contains get and post methods for manipulating menu data
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'menu_option',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a menu option',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'price',
            required=True,
            type=float,
            help='kindly provide a price(should be a valid number)',
            location=['form', 'json'])
        super(MenuList, self).__init__()

    def post(self):
        """
        Adds meal option to the menu
        """
        kwargs = self.reqparse.parse_args()
        for menu_id in data.ALL_MENU:
            if data.ALL_MENU.get(menu_id)['menu_option'] == kwargs.get('menu_option'):
                return jsonify({"message" : "menu option with that name already exist"})
        result = data.Menu.create_menu(**kwargs)
        return make_response(jsonify(result), 201)

    def get(self):
        """
        Gets all menu options on the menu
        """
        return make_response(jsonify(data.ALL_MENU), 200)

class Menu(Resource):
    """
    Contains get, put and delete methods for manipulating single menu option
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'menu_option',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a menu option',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'price',
            required=True,
            type=float,
            help='kindly provide a price(should be a valid number)',
            location=['form', 'json'])
        super(Menu, self).__init__()

    def get(self, menu_id):
        """
        Get a particular menu option
        """
        try:
            meal = data.ALL_MENU[menu_id]
            return make_response(jsonify(meal), 200)
        except KeyError:
            return make_response(jsonify({"message" : "menu option does not exist"}), 404)

    def put(self, menu_id):
        """
        Update a particular menu option
        """
        kwargs = self.reqparse.parse_args()
        result = data.Menu.update_menu(menu_id, **kwargs)
        if result != {"message" : "menu option does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

    def delete(self, menu_id):
        """
        Delete a particular menu option
        """
        result = data.Menu.delete_menu(menu_id)
        if result != {"message" : "menu option does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)


class OrderList(Resource):
    """
    Contains get and post methods for manipulating orders
    """

    def __init__(self):
        self.now = datetime.time(8, 59, 59)
        self.closing = datetime.time(16, 59, 59)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'order_item',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide an order item',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'price',
            required=True,
            type=float,
            help='kindly provide a price(should be a valid number)',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'status',
            required=True,
            type=str,
            help='order status cannot be empty',
            location=['form', 'json'])
        super(OrderList, self).__init__()

    def post(self):
        """
        Creates a new order
        """
        kwargs = self.reqparse.parse_args()
        if self.now.hour < self.closing.hour:
            for order_id in data.ALL_ORDERS:
                if data.ALL_ORDERS.get(order_id)["order_item"] == kwargs.get("order_item"):
                    return jsonify({"message": "order item with that name already exist"})
            result = data.Order.create_order(**kwargs)
            return make_response(jsonify(result), 201)
        return make_response(jsonify(
            {"message" : "sorry, you cannot make an order between 5pm and 8am"}), 200)


    def get(self):
        """Gets all orders"""
        return make_response(jsonify(data.ALL_ORDERS), 200)


class Order(Resource):
    """
    Contains get, put and delete methods for manipulating a single order
    """

    def __init__(self):
        self.now = datetime.time(8, 59, 59)
        self.closing = datetime.time(16, 59, 59)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'status',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='status has to be included',
            location=['form', 'json'])
        super(Order, self).__init__()

    def get(self, order_id):
        """Get a particular order"""
        try:
            order = data.ALL_ORDERS[order_id]
            return make_response(jsonify(order), 200)
        except KeyError:
            return make_response(jsonify({"message" : "order item does not exist"}), 404)

    def put(self, order_id):
        """Update a particular order"""
        kwargs = self.reqparse.parse_args()
        status = kwargs.get('status')
        if self.now.hour < self.closing.hour:
            result = data.Order.update_order(order_id, status)
            if result != {"message" : "order item does not exist"}:
                return make_response(jsonify(result), 200)
            return make_response(jsonify(result), 400)
        return make_response(jsonify(
            {"message" : "sorry, you cannot modify an order between 5pm and 8am"}), 200)


    def delete(self, order_id):
        """Delete a particular order"""
        result = data.Order.delete_order(order_id)
        if result != {"message" : "order item does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)


MEALS_API = Blueprint('resources.meals', __name__)
API = Api(MEALS_API)
API.add_resource(MealList, '/meals', endpoint='meals')
API.add_resource(Meal, '/meals/<int:meal_id>', endpoint='meal')
API.add_resource(MenuList, '/menu', endpoint='menus')
API.add_resource(Menu, '/menu/<int:menu_id>', endpoint='menu')
API.add_resource(OrderList, '/orders', endpoint='orders')
API.add_resource(Order, '/orders/<int:order_id>', endpoint='order')
