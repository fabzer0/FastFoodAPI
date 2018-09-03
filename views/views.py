from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse 

app = Flask(__name__)
api = Api(app)


meals = [
    {
        "id" : 1,
        "name" : "Rice & Beef",
        "price" : 160
    }, 

    {
        "id" : 2,
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
    
    def get(self):
        """
        This function gets all the meals from the meals list
        """

        return meals


api.add_resource(Meals, '/api/v1/meals')