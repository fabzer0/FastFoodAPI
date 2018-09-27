"""
This module facilitates testing
"""
import unittest
import os
import sys
import json

from tests.v2.base_setup import BaseTests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


USERS_ORDERS_URL = 'api/v2/users/orders'
USERS_ORDERS_SPECIFIC_URL = 'api/v2/users/orders/1'
ADMINS_ORDERS_URL = '/api/v2/orders'
ADMINS_ORDERS_SPECIFIC_URL = '/api/v2/orders/1'


class OrdersTest(BaseTests):
    """
    This class contains methods to tests orders manipulation
    """

    def test_successful_order_creation(self):
        """
        This method tests a successful order creation
        """
        order = {
            "ordername": "Chapati & Chicken",
            "price": 90
        }
        response = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], 'order has been successfully posted')

    def test_wrong_input_for_order_price_field(self):
        """
        This method tests error returned if wrong input for price field is used
        """
        order = {
            'ordername': 'Rice & Beef',
            'price': 'twenty'
        }
        response = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], {'price': 'kindly provide a price(should be a valid number)'})

    def test_wrong_input_for_order_ordername_field(self):
        """
        This method tests error returned if wrong input for ordername field is used
        """
        order = {
            'ordername': '',
            'price': 'twenty'
        }
        response = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], {'ordername': 'kindly provide a valid name'})

    def test_double_ordering(self):
        """
        This method tests double creation of an order
        """
        order = {
            'ordername': 'Rice & Githeri',
            'price': 30
        }
        self.client().post(USERS_ORDERS_URL, data=order)
        response = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(response.status_code, 203)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], 'order with that name already exist')

    def test_user_getting_all_orders(self):
        """
        This method tests successful return of all orders by the user
        """
        response = self.client().get(USERS_ORDERS_URL)
        self.assertEqual(response.status_code, 200)

    def test_user_getting_a_specific_order(self):
        """
        This method tests successful return of an order by the user
        """
        order = {
            'ordername': 'Rice & Githeri',
            'price': 30
        }
        res = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(res.status_code, 201)
        response = self.client().get(USERS_ORDERS_SPECIFIC_URL)
        self.assertEqual(response.status_code, 200)

    def test_user_getting_specific_order_that_doesnt_exist(self):
        """
        This method tests return of error if user gets an order that does not exist
        """
        response = self.client().get(USERS_ORDERS_SPECIFIC_URL)
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'order does not exist')

    def test_user_deleting_an_order(self):
        """
        This method tests successful deletion of an order
        """
        order = {
            'ordername': 'Rice & Soup',
            'price': 30
        }
        response = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(response.status_code, 201)
        res = self.client().delete(USERS_ORDERS_SPECIFIC_URL)
        self.assertEqual(res.status_code, 200)

    def test_admin_getting_all_orders(self):
        """
        This method tests successful getting of orders by an admin
        """
        order = {
            'ordername': 'Chicken & Soup',
            'price': 30
        }
        res = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(res.status_code, 201)
        response = self.client().get(ADMINS_ORDERS_URL)
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_specific_order(self):
        """
        This method tests successful getting of a particular order by an admin
        """
        order = {
            'ordername': 'Chicken & Beef',
            'price': 30
        }
        res = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(res.status_code, 201)
        response = self.client().get(ADMINS_ORDERS_SPECIFIC_URL)
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_specific_order_that_doesnt_exist(self):
        """
        This method tests unsuccessful getting of a particular order by an admin
        """
        response = self.client().get(ADMINS_ORDERS_SPECIFIC_URL)
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'order does not exist')


    def test_admin_editing_an_order(self):
        """
        This method tests a successful updating of an order by an admin
        """
        order = {
            "ordername": "Beans & Chicken",
            "price": 90
        }
        response = self.client().post(USERS_ORDERS_URL, data=order)
        self.assertEqual(response.status_code, 201)
        data = {
            "status": "new"
        }
        res = self.client().put(ADMINS_ORDERS_SPECIFIC_URL, data=data)
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'order has been updated successfully')


if __name__ == '__main__':
    unittest.main()
