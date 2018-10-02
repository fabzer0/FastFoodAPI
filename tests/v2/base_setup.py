
"""
This module sets up information needed for testing
"""
import sys
import os
import unittest
import json

from app.v2.models.createdb import main, connect_to_db
from app.basev2 import create_app
from instance.v2.config import app_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaseTests(unittest.TestCase):
    def setUp(self):
        main('testing')
        self.app = create_app()
        with self.app.app_context():
            from app.v2.models.models import UserModel, OrdersModel, MealsModel
        self.client = self.app.test_client

        self.user_data = {
            'username': 'fabisch',
            'email': 'fabischapeli97@gmail.com',
            'password': 'secretsanta',
            'confirm_password': 'secretsanta'
        }

        self.admin_data = {
            'username': 'admin',
            'email': 'admin@gmail.com',
            'password': 'secretsanta',
            'confirm_password': 'secretsanta'
        }

        self.user_data_1 = {
            'username': 'jamal',
            'email': 'jamal@gmail.com',
            'password': 'secretsanta',
            'confirm_password': 'secretsanta'
        }

        self.order_data = {
            'ordername': 'Rice Chicken',
            'price': 45
        }

        self.order_data_1 = {
            'ordername': '',
            'price': 45
        }

        self.order_data_2 = {
            'ordername': 'Chicken Burger',
            'price': 'ninety'
        }

    def logged_in_user(self):
        self.client().post('/api/v2/auth/signup', data=json.dumps(self.user_data), content_type='application/json')
        res = self.client().post('/api/v2/auth/login', data=json.dumps({'email': 'fabischapeli97@gmail.com', 'password': 'secretsanta'}), content_type='application/json')
        return res

    def logged_in_admin(self):
        self.client().post('/api/v2/auth/signup', data=json.dumps(self.admin_data), content_type='application/json')
        res = self.client().post('/api/v2/auth/login', data=json.dumps({'email': 'admin@gmail.com', 'password': 'secretsanta'}), content_type='application/json')
        return res


    def tearDown(self):
        conn = connect_to_db('testing')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS users CASCADE')
        cur.execute('DROP TABLE IF EXISTS menu CASCADE')
        cur.execute('DROP TABLE IF EXISTS orders CASCADE')

        conn.commit()
        cur.close()
        conn.close()
