from datetime import datetime, timedelta
from flask import jsonify, make_response
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from instance.v2.config import app_config
from .createdb import connect_to_db

conn = connect_to_db()
conn.set_session(autocommit=True)
cur = conn.cursor()

class BaseModel(object):
    '''Base class to set up database'''

    def save(self):
        conn.commit()

    @staticmethod
    def get_one(table_name, **kwargs):
        for key, val in kwargs.items():
            query = "SELECT * FROM {} WHERE {}='{}'".format(table_name, key, val)
            cur.execute(query)
            item = cur.fetchone()
            return item

    @staticmethod
    def get_all(table_name):
        query = 'SELECT * FROM {}'.format(table_name)
        cur.execute(query)
        data = cur.fetchall()
        return data

    @staticmethod
    def update(table_name, id, data):
        for key, val in data.items():
            string = "{}='{}'".format(key, val)
            query = 'UPDATE {} SET {} WHERE id={}'.format(table_name, string, id)
            cur.execute(query)
            conn.commit()

    @staticmethod
    def delete(table_name, id):
        query = 'DELETE FROM {} WHERE id={}'.format(table_name, id)
        cur.execute(query)
        conn.commit()

class UserModel(BaseModel):
    """
    Users model class
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def create_user(self):
        cur.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                    (self.username, self.email, self.password))
        self.save()

    @staticmethod
    def user_details(user):
        return dict(
            id=user[0],
            username=user[1],
            email=user[2],
            admin=user[4]
        )

    @staticmethod
    def validate_password(password, email):
        user = UserModel.get_one('users', email=email)
        if check_password_hash(user[3], password):
            return True
        return False

    @staticmethod
    def generate_token(user):
        user_id, admin = user[0], user[4]
        payload = {
            'id': user_id,
            'admin': admin,
            'exp': datetime.utcnow()+timedelta(days=1)
        }
        return jwt.encode(payload, str(app_config['development']), algorithm='HS256').decode('utf-8')

    @staticmethod
    def decode_token(token):
        payload = jwt.decode(token, str(app_config['development']), algorithm='HS256')
        return payload

class MealsModel(BaseModel):

    def __init__(self, mealname, price, image):
        self.mealname = mealname
        self.price = price
        self.image = image

    def create_meal(self):
        cur.execute('INSERT INTO meals (mealname, price, image) VALUES (%s, %s, %s)', (self.mealname, self.price, self.image))
        self.save()

    @staticmethod
    def meal_details(meal):
        return dict(
            id=meal[0],
            mealname=meal[1],
            price=meal[2],
            image=meal[3],
            in_menu=meal[4]
        )


    @staticmethod
    def menu_details(meal):
        return dict(
            id=meal[0],
            mealname=meal[1],
            price=meal[2],
            image=meal[3]
        )

    @staticmethod
    def add_to_menu(meal_id):
        meal = MealsModel.get_one('meals', id=meal_id)
        if not meal:
            return make_response(jsonify({'message': 'meal does not exist'}), 404)
        if meal[4]:
            return make_response(jsonify({'message': 'meal already in menu'}), 409)
        data = {'in_menu': True}
        MealsModel.update('meals', id=meal[0], data=data)
        meal = MealsModel.get_one('meals', id=meal[0])
        return make_response(jsonify({'message': 'meal successfully added to menu', 'meal': MealsModel.meal_details(meal)}), 201)

    @staticmethod
    def remove_from_menu(meal_id):
        meal = MealsModel.get_one('meals', id=meal_id)
        if meal is None:
            return make_response(jsonify({'message': 'meal does not exist'}), 404)
        if not meal[4]:
            return make_response(jsonify({'message': 'meal already not in menu'}), 400)
        data = {'in_menu': False}
        MealsModel.update('meals', id=meal[0], data=data)
        return make_response(jsonify({'message': 'meal successfully removed from menu'}), 200)

    @staticmethod
    def get_menu(meal_id):

        meal = MealsModel.get_one('meals', id=meal_id)
        if meal is None:
            return make_response(jsonify({'message': 'meal does not exist'}), 404)
        if not meal[4]:
            return make_response(jsonify({'message': 'kindly ensure this meal is in the menu'}), 400)
        return make_response(jsonify({'menu': MealsModel.menu_details(meal)}), 200)

class OrdersModel(BaseModel):

    def __init__(self, user_id, item, totalprice):
        self.user_id = user_id
        self.item = item
        self.totalprice = totalprice


    def create_order(self):
        cur.execute('INSERT INTO orders (user_id, item, totalprice) VALUES (%s, %s, %s)', (self.user_id, self.item, self.totalprice))
        self.save()

    @staticmethod
    def get(user_id, order_id=None):
        """
        Method for fetching both single and all orders
        """
        if order_id:
            query = 'SELECT * FROM orders WHERE user_id={} AND id={}'.format(user_id, order_id)
            cur.execute(query)
            return cur.fetchone()
        query = 'SELECT orders.id, users.id, item, totalprice, status, created_at FROM users INNER JOIN orders ON orders.user_id=users.id WHERE users.id={} ORDER BY created_at'.format(user_id)
        cur.execute(query)
        user_orders = cur.fetchall()
        return user_orders

    @staticmethod
    def order_details(order):
        return dict(
            id=order[0],
            item=order[2],
            totalprice=order[3],
            status=order[4]
        )

    @staticmethod
    def admin_order_details(order):
        return dict(
            id=order[0],
            user_id=order[1],
            item=order[2],
            totalprice=order[3],
            status=order[4]
        )
