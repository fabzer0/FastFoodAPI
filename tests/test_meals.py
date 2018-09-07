"""
This module facilitates testing
"""
import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app


app = app.create_app()
app.config.from_object('config.Testing')


class MealTest(unittest.TestCase):
    """
    This class contains tests to meals, orders and menus
    """

    def setUp(self):
        self.app = app.test_client()
        self.meal = json.dumps({"meal_item" : "Ugali & Kuku", "price" : 350})
        self.menu = json.dumps({"meal_option" : "Ugali & Kuku", "price" : 350})
        self.order = json.dumps({"order_item" : "Ugali & Kuku", "price" : 350})
        self.existing_meal = self.app.post('/api/v1/meals',
                                           data=self.meal, content_type='application/json')
        self.existing_menu = self.app.post('/api/v1/menu',
                                           data=self.menu, content_type='application/json')
        self.existing_order = self.app.post('/api/v1/orders',
                                            data=self.order, content_type='application/json')

    def test_get_all_meals(self):
        """
        This method tests to return all meals
        """
        response = self.app.get('/api/v1/meals')
        self.assertEqual(response.status_code, 200)

    def test_successful_meal_creation(self):
        """
        This method tests to successfully create a meal
        """
        data = json.dumps({"meal_item" : "Ugali & Nyama", "price" : 100})
        response = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("meal_item"), "Ugali & Nyama")
        self.assertEqual(result.get("price"), 100)
        self.assertEqual(response.status_code, 201)

    def test_meal_existence(self):
        """
        This method tests to check if a unique meal exists
        """
        data = json.dumps({"meal_item" : "Fries & Chicken", "price" : 250})
        self.app.post('/api/v1/meals', data=data, content_type='application/json')
        response = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "meal item with that name already exist")

    def test_create_meal_with_empty_name(self):
        """
        This method tests to check no meal creation if no name provided
        """
        data = json.dumps({"meal_item" : "", "price" : 40})
        response = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"meal_item" : "kindly provide a meal item"})

    def test_create_meal_with_empty_price(self):
        """
        This method checks no meal creation if empty price is submitted
        """
        data = json.dumps({"meal_item" : "Ugali & Chicken", "price" : ""})
        response = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price" : "kindly provide a price(should be a valid number)"})

    def test_create_meal_invalid_price(self):
        """
        This method checks to prevent meal creation if invalid price given
        """
        data = json.dumps({"meal_item" : "Kuku", "price" : "one hundred"})
        response = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price" : "kindly provide a price(should be a valid number)"})

    def test_return_one_meal(self):
        """
        This method tests to check if one meal is returned successfully
        """
        response = self.app.get('/api/v1/meals/1')
        self.assertEqual(response.status_code, 200)

    def test_return_error_if_meal_does_not_exist(self):
        """
        This method tests error to be returned if a meal does not exist
        """
        response = self.app.get('/api/v1/meals/12')
        self.assertEqual(response.status_code, 404)

    def test_successful_meal_update(self):
        """
        This method tests successful update of an existing meal
        """
        data = json.dumps({"meal_item" : "Chapati", "price" : 20})
        response = self.app.put('/api/v1/meals/2', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_update_non_existing_meal(self):
        """
        This method tests error returned if one updates a non-existing meal
        """
        data = json.dumps({"meal_item" : "Pilau & Kuku", "price" : 200})
        response = self.app.put('/api/v1/meals/30', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_successful_meal_deletion(self):
        """
        This method tests a successful meal deletion
        """
        response = self.app.delete('/api/v1/meals/1')
        self.assertEqual(response.status_code, 200)

    def test_deleting_non_existing_meal(self):
        """
        This method tests error returned if one tries to delete a non-existing meal
        """
        response = self.app.delete('/api/v1/meals/130')
        self.assertEqual(response.status_code, 404)


    #menu
    def test_get_all_menu(self):
        """
        This method tests all if all menu is returned successfully
        """
        response = self.app.get('/api/v1/menu')
        self.assertEqual(response.status_code, 200)

    def test_successful_menu_creation(self):
        """
        This method tests if a menu is created successfully
        """
        data = json.dumps({"menu_option" : "Chapati & Kuku", "price" : 250})
        response = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('menu_option'), 'Chapati & Kuku')
        self.assertEqual(result.get('price'), 250)
        self.assertEqual(response.status_code, 201)

    def test_create_menu_that_already_exist(self):
        """
        This method tests error returned if one tries to create menu that already exist
        """
        data = json.dumps({"menu_option" : "Cofee", "price" : 240})
        self.app.post('/api/v1/menu', data=data, content_type='application/json')
        response = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu option with that name already exist')

    def test_create_menu_with_empty_name(self):
        """
        This method return error if one tries to create menu that has no name
        """
        data = json.dumps({"menu_option" : "", "price" : 100})
        response = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"menu_option" : "kindly provide a menu option"})

    def test_create_menu_with_empty_price(self):
        """
        This method tests error returned if one tries to make menu with an empty price
        """
        data = json.dumps({"menu_option" : "Coffee", "price" : ""})
        response = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price" : "kindly provide a price(should be a valid number)"})

    def test_create_menu_with_invalid_price(self):
        """
        This method returns error if one tries to create menu with an invalid price
        """
        data = json.dumps({"menu_option" : "Rice & Pork", "price" : "one hundred"})
        response = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price": "kindly provide a price(should be a valid number)"})

    def test_get_one_menu(self):
        """
        This method tests if a unique menu is returned
        """
        response = self.app.get('/api/v1/menu/1')
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_menu(self):
        """
        This method tests error returned if one tries getting menu that does not exist
        """
        response = self.app.get('/api/v1/menu/11')
        self.assertEqual(response.status_code, 404)

    def test_successful_menu_update(self):
        """
        This method returns successful menu update
        """
        data = json.dumps({"menu_option" : "Chapati", "price" : 20})
        response = self.app.put('/api/v1/menu/2', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_successful_menu_deletion(self):
        """
        This method returns successful menu deletion
        """
        data = json.dumps({"menu_option" : "Rice", "price" : 20})
        response = self.app.delete('api/v1/menu/1', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test__menu_deletion_non_existing(self):
        """
        This method returns error if one tries to delete menu that does not exist
        """
        original_data = json.dumps({"menu_option" : "Rice", "price" : 20})
        response1 = self.app.post('/api/v1/menu', data=original_data,
                                  content_type='application/json')
        self.assertEqual(response1.status_code, 201)
        response2 = self.app.delete('api/v1/menu/2')
        self.assertEqual(response2.status_code, 404)


    #orders
    def test_get_all_orders(self):
        """
        This method tests if all orders are returned successfully
        """
        response = self.app.get('api/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_get_one_order(self):
        """
        This method tests if one order is returned successfully
        """
        response = self.app.get('api/v1/orders/2')
        self.assertEqual(response.status_code, 200)

    def test_successful_order_creation(self):
        """
        This method tests if an order is successfully created
        """
        data = json.dumps({"order_item" : "Tea", "price" : 340})
        response = self.app.post('api/v1/orders', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('order_item'), 'Tea')
        self.assertEqual(result.get('price'), 340)
        self.assertEqual(response.status_code, 201)

    def test_create_order_empty_name(self):
        """
        This method returns error if order is created with an empty name
        """
        data = json.dumps({"order_item" : "", "price" : 400})
        response = self.app.post('/api/v1/orders', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"order_item": "kindly provide an order item"})

    def test_create_order_empty_price(self):
        """
        This method return error if order is created with an empty price
        """
        data = json.dumps({"order_item" : "Ugali & Kuku", "price" : ""})
        response = self.app.post('/api/v1/orders', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price": "kindly provide a price(should be a valid number)"})

    def test_create_order_invalid_price(self):
        """
        This method return error if order is created with an invalid price
        """
        data = json.dumps({"order_item" : "Ugali & Beef", "price" : "one hundred"})
        response = self.app.post('/api/v1/orders', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"),
                         {"price": "kindly provide a price(should be a valid number)"})


    def test_get_non_existing_order(self):
        """
        This method returns error if one tries getting a non existing order
        """
        response = self.app.get('api/v1/orders/24')
        self.assertEqual(response.status_code, 404)

    def test_successful_order_update(self):
        """
        This method tests if an order can be updated successfully
        """
        original_data = json.dumps({"order_item" : "Beans", "price" : 320})
        response1 = self.app.post('api/v1/orders', data=original_data,
                                  content_type='application/json')
        self.assertEqual(response1.status_code, 201)

        new_data = json.dumps({"order_item" : "Beans", "price" : 300})
        response2 = self.app.put('api/v1/orders/1', data=new_data, content_type='application/json')
        self.assertEqual(response2.status_code, 200)

    def test_update_non_existing_order(self):
        """
        This method should return error if a non existing order is updated
        """
        original_data = json.dumps({"order_item" : "Bread", "price" : 70})
        response1 = self.app.post('api/v1/orders', data=original_data,
                                  content_type='application/json')
        self.assertEqual(response1.status_code, 201)

        new_data = json.dumps({"order_item" : "Bread", "price" : 40})
        response2 = self.app.put('api/v1/orders/1', data=new_data, content_type='application/json')
        self.assertEqual(response2.status_code, 200)


    def test_successful_order_deletion(self):
        """
        This method should return a successful order deletion
        """
        response = self.app.delete('api/v1/orders/2')
        self.assertEqual(response.status_code, 200)

    def test_deletion_non_existing_order(self):
        """
        This method should return error if there is deletion of a non-existing order
        """
        response = self.app.delete('api/v1/orders/33')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
