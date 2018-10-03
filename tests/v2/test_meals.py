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
        response = self.logged_in_admin()
        token = json.loads(response.data.decode('utf-8'))['token']
        headers = {'Content-Type': 'application/json', 'x-access-token': token}
        response = self.client().post('/api/v2/meals', headers=headers, data=json.dumps({'mealname': 'chicken', 'price': 90}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    


if __name__ == '__main__':
    unittest.main()
