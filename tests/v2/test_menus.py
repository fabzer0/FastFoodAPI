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
        response = self.client().get('api/v2/menu')
        self.assertEqual(response.status_code, 200)


    def test_get_a_particular_menu(self):
        """
        This method tests if an admin successfully gets a particular menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client().get('api/v2/menu')
        self.assertEqual(response.status_code, 200)
        

    def test_admin_create_menu(self):
        """
        This method tests a successful creation of menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_admin_delete_a_particular_menu(self):
        """
        This method tests successful deletion of a particular menu
        """
        admin_response = self.logged_in_admin()
        token = json.loads(admin_response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client().post('/api/v2/menu', headers=headers, data=json.dumps({'meal_id': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client().delete('/api/v2/menu/1', headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
