"""Contain interactive doccumentation to help one get started using the API
"""
import os

from flasgger import Swagger

from app import create_app

app = create_app()
swagger = Swagger(app)


# Users
@app.route('/api/v1/auth/signup/', methods=["POST"])
def signup():
    """ endpoint for registering users.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
    """

@app.route('/api/v1/auth/login', methods=["POST"])
def login():
    """ endpoint for logging in users.
    ---
    parameters:
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    """

@app.route('/api/v1/users', methods=["POST"])
def users_signup():
    """ endpoint for registering users.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
    """

@app.route("/api/v1/users", methods=["GET"])
def get_all_users():
    """endpoint for  getting all users.
    No parameters required
    """

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_one_user():
    """endpoint for  getting a particular user.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/users/id', methods=["PUT"])
def update_user():
    """ endpoint for updating an existing user.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
      - name: id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/users/<int:user_id>', methods=["DELETE"])
def delete_user():
    """ endpoint for deleting an existing user.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    """


# Meals
@app.route('/api/v1/meals', methods=["POST"])
def create_meal():
    """ endpoint for creating a meal item.
    ---
    parameters:
      - name: meal_item
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
    """

@app.route("/api/v1/meals", methods=["GET"])
def get_all_meals():
    """endpoint for getting all meals.
    No parameters required
    """

@app.route("/api/v1/meals/<int:meal_id>", methods=["GET"])
def get_one_meal():
    """endpoint for  getting a particular meal.
    ---
    parameters:
      - name: meal_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/meals/<int:meal_id>', methods=["PUT"])
def update_meal():
    """ endpoint for updating an existing meal.
    ---
    parameters:
      - name: meal_item
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
      - name: meal_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/meals/<int:meal_id>', methods=["DELETE"])
def delete_meal():
    """ endpoint for deleting an existing meal.
    ---
    parameters:
      - name: meal_id
        in: path
        type: integer
        required: true
    """


# Menu
@app.route('/api/v1/menu', methods=["POST"])
def create_menu():
    """ endpoint for creating a menu option.
    ---
    parameters:
      - name: menu_option
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
    """

@app.route("/api/v1/menu", methods=["GET"])
def get_all_menu():
    """endpoint for  getting all menu options.
    No parameters required
    """

@app.route("/api/v1/menu/<int:menu_id>", methods=["GET"])
def get_one_menu_option():
    """endpoint for getting a particular menu option.
    ---
    parameters:
      - name: menu_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/menu/<int:menu_id>', methods=["PUT"])
def update_menu():
    """ endpoint for updating an existing menu option.
    ---
    parameters:
      - name: menu_option
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
      - name: menu_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/meals/<int:menu_id>', methods=["DELETE"])
def delete_menu():
    """ endpoint for deleting an existing menu option.
    ---
    parameters:
      - name: menu_id
        in: path
        type: integer
        required: true
    """


# Orders
@app.route('/api/v1/orders', methods=["POST"])
def create_order():
    """ endpoint for creating an order item.
    ---
    parameters:
      - name: order_item
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
    """

@app.route("/api/v1/orders", methods=["GET"])
def get_all_orders():
    """endpoint for  getting all orders.
    No parameters required
    """

@app.route("/api/v1/orders/<int:order_id>", methods=["GET"])
def get_one_order():
    """endpoint for  getting a particular order.
    ---
    parameters:
      - name: order_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/orders/<int:order_id>', methods=["PUT"])
def update_order():
    """ endpoint for updating an existing order.
    ---
    parameters:
      - name: order_item
        required: true
        in: formData
        type: string
      - name: price
        in: formData
        type: float
        required: true
      - name: order_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/orders/<int:order_id>', methods=["DELETE"])
def delete_order():
    """ endpoint for deleting an existing order.
    ---
    parameters:
      - name: order_id
        in: path
        type: integer
        required: true
    """

@app.route('/')
def hello_world():
    "test that flask app is running"
    return "To view the docs visit: https://fast-food-fast-api-97.herokuapp.com/"

if __name__ == "__main__":
    app.run(port=8080)
