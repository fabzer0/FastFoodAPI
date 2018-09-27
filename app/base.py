from flask import Flask

from app.v2.resources.menus import menus_api
from app.v2.resources.orders import orders_api
from app.v2.resources.users import users_api

def create_app():
    from app.v2.models.createdb import main
    app = Flask(__name__)
    app.config.from_object('instance.v2.config.TestingEnv')
    app.url_map.strict_slashes = False

    app.register_blueprint(menus_api, url_prefix='/api/v2')
    app.register_blueprint(orders_api, url_prefix='/api/v2')
    app.register_blueprint(users_api, url_prefix='/api/v2')
    main()

    @app.route('/', methods=['GET'])
    def index_info():
        return 'Great, the app works'

    return app
