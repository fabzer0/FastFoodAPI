"""
This module facilitates testing
"""
import unittest
import json
import sys
import os
from base_setup import BaseTest
from models import ALL_ORDERS
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class OrderTest(BaseTest):
    """
    This class contains tests to orders
    """

    def test_order_creation(self):
        """
        This method test to confirm two orders have been created
        """
        first_order = self.client().post('/api/v1/orders', data=self.order_1)
        self.assertEqual(first_order.status_code, 201)
        result_1 = json.loads(first_order.data.decode('utf-8'))
        self.assertEqual(result_1['order_item'], 'Ugali & Kuku')
        second_order = self.client().post('/api/v1/orders', data=self.order_2)
        self.assertEqual(second_order.status_code, 201)
        result_2 = json.loads(second_order.data.decode('utf-8'))
        self.assertEqual(result_2['order_item'], 'Chapati & Kuku')
        self.assertTrue(len(ALL_ORDERS) > 0)

    def test_get_all_orders(self):
        """
        Tests successful retrieval of all orders
        """
        response = self.client().get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_get_one_order(self):
        """
        Tests successful retrieval of a particular order
        """
        res = self.client().post('/api/v1/orders', data={'order_item': 'Rice & Beef', 'price': 60})
        self.assertEqual(res.status_code, 201)
        response = self.client().get('/api/v1/orders/1')
        self.assertEqual(response.status_code, 200)

    def test_edit_an_order(self):
        """
        Tests successful update of an existing order
        """
        res = self.client().post('/api/v1/orders', data={'order_item': 'Rice & Fish', 'price': 90})
        self.assertEqual(res.status_code, 201)
        response = self.client().put('/api/v1/orders/1',
                                     data={'order_item': 'Rice & Fish', 'price': 70})
        self.assertEqual(response.status_code, 200)

    def test_delete_an_order(self):
        """
        Tests successful deletion of an existin order
        """
        self.client().post('/api/v1/orders', data={'order_item': 'Ugali & Ndengu', 'price': 40})
        self.client().post('/api/v1/orders', data={'order_item': 'Fries', 'price': 90})
        response = self.client().delete('/api/v1/orders/2')
        self.assertEqual(response.status_code, 200)
        # test to see if it still exist, should return 404
        result = self.client().get('/api/v1/orders/2')
        self.assertEqual(result.status_code, 404)

    def test_create_order_that_already_exist(self):
        """
        This method tests error returned for creating order that already exist
        """
        data = {"order_item" : "Cofee", "price" : 240}
        self.client().post('/api/v1/orders', data=data)
        response = self.client().post('/api/v1/orders', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'order item with that name already exist')

    def test_get_order_that_doest_not_exist(self):
        """
        Tests error return for getting an order that does not exist
        """
        self.client().post('/api/v1/orders', data={'order_item': 'Beef Stew', 'price': 70})
        res = self.client().get('/api/v1/orders/2')
        self.assertEqual(res.status_code, 404)

    def test_edit_order_that_doest_not_exist(self):
        """
        Tests updating an order that doesnt exist
        """
        self.client().post('/api/v1/orders', data={'order_item': 'Beef Stew', 'price': 70})
        res = self.client().put('/api/v1/orders/2', data={'order_item': 'Beef Stew', 'price': 60})
        self.assertEqual(res.status_code, 400)

    def test_delete_an_order_that_does_not_exist(self):
        """
        Tests error returned for deleting a non existing order
        """
        self.client().post('/api/v1/orders', data={'order_item': 'Beef Stew', 'price': 70})
        res = self.client().delete('/api/v1/orders/2')
        self.assertEqual(res.status_code, 404)

    def test_create_order_empty_order_item(self):
        """
        Tests error returned for submitting empty order item during creation
        """
        res = self.client().post('/api/v1/orders', data={'order_item': '', 'price': 98})
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result, {'message': {'order_item': 'kindly provide an order item'}})

    def test_create_order_empty_price(self):
        """
        Tests error returned for submitting empty price during creation
        """
        res = self.client().post('/api/v1/orders', data={'order_item': 'Nyama Choma', 'price': ''})
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result, {'message':
                                  {'price': 'kindly provide a price(should be a valid number)'}})

    def test_create_order_invalid_price(self):
        """
        This method return error if order is created with an invalid price
        """
        data = {"order_item" : "Ugali & Beef", "price" : "one hundred"}
        response = self.client().post('/api/v1/orders', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price": "kindly provide a price(should be a valid number)"})



if __name__ == '__main__':
    unittest.main()
