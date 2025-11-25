from flask import Blueprint, request, jsonify
import jwt
import datetime
from models.db import db, bcrypt
from models.user import User

# create authentication blueprint
auth_bp = Blueprint('auth', __name__)
SECRET_KEY = "findme-secret-key-2024"

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """handle user registration with jwt token generation"""
    try:
        data = request.get_json()
        
        # validate required fields
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'name, email and password are required'}), 400
        
        # check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({'error': 'a user with this email already exists'}), 400
        
        # create new user
        new_user = User(
            name=data['name'],
            email=data['email']
        )
        new_user.set_password(data['password'])
        
        # save to database
        db.session.add(new_user)
        db.session.commit()
        
        # generate jwt token
        token = jwt.encode({
            'user_id': new_user.id,
            'email': new_user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'message': 'user registered successfully',
            'user_id': new_user.id,
            'token': token
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'registration failed: {str(e)}'}), 500

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """handle user login and jwt token generation"""
    try:
        data = request.get_json()
        
        # validate required fields
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'email and password are required'}), 400
        
        # find user by email
        user = User.query.filter_by(email=data['email']).first()
        
        # verify user exists and password matches
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'invalid email or password'}), 401
        
        # generate jwt token
        token = jwt.encode({
            'user_id': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'message': 'login successful',
            'user_id': user.id,
            'name': user.name,
            'token': token
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'login failed: {str(e)}'}), 500

@auth_bp.route('/api/auth/me', methods=['GET'])
def get_current_user():
    """get current user details from jwt token"""
    token = request.headers.get('Authorization')
    
    # check if token exists
    if not token:
        return jsonify({'error': 'authentication token is required'}), 401
    
    try:
        # remove 'Bearer ' prefix if present
        if token.startswith('Bearer '):
            token = token[7:]
            
        # decode and verify jwt token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        
        # get user from database
        user = User.query.get(payload['user_id'])
        if not user:
            return jsonify({'error': 'user not found'}), 404
            
        # return user details
        return jsonify(user.to_dict()), 200
        
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'your session has expired, please login again'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'invalid authentication token'}), 401