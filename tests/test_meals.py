import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

app = app.create_app()
app.config.from_object('config.Testing')


class MealTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.meal = json.dumps({"meal_item" : "Ugali & Kuku", "price" : 350})
        self.menu = json.dumps({"meal_option" : "Ugali & Kuku", "price" : 350})
        self.order = json.dumps({"order_item" : "Ugali & Kuku", "price" : 350})
        self.existing_meal = self.app.post('/api/v1/meals', data=self.meal, content_type='application/json')
        self.existing_menu = self.app.post('/api/v1/menu', data=self.menu, content_type='application/json')
        self.existing_order = self.app.post('/api/v1/orders', data=self.order, content_type='application/json')


    def test_get_all_meals(self):
        response = self.app.get('/api/v1/meals')
        self.assertEqual(response.status_code, 200)

    def test_successful_meal_creation(self):
        data = json.dumps({"meal_item" : "Ugali & Nyama", "price" : 100})
        response = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("meal_item"), "Ugali & Nyama")
        self.assertEqual(result.get("price"), 100)
        self.assertEqual(response.status_code, 201)

    def test_meal_existence(self):
        data = json.dumps({"meal_item" : "Fries & Chicken", "price" : 250})
        response1 = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        response2 = self.app.post('/api/v1/meals', data=data, content_type='application/json')
        result = json.loads(response2.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "meal item with that name already exist")

    def test_return_one_meal(self):
        response = self.app.get('/api/v1/meals/1')
        self.assertEqual(response.status_code, 200)

    def test_return_error_if_meal_does_not_exist(self):
        response = self.app.get('/api/v1/meals/12')
        self.assertEqual(response.status_code, 404)

    def test_successful_meal_update(self):
        data = json.dumps({"meal_item" : "Pilau & Nyama", "price" : 340})
        response = self.app.put('/api/v1/meals/1', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_non_existing_meal(self):
        data = json.dumps({"meal_item" : "Pilau & Kuku", "price" : 200})
        response = self.app.put('/api/v1/meals/30', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_successful_meal_deletion(self):
        response = self.app.delete('/api/v1/meals/30')
        self.assertEqual(response.status_code, 200)

    #def test_deleting_non_existing_meal(self):
        #response = self.app.delete('/api/v1/meals/130')
        #self.assertEqual(response.status_code, 404)


    #menu
    def test_get_all_menu(self):
        response = self.app.get('/api/v1/menu')
        self.assertEqual(response.status_code, 200)

    def test_successful_menu_creation(self):
        data = json.dumps({"menu_option" : "Chapati & Kuku", "price" : 250})
        response = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('menu_option'), 'Chapati & Kuku')
        self.assertEqual(result.get('price'), 250)
        self.assertEqual(response.status_code, 201)

    def test_create_menu_that_already_exist(self):
        data = json.dumps({"menu_option" : "Cofee", "price" : 240})
        response1 = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        response2 = self.app.post('/api/v1/menu', data=data, content_type='application/json')
        result = json.loads(response2.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu option with that name already exist')

    def test_get_one_menu(self):
        response = self.app.get('/api/v1/menu/1')
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_menu(self):
        response = self.app.get('/api/v1/menu/11')
        self.assertEqual(response.status_code, 404)

    def test_successful_menu_update(self):
        data = json.dumps({"menu_option" : "Chapati", "price" : 20})
        response = self.app.put('/api/v1/menu/2', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    #def test_updating_non_existing_menu(self):
        #data = json.dumps({"menu_option" : "Rice", "price" : 20})
        #response = self.app.put('/api/v1/menu/1', data=data, content_type='application/json')
        #self.assertEqual(response.status_code, 404)

    def test_successful_menu_deletion(self):
        response = self.app.delete('api/v1/menu/1')
        self.assertEqual(response.status_code, 200)

    def test__menu_deletion_non_existing(self):
        response = self.app.delete('api/v1/menu/55')
        self.assertEqual(response.status_code, 404)


    #orders
    def test_get_all_orders(self):
        response = self.app.get('api/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_get_one_order(self):
        response = self.app.get('api/v1/orders/2')
        self.assertEqual(response.status_code, 200)

    def test_successful_order_creation(self):
        data = json.dumps({"order_item" : "Tea", "price" : 340})
        response = self.app.post('api/v1/orders', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('order_item'), 'Tea')
        self.assertEqual(result.get('price'), 340)
        self.assertEqual(response.status_code, 201)

    def test_get_non_existing_orderr(self):
        response = self.app.get('api/v1/orders/24')
        self.assertEqual(response.status_code, 404)

    def test_successful_order_update(self):
        data = json.dumps({"order_item" : "Beans", "price" : 320})
        response = self.app.put('api/v1/orders/2', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_non_existing_order(self):
        data = json.dumps({"order_item" : "Bread", "price" : 70})
        response = self.app.put('api/v1/orders/28', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_successful_order_deletion(self):
        response = self.app.delete('api/v1/orders/2')
        self.assertEqual(response.status_code, 200)

    def test_deletion_non_existing_order(self):
        response = self.app.delete('api/v1/orders/33')
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main()
