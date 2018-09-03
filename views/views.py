from flask import Flask, jsonify
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

    def get(self, name):
        """
        This function returns only one meal as specified
        """
        meal = [meal for meal in meals if meal['name'] == name]
        return jsonify({"meal" : meal[0]})


api.add_resource(Meals, '/api/v1/meals/<name>')
