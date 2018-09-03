from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

meals = [
    {
        "id" : 1,
        "name" : "Rice & Beef",
        "price" : 160
    },
    {
        "id": 2,
        "name" : "Chapati & Kuku",
        "price" : 300
    },

    {
        "id" : 3,
        "name" : "Ugali & Kales",
        "price" : 50
    },

    {
        "id" : 4,
        "name" : "Ugali & Fish",
        "price" : 200
    }
]


class Meals(Resource):

    def post(self):
        """
        This method adds a new meal to meals list
        """
        
        json_data = request.get_json(force=True)
        id = len(meals) + 1
        name = json_data['name']
        price = json_data['price']
        meal = {"id" : id, "name" : name, "price" : price}
        meals.append(meal)
        return jsonify({"meals" : meals})


api.add_resource(Meals, '/api/v1/meals')
