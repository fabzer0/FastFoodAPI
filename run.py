import os
from app.base import create_app


env_name = os.getenv('APP_SETTINGS')
app = create_app(env_name)

@app.route('/')
def hello_world():
    """
    This method tests if flask is working in the browser
    """
    return 'Welcome to Fast Food Fast API'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
