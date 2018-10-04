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
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_wrong_input_for_order_price_field(self):
        """
        This method tests error returned if wrong input for price field is used
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': ''}), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), {"quantity": "quantity field is required"})


    def test_wrong_input_for_order_ordername_field(self):
        """
        This method tests error returned if wrong input for ordername field is used
        """

        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': '', 'quantity': 2}), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), {"item": "item field is required"})


    def test_user_getting_all_orders(self):
        """
        This method tests successful return of all orders by the user
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/api/v2/user/orders', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_getting_a_specific_order(self):
        """
        This method tests successful return of an order by the user
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/api/v2/user/orders/1', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_user_getting_specific_order_that_doesnt_exist(self):
        """
        This method tests return of error if user gets an order that does not exist
        """
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().get('/api/v2/user/orders/1', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'order not found')

    def test_user_deleting_an_order(self):
        """
        This method tests successful deletion of an order
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().delete('/api/v2/user/orders/1', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_all_orders(self):
        """
        This method tests successful getting of orders by an admin
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().get('/api/v2/orders', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_specific_order(self):
        """
        This method tests successful getting of a particular order by an admin
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().get('/api/v2/orders/1', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_specific_order_that_doesnt_exist(self):
        """
        This method tests unsuccessful getting of a particular order by an admin
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().get('/api/v2/orders/99', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'order does not exist')


    def test_admin_editing_an_order(self):
        """
        This method tests a successful updating of an order by an admin
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.logged_in_user()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/user/orders', headers=headers, data=json.dumps({'item': 'chicken', 'quantity': 2}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().put('/api/v2/orders/1', headers=headers, data=json.dumps({'status': 'processing'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
