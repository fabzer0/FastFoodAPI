"""
This module calls the create app function to run our system
"""

from app.base import create_app


APP = create_app()

@APP.route('/')
def hello_world():
    """
    This method tests if flask is working in the browser
    """
    return 'Welcome to Fast Food Fast API'


if __name__ == '__main__':
    APP.run(debug=True, port=8080)
