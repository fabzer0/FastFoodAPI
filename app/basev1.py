from flask import Flask

from app.v1.resources.meals import MEALS_API
from app.v1.resources.users import USERS_API

def create_app():

    app = Flask(__name__)
    app.config.from_object('instance.v1.config.Development')
    app.url_map.strict_slashes = False
    app.register_blueprint(MEALS_API, url_prefix='/api/v1')
    app.register_blueprint(USERS_API , url_prefix='/api/v1')

    @app.route('/', methods=['GET'])
    def index_info():
        return 'Welcome to Fast Food Fast Version 1'

    return app
