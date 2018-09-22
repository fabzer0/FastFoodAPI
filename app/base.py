from flask import Flask

from app.v1.resources.meals import MEALS_API
from app.v1.resources.users import USERS_API
from instance.config import app_config

def create_app(env_settings):
    """
    Create the flask app
    """
    app = Flask(__name__)
    app.config.from_object(app_config[env_settings])
    app.url_map.strict_slashes = False
    app.register_blueprint(MEALS_API, url_prefix='/api/v1')
    app.register_blueprint(USERS_API, url_prefix='/api/v1')

    return app
