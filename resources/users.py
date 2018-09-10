"""
Contains all endpoints to manipulate user information
"""
from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api, reqparse, inputs
import models as data

class Signup(Resource):
    """
    Has post method to register new user
    """

    def __init__(self):
        """
        Validates input from form as well as json input
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='kindly provide a valid username',
            type=inputs.regex(r"(.*\S.*)"),
            location=['form', 'json']) 
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            trim=True,
            help='kindly provide a valid confirmation password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'admin',
            required=False,
            default=False,
            type=bool,
            location=['form', 'json'])
        super(Signup, self).__init__()

    def post(self):
        """
        Register a new user
        """
        kwargs = self.reqparse.parse_args()
        for user_id in data.ALL_USERS:
            if data.ALL_USERS.get(user_id)['email'] == kwargs.get('email'):
                return jsonify({"message" : "user with that email already exist"})

        if kwargs.get('password') == kwargs.get('confirm_password'):
            if len(kwargs.get('password')) >= 8:
                result = data.User.create_user(**kwargs)
                return make_response(jsonify(result), 201)
            return jsonify({"message" : "password should be atleast 8 characters"})
        return jsonify({"message" : "password and confirm password should be identical"})

class Login(Resource):
    """
    Contains post method to login a user
    """

    def __init__(self):
        """
        Validates input from the form as well as json input
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        super(Login, self).__init__()

    def post(self):
        """
        Logs in a user
        """
        kwargs = self.reqparse.parse_args()
        for user_id in data.ALL_USERS:
            if data.ALL_USERS.get(user_id)['email'] == kwargs.get('email') and \
                data.ALL_USERS.get(user_id)['password'] == kwargs.get('password'):
                return make_response(jsonify(
                    {"message" : "you have successfully logged in"}), 200)
            return make_response(jsonify({"message" : "invalid email address or password"}), 401)

class UserList(Resource):
    """
    Contain get method to return all the users available
    """

    def get(self):
        """
        Get all users
        """
        return make_response(jsonify(data.ALL_USERS), 200)

class User(Resource):
    """
    Contains get, put and delete methods to manipulate a particular user
    """

    def __init__(self):
        "Validates input from the form as well as json input"
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='kindly provide a valid username',
            type=inputs.regex(r"(.*\S.*)"),
            location=['form', 'json'])
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            trim=True,
            help='kindly provide a valid confirmation password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'admin',
            required=False,
            default=False,
            type=bool,
            location=['form', 'json'])
        super(User, self).__init__()

    def get(self, user_id):
        """
        Get a particular user
        """
        try:
            user = data.ALL_USERS[user_id]
            return make_response(jsonify(user), 200)
        except KeyError:
            return make_response(jsonify({"message" : "user does not exist"}), 401)

    def put(self, user_id):
        """
        Update a particular user
        """
        kwargs = self.reqparse.parse_args()
        result = data.User.update_user(user_id, **kwargs)
        if result != {"message" : "user does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

    def delete(self, user_id):
        """
        Delete a particular user
        """
        result = data.User.delete_user(user_id)
        if result != {"message" : "user does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)


USERS_API = Blueprint('resources.users', __name__)
API = Api(USERS_API)
API.add_resource(Signup, '/auth/signup', endpoint='signup')
API.add_resource(Login, '/auth/login', endpoint='login')
API.add_resource(UserList, '/users', endpoint='users')
API.add_resource(User, '/users/<int:user_id>', endpoint='user')
