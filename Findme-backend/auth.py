from flask import Blueprint, request, jsonify
import jwt
import datetime
from models.user import db, User, bcrypt

# create authentication blueprint for organizing auth-related routes
auth_bp = Blueprint('auth', __name__)
SECRET_KEY = "findme-secret-key-2024"

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """handle new user registration with email and password"""
    try:
        # get user data from the request
        data = request.get_json()
        
        # validate that all required fields are provided
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'name, email and password are required'}), 400
        
        # check if a user with this email already exists in postgresql
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({'error': 'a user with this email already exists'}), 400
        
        # create new user instance for postgresql storage
        new_user = User(
            name=data['name'],
            email=data['email']
        )
        # securely hash the password before storing in postgresql
        new_user.set_password(data['password'])
        
        # save the new user to postgresql database
        db.session.add(new_user)
        db.session.commit()
        
        # generate a secure jwt token for the new user
        token = jwt.encode({
            'user_id': new_user.id,
            'email': new_user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        # return success response with user id and token
        return jsonify({
            'message': 'user registered successfully',
            'user_id': new_user.id,
            'token': token
        }), 201
        
    except Exception as e:
        # rollback database changes if anything goes wrong
        db.session.rollback()
        return jsonify({'error': f'registration failed: {str(e)}'}), 500

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """authenticate existing users and provide access token"""
    try:
        data = request.get_json()
        
        # validate login credentials
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'email and password are required'}), 400
        
        # find user in postgresql database by email
        user = User.query.filter_by(email=data['email']).first()
        
        # verify user exists and password is correct
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'invalid email or password'}), 401
        
        # generate new jwt token for the authenticated user
        token = jwt.encode({
            'user_id': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        # return successful login response
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
    """get current user profile using jwt token"""
    token = request.headers.get('Authorization')
    
    # check if token was provided in the request
    if not token:
        return jsonify({'error': 'authentication token is required'}), 401
    
    try:
        # remove 'Bearer ' prefix if present
        if token.startswith('Bearer '):
            token = token[7:]
            
        # decode and verify the jwt token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        
        # find user in postgresql database using token payload
        user = User.query.get(payload['user_id'])
        if not user:
            return jsonify({'error': 'user not found'}), 404
            
        # return user profile information
        return jsonify(user.to_dict()), 200
        
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'your session has expired, please login again'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'invalid authentication token'}), 401