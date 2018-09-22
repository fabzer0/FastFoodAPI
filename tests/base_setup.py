"""
This module sets up information needed for testing
"""
import unittest
import sys
import os

from instance.config import app_config

from app.base import create_app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




class BaseTest(unittest.TestCase):
    """
    This is a base class to be inherited by other test classes
    """

    def setUp(self):
        """
        This method sets up information to be used in testing
        """
        env_name = os.getenv('TESTING')
        self.app = create_app(env_name)
        self.client = self.app.test_client
        self.meal_1 = {"meal_item": "Ugali & Kuku", "price": 350}
        self.meal_2 = {"meal_item": "Chapati & Kuku", "price": 250}
        self.menu_1 = {"menu_option": "Ugali & Kuku", "price": 350}
        self.menu_2 = {"menu_option": "Chapati & Kuku", "price": 250}
        self.order_1 = {"order_item": "Ugali & Kuku", "price": 350}
        self.order_2 = {"order_item": "Chapati & Kuku", "price": 250}
        self.user_1 = {
            "username": "fabischapeli",
            "email": "fabischapeli97@gmail.com",
            "password": "secretsanta",
            "confirm_password": "secretsanta"
        }
        self.user_2 = {
            "username": "enockolasi",
            "email": "enockolasi@gmail.com",
            "password": "secretcircle",
            "confirm_password": "secretcircle"
        }
