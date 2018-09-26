"""
This module has the function that initializes our flask object
"""
import os
import sys
from flask import Flask
from app.v1.resources.meals import MEALS_API
from app.v1.resources.users import USERS_API

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def create_app():
    """
    Create the flask app
    """
    app = Flask(__name__)
    app.config.from_object('instance.v1.config.Development')
    app.url_map.strict_slashes = False
    app.register_blueprint(MEALS_API, url_prefix='/api/v1')
    app.register_blueprint(USERS_API, url_prefix='/api/v1')

    return app
