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

    def delete(self, name):
        """
        This method deletes meal from the application
        """
        global meals
        meal = [meal for meal in meals if meal['name'] != name]
        return "{} was deleted.".format(name), 200



api.add_resource(Meals, '/api/v1/meals/<name>')
