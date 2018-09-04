

app = Flask(__name__)
api = Api(app)


meals = [
    {
        "id" : 1,
        "name" : "Rice & Beef",
        "price" : 160

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
