"""
This module facilitates testing
"""
import unittest
import os
import sys
import json

from base_setup import BaseTests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class MenuTests(BaseTests):
    """
    This class contains tests for menu
    """

    def test_admin_get_all_menu(self):
        """
        This method tests if an admin successfully gets all menu
        """
        response = self.client().get('api/v2/menu')
        self.assertEqual(response.status_code, 200)

    def test_admin_get_a_particular_menu(self):
        """
        This method tests if an admin successfully gets a particular menu
        """
        response = self.client().get('api/v2/menu/1')
        self.assertEqual(response.status_code, 200)

    def test_admin_get_a_particular_menu_that_doesnt_exist(self):
        """
        This method tests an admin trying to get a particular menu that does not exist
        """
        response = self.client().get('api/v2/menu/3')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu item does not exist')

    def test_admin_create_menu(self):
        """
        This method tests a successful creation of menu
        """
        data = {
            "menu_item": "Ugali & Mboga",
            "price": 50
        }
        response = self.client().post('/api/v2/menu', data=data)
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu item successfully created')

    def test_admin_delete_a_particular_menu(self):
        """
        This method tests successful deletion of a particular menu
        """
        response = self.client().delete('/api/v2/menu/1')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu item successfully deleted')

if __name__ == '__main__':
    unittest.main()
