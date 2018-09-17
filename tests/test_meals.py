"""
This module facilitates testing
"""
import unittest
import json
import sys
import os
from .base_setup import BaseTest
from models import ALL_MEALS
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MealTest(BaseTest):
    """
    This class contains tests to meals
    """

    def test_meal_creation(self):
        """
        This method test to confirm two meals have been created
        """
        first_meal = self.client().post('/api/v1/meals', data=self.meal_1)
        self.assertEqual(first_meal.status_code, 201)
        result_1 = json.loads(first_meal.data.decode('utf-8'))
        self.assertEqual(result_1['meal_item'], 'Ugali & Kuku')
        second_meal = self.client().post('/api/v1/meals', data=self.meal_2)
        self.assertEqual(second_meal.status_code, 201)
        result_2 = json.loads(second_meal.data.decode('utf-8'))
        self.assertEqual(result_2['meal_item'], 'Chapati & Kuku')
        self.assertTrue(len(ALL_MEALS) > 0)

    def test_get_all_meals(self):
        """
        This method tests if all meals are returned from the app
        """
        response = self.client().get('/api/v1/meals')
        self.assertEqual(response.status_code, 200)

    def test_get_one_meal(self):
        """
        This method tests if a selected meal is returned
        """
        res = self.client().post('/api/v1/meals', data={'meal_item': 'Rice & Beef', 'price': 60})
        self.assertEqual(res.status_code, 201)
        response = self.client().get('/api/v1/meals/1')
        self.assertEqual(response.status_code, 200)

    def test_edit_a_meal(self):
        """
        This method tests a successful update of an existing meal
        """
        res = self.client().post('/api/v1/meals', data={'meal_item': 'Rice & Fish', 'price': 90})
        self.assertEqual(res.status_code, 201)
        response = self.client().put('/api/v1/meals/1',
                                     data={'meal_item': 'Rice & Fish', 'price': 70})
        self.assertEqual(response.status_code, 200)

    def test_delete_a_meal(self):
        """
        This method tests a successful deletion of an existin meal
        """
        self.client().post('/api/v1/meals', data={'meal_item': 'Ugali & Ndengu', 'price': 40})
        self.client().post('/api/v1/meals', data={'meal_item': 'Fries', 'price': 90})
        response = self.client().delete('/api/v1/meals/2')
        self.assertEqual(response.status_code, 200)
        # test to see if it still exist, should return 404
        result = self.client().get('/api/v1/meals/2')
        self.assertEqual(result.status_code, 404)

    def test_create_meal_that_already_exist(self):
        """
        This meal tests error returned if meal name that already exist is submitted during creation
        """
        res = self.client().post('/api/v1/meals', data=self.meal_1)
        self.assertEqual(res.status_code, 201)
        response = self.client().post('/api/v1/meals', data=self.meal_1)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result, {'message': 'meal item with that name already exist'})

    def test_get_meal_that_doest_not_exist(self):
        """
        This method tests error response for getting meal that does not exist
        """
        self.client().post('/api/v1/meals', data={'meal_item': 'Beef Stew', 'price': 70})
        res = self.client().get('/api/v1/meals/2')
        self.assertEqual(res.status_code, 404)

    def test_edit_meal_that_doest_not_exist(self):
        """
        This method returns error for updating a non existing meal
        """
        self.client().post('/api/v1/meals', data={'meal_item': 'Beef Stew', 'price': 70})
        res = self.client().put('/api/v1/meals/2', data={'meal_item': 'Beef Stew', 'price': 60})
        self.assertEqual(res.status_code, 404)

    def test_delete_a_meal_that_does_not_exist(self):
        """
        This method returns an error for deleting a non existing meal
        """
        self.client().post('/api/v1/meals', data={'meal_item': 'Beef Stew', 'price': 70})
        res = self.client().delete('/api/v1/meals/2')
        self.assertEqual(res.status_code, 404)

    def test_create_meal_empty_meal_item(self):
        """
        This method returns an error if meal name is empty during meal creation
        """
        res = self.client().post('/api/v1/meals', data={'meal_item': '', 'price': 98})
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result, {'message': {'meal_item': 'kindly provide a meal item'}})

    def test_create_meal_empty_price(self):
        """
        This method returns an error if price field is empty during meal creation
        """
        res = self.client().post('/api/v1/meals', data={'meal_item': 'Nyama Choma', 'price': ''})
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result,
                         {'message': {'price': 'kindly provide a price(should be a valid number)'}})

    def test_create_meal_invalid_price(self):
        """
        This method checks to prevent meal creation if invalid price given
        """
        response = self.client().post('/api/v1/meals',
                                      data={"meal_item" : "Kuku", "price" : "one hundred"})
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price" : "kindly provide a price(should be a valid number)"})



if __name__ == '__main__':
    unittest.main()
