"""
This module facilitates testing
"""
import unittest
import os
import sys
import json
from tests.v2.base_setup import BaseTests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MenuTests(BaseTests):
    """
    This class contains tests for menu
    """

    def test_get_all_menu(self):
        """
        This method tests if an admin successfully gets all menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers,
        data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('api/v2/menu')
        self.assertEqual(response.status_code, 200)

    def test_get_a_particular_menu(self):
        """
        This method tests if an admin successfully gets a particular menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers,
        data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('api/v2/menu/1')
        self.assertEqual(response.status_code, 200)

    def test_get_a_particular_menu_that_doesnt_exist(self):
        """
        This method tests if an admin successfully gets a particular menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers,
        data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('api/v2/menu/2')
        self.assertEqual(response.status_code, 404)

    def test_admin_create_menu(self):
        """
        This method tests a successful creation of menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers,
        data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_admin_create_menu_that_already_exist(self):
        """
        This method tests a successful creation of menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        response = self.client().post('/api/v2/menu', headers=headers,
        data=json.dumps({'meal_id': 1}), content_type='application/json')
        response = self.client().post('/api/v2/menu', headers=headers,
        data=json.dumps({'meal_id': 1}), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'meal already in menu')

    def test_admin_delete_a_particular_menu(self):
        """
        This method tests successful deletion of a particular menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().delete('/api/v2/menu/1', headers=headers,
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_a_particular_menu_that_doesnt_exist(self):
        """
        This method tests successful deletion of a particular menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers,
        data=json.dumps({'mealname': 'chicken', 'price': 90, 'image': 'https://images-na.ssl-images-amazon.com/images/I/811UdGCb9LL._SL1500_.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().delete('/api/v2/menu/4', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
