"""
This module facilitates testing
"""
import unittest
import os
import sys
import json
from tests.v2.base_setup import BaseTests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MealsTests(BaseTests):
    """
    This class contains tests for menu
    """

    def test_admin_successfully_creates_new_meal(self):
        """
        This method tests admin successfully creating a new meal
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_admin_posting_a_meal_that_already_exist(self):
        """
        This method tests admin  creating a conflicting meal
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'meal with that name already exist')

    def test_admin_getting_all_meals(self):
        """
        This method tests admin successfully getting all meals
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        response = self.client().get('/api/v2/meals', headers=headers, 
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_a_single_meal(self):
        """
        This method tests admin successfully getting a single meal
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/api/v2/meals/1', headers=headers, 
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_getting_single_meal_that_does_not_exist(self):
        """
        This method tests admin getting a single meal that does not exist
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/api/v2/meals/2', headers=headers, 
        content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'meal item does not exist')

    def test_admin_successfully_updates_a_meal(self):
        """
        This method tests admin successfully updating a meal
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v2/meals/1', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 45}), 
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_updates_a_meal_that_does_not_exist(self):
        """
        This method tests admin updating a meal that does not exist
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v2/meals/2', headers=headers, 
        data=json.dumps({'mealname': 'chicken', 'price': 45}), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_admin_successfully_deletes_a_meal(self):
        """
        This method tests admin successfully deleting a meal
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().delete('/api/v2/meals/1', headers=headers, 
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_admin_deletes_non_existing_meal(self):
        """
        This method tests admin unsuccessfully deleting a non existing meal
        """
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().delete('/api/v2/meals/2', headers=headers, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'meal item does not exist')

if __name__ == '__main__':
    unittest.main()
