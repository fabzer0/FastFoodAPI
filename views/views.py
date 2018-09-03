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

    def put(self, name):
        """This method updates an existing meals
        """

        meal = [meal for meal in meals if meal['name'] == name]
        json_data = request.get_json(force=True)
        meal[0]['id'] = meal[0]['id']
        meal[0]['name'] = json_data['name']
        meal[0]['price'] = json_data['price']
        return jsonify({"meal" : meal[0]})


api.add_resource(Meals, '/api/v1/meals/<name>')
