

app = Flask(__name__)
api = Api(app)


meals = [
    {
        "id" : 1,
        "name" : "Rice & Beef",
        "price" : 160

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
      
  def put(self, name):
        """This method updates an existing meals
        """

        meal = [meal for meal in meals if meal['name'] == name]
        json_data = request.get_json(force=True)
        meal[0]['id'] = meal[0]['id']
        meal[0]['name'] = json_data['name']
        meal[0]['price'] = json_data['price']
        return jsonify({"meal" : meal[0]})
      
  def delete(self, name):
        """
        This method deletes meal from the application
        """
        global meals
        meal = [meal for meal in meals if meal['name'] != name]
        return "{} was deleted.".format(name), 200


