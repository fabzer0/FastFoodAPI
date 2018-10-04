from functools import wraps
from flask import jsonify, request
from .models import UserModel


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return {'message': 'kindly provide a valid token in the header'}, 401
        try:
            user_id = UserModel.decode_token(token)['id']    
        except:
            return {'message': 'error while decoding token, session might have expired'}, 401
        return f(user_id=user_id, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return {'message': 'kindly provide a valid token in the header'}
        try:
            data = UserModel.decode_token(token)
            admin = data['admin']
        except:
            return {'message': 'error while decoding token'}
        if not admin:
            return {'message': 'you are not authorized to perform this function as a non admin'}
        return f(*args, **kwargs)
    return decorated



def is_blank(var):
    if var.strip() == '':
        return 'all fields required'
    return None
