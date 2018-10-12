from functools import wraps
from flask import jsonify, request, make_response
from .models import UserModel

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({'message': 'You did not provide authorization which is required for this operation.'}), 401)
        try:
            user_id = UserModel.decode_token(token)['id']
        except:
            return make_response(jsonify({'message': 'error while decoding token'}), 401)
        return f(user_id=user_id, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({'message': 'You did not provide authorization which is required for this operation.'}), 401)
        try:
            data = UserModel.decode_token(token)
            admin = data['admin']
        except:
            return make_response(jsonify({'message': 'error while decoding token'}), 401)
        if not admin:
            return make_response(jsonify({'message': 'You are not allowed to perform the operation.'}), 403)
        return f(*args, **kwargs)
    return decorated
