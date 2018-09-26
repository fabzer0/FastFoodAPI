"""
This module sets up information needed for testing
"""
import sys
import os
import unittest

from app.v2.models.createdb import main, connect_to_db
from app.base import create_app
from instance.v2.config import app_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaseTests(unittest.TestCase):
    def setUp(self):
        main('testing')
        self.app = create_app()
        with self.app.app_context():
            from app.v2.models.models import UserModel, OrdersModel, MenuModel
        self.client = self.app.test_client

    def tearDown(self):
        conn = connect_to_db('testing')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS users CASCADE')
        cur.execute('DROP TABLE IF EXISTS menu CASCADE')
        cur.execute('DROP TABLE IF EXISTS orders CASCADE')

        conn.commit()
        cur.close()
        conn.close()
