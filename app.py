"""
Create an app instance, register the blueprints and run the Flask App
"""
import os
from flask import Flask

from resources.meals import meals_api
from resources.users import users_api

def create_app():
    """
    Create the flask app
    """
    app = Flask(__name__)
    app.config.from_object('config.Development')
    app.url_map.strict_slashes = False
    
    app.register_blueprint(meals_api, url_prefix='/api/v1')
    app.register_blueprint(users_api, url_prefix='/api/v1')

    return app

app = create_app()


@app.route('/')
def hello_world():
    return 'Welcome to Fast Food Fast API'


if __name__ == '__main__':
    app.run(debug=True)
