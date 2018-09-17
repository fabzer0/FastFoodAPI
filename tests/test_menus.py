"""
This module facilitates testing
"""
import unittest
import json
import sys
import os
from .base_setup import BaseTest
from models import ALL_MENU
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MenuTest(BaseTest):
    """
    This class contains tests to menus
    """

    def test_menu_creation(self):
        """
        This method test to confirm two menus have been created
        """
        first_menu = self.client().post('/api/v1/menu', data=self.menu_1)
        self.assertEqual(first_menu.status_code, 201)
        result_1 = json.loads(first_menu.data.decode('utf-8'))
        self.assertEqual(result_1['menu_option'], 'Ugali & Kuku')
        second_meal = self.client().post('/api/v1/menu', data=self.menu_2)
        self.assertEqual(second_meal.status_code, 201)
        result_2 = json.loads(second_meal.data.decode('utf-8'))
        self.assertEqual(result_2['menu_option'], 'Chapati & Kuku')
        self.assertTrue(len(ALL_MENU) > 0)

    def test_get_all_menu(self):
        """
        This method tests successful return of menu
        """
        response = self.client().get('/api/v1/menu')
        self.assertEqual(response.status_code, 200)

    def test_get_one_menu(self):
        """
        This method tests successful return of a unique menu
        """
        res = self.client().post('/api/v1/menu', data={'menu_option': 'Rice & Beef', 'price': 60})
        self.assertEqual(res.status_code, 201)
        response = self.client().get('/api/v1/menu/1')
        self.assertEqual(response.status_code, 200)

    def test_edit_a_menu(self):
        """
        This method tests successful update of a menu
        """
        res = self.client().post('/api/v1/menu', data={'menu_option': 'Rice & Fish', 'price': 90})
        self.assertEqual(res.status_code, 201)
        response = self.client().put('/api/v1/menu/1',
                                     data={'menu_option': 'Rice & Fish', 'price': 70})
        self.assertEqual(response.status_code, 200)

    def test_delete_a_menu(self):
        """
        This method tests successful deletion of menu
        """
        self.client().post('/api/v1/menu', data={'menu_option': 'Ugali & Ndengu', 'price': 40})
        self.client().post('/api/v1/menu', data={'menu_option': 'Fries', 'price': 90})
        response = self.client().delete('/api/v1/menu/2')
        self.assertEqual(response.status_code, 200)
        # test to see if it still exist, should return 404
        result = self.client().get('/api/v1/menu/2')
        self.assertEqual(result.status_code, 404)

    def test_create_menu_that_already_exist(self):
        """
        This method tests return of error if menu that already exist is recreated
        """
        res = self.client().post('/api/v1/menu', data={'menu_option': 'Samaki', 'price': 79})
        self.assertEqual(res.status_code, 201)
        response = self.client().post('/api/v1/menu', data={'menu_option': 'Samaki', 'price': 79})
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result, {'message': 'menu option with that name already exist'})

    def test_get_menu_that_doest_not_exist(self):
        """
        This method tests return of error for getting a non existing menu
        """
        self.client().post('/api/v1/menu', data={'menu_option': 'Beef Stew', 'price': 70})
        res = self.client().get('/api/v1/menu/2')
        self.assertEqual(res.status_code, 404)

    def test_updating_non_existing_menu(self):
        """
        Tests updating a meal that does not exist
        """
        data = {"menu_option" : "Pilau & Ndengu", "price" : 600}
        self.client().post('/api/v1/menu', data=data)
        response = self.client().put('/api/v1/menu/27', data=json.dumps(dict(price=340)))
        self.assertEqual(response.status_code, 400)

    def test_delete_a_menu_that_does_not_exist(self):
        """
        The method tests deletion of a non existing menu
        """
        self.client().post('/api/v1/menu', data={'menu_option': 'Beef Stew', 'price': 70})
        res = self.client().delete('/api/v1/menu/2')
        self.assertEqual(res.status_code, 404)

    def test_create_menu_empty_menu_option(self):
        """
        Tests return of error if menu option is empty during creation
        """
        res = self.client().post('/api/v1/menu', data={'menu_option': '', 'price': 98})
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result, {'message': {'menu_option': 'kindly provide a menu option'}})

    def test_create_menu_empty_price(self):
        """
        Tests return of error if price is empty during creation
        """
        res = self.client().post('/api/v1/menu', data={'menu_option': 'Nyama Choma', 'price': ''})
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result,
                         {'message': {'price': 'kindly provide a price(should be a valid number)'}})

    def test_create_menu_with_invalid_price(self):
        """
        This method returns error if one tries to create menu with an invalid price
        """
        data = {"menu_option" : "Rice & Pork", "price" : "one hundred"}
        response = self.client().post('/api/v1/menu', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price": "kindly provide a price(should be a valid number)"})




if __name__ == '__main__':
    unittest.main()
