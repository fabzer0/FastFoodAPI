"""
This module calls the whole app to run it
"""
from app.base import create_app


app = create_app()

if __name__ == '__main__':
    app.run()
