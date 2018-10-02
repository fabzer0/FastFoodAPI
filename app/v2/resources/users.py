from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api, reqparse, inputs
from ..models.decorators import admin_required
from ..models.models import UserModel
import os

class SignUp(Resource):

    def __init__(self):
        """
        Validates both json and form-data input
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
        super(SignUp, self).__init__()


    def post(self):
        """
        Register a new user
        """
        kwargs = self.reqparse.parse_args()
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        confirm_password = kwargs.get('confirm_password')
        username_exist = UserModel.get_one('users', username=username)
        if username_exist:
            return make_response(jsonify({'message': 'username already taken'}), 400)
        if password == confirm_password:
            if len(password) >= 8:
                email_exists = UserModel.get_one('users', email=email)
                if not email_exists:
                    if username == os.getenv('ADMIN'):
                        user = UserModel(username=username, email=email, password=password)
                        user.create_user()
                        fetch_admin = UserModel.get_one('users', username=username)
                        data = {'admin': True}
                        UserModel.update('users', id=fetch_admin[0], data=data)
                        user = UserModel.get_one('users', id=fetch_admin[0])
                        return jsonify({'admin': UserModel.user_details(user)})
                    user = UserModel(username=username, email=email, password=password)
                    user.create_user()
                    user = UserModel.get_one('users', username=username)
                    return make_response(jsonify({'message': 'successfully registered', 'user': UserModel.user_details(user)}), 201)
                return make_response(jsonify({'message': 'email already taken'}), 203)
            return make_response(jsonify({'message': 'password should be atleast 8 characters'}), 400)
        return make_response(jsonify({"message" : "password and confirm password should be identical"}), 400)


class AllUsers(Resource):

    @admin_required
    def get(self):
        users = UserModel.get_all('users')
        if not users:
            return jsonify({'message': 'no users found yet'})

        return make_response(jsonify({'all_users': [UserModel.user_details(user) for user in users]}))

class PromoteUser(Resource):

    @admin_required
    def put(self, user_id):
        user = UserModel.get_one('users', id=user_id)
        if not user:
            return jsonify({'message': 'user not found'})
        data = {'admin': True}
        UserModel.update('users', id=user[0], data=data)
        user = UserModel.get_one('users', id=user_id)
        return jsonify({'user': UserModel.user_details(user)})


class Login(Resource):

    def __init__(self):
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

        kwargs = self.reqparse.parse_args()
        email = kwargs.get('email')
        password = kwargs.get('password')
        user = UserModel.get_one('users', email=email)

        if user is None:
            return make_response(jsonify({'message': 'invalid email or password'}), 404)

        if UserModel.validate_password(password=password, email=user[2]):
            token = UserModel.generate_token(user)
            return make_response(jsonify({'message': 'you are successfully logged in', 'token': token}), 200)
        return make_response(jsonify({'message': 'invalid email or password'}), 401)



users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(SignUp, '/auth/signup', endpoint='signup')
api.add_resource(AllUsers, '/users')
api.add_resource(PromoteUser, '/users/<int:user_id>')
api.add_resource(Login, '/auth/login', endpoint='login')
