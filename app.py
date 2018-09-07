"""
Create an app instance, register the blueprints and run the Flask App
"""
import os
from flask import Flask

from resources.meals import MEALS_API
from resources.users import USERS_API

def create_app():
    """
    Create the flask app
    """
    app = Flask(__name__)
    app.config.from_object('config.Development')
    app.url_map.strict_slashes = False
    app.register_blueprint(MEALS_API, url_prefix='/api/v1')
    app.register_blueprint(USERS_API, url_prefix='/api/v1')

    return app

app = create_app()


@app.route('/')
def hello_world():
    """
    This method tests if flask is working in the browser
    """
    return 'Welcome to Fast Food Fast API'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
