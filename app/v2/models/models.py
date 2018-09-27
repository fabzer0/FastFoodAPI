from datetime import datetime, timedelta
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from instance.v2.config import app_config
from .createdb import connect_to_db


conn = connect_to_db(app_config['development'])
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
            email=user[2]
        )

    @staticmethod
    def validate_password(password, email):
        user = UserModel.get_one('users', email=email)
        if check_password_hash(user[3], password):
            return True
        return False

    @staticmethod
    def generate_token(user):
        user_id, username = user[0], user[1]
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow()+timedelta(days=1),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, str(app_config['development']), algorithm='HS256').decode('utf-8')

    @staticmethod
    def decode_token(token):
        payload = jwt.decode(token, str(app_config['development']), algorithm='HS256')
        return payload


class MenusModel(BaseModel):

    def __init__(self, menu_item, price):
        self.menu_item = menu_item
        self.price = price

    def create_menu(self):
        cur.execute('INSERT INTO menu (menu_item, price) VALUES (%s, %s)', (self.menu_item, self.price))
        self.save()

    @staticmethod
    def menu_details(menu):
        return dict(
            id=menu[0],
            mealname=menu[1],
            price=menu[2]
        )

class OrdersModel(BaseModel):

    def __init__(self, ordername, price, status):
        self.ordername = ordername
        self.price = price
        self.status = status

    def create_order(self):
        cur.execute('INSERT INTO orders (ordername, price, status) VALUES (%s, %s)', (self.ordername, self.price, self.status))
        self.save()

    @staticmethod
    def order_details(order):
        return dict(
            id=order[0],
            mealname=order[1],
            price=order[2]
        )
