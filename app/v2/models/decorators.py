from functools import wraps
from flask import request, make_response, jsonify
from .models import UserModel

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        access_token = None
        try:
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                access_token = authorization_header.split(' ')[1]
            if access_token:
                user_id = UserModel.decode_token(access_token)['user_id']
                return f(user_id=user_id, *args, **kwargs)
            return make_response(jsonify({'message': 'your session is expired. please login again'}), 401)
        except Exception as e:
            raise e
    return decorated
