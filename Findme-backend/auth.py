from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Create a blueprint for auth routes (like a mini-app for authentication)
auth_bp = Blueprint('auth', __name__)

# Temporary user storage - we'll replace this with a real database later
users = []
SECRET_KEY = "findme-secret-key-2024"  # Key for signing tokens

# Route for user registration
@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    try:
        # Get user data from the request
        data = request.get_json()
        
        # Check if all required fields are provided
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Please provide name, email and password'}), 400
        
        # Check if email is already registered
        for user in users:
            if user['email'] == data['email']:
                return jsonify({'error': 'This email is already registered'}), 400
        
        # Create new user with hashed password
        new_user = {
            'id': len(users) + 1,
            'name': data['name'],
            'email': data['email'],
            'password': generate_password_hash(data['password']),  # Hash the password!
            'created_at': datetime.datetime.now().isoformat()
        }
        
        users.append(new_user)
        
        # Create a secure token for the user (lasts 24 hours)
        token = jwt.encode({
            'user_id': new_user['id'],
            'email': new_user['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        # Return success response with token
        return jsonify({
            'message': 'Account created successfully!',
            'user_id': new_user['id'],
            'token': token
        }), 201
        
    except Exception as e:
        return jsonify({'error': 'Something went wrong'}), 500

# Route for user login
@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Check if email and password are provided
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
        
        # Find user by email
        user = next((u for u in users if u['email'] == data['email']), None)
        
        # Check if user exists and password is correct
        if not user or not check_password_hash(user['password'], data['password']):
            return jsonify({'error': 'Invalid email or password'}), 401
        
        # Create login token
        token = jwt.encode({
            'user_id': user['id'],
            'email': user['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'message': 'Login successful!',
            'user_id': user['id'],
            'name': user['name'],
            'token': token
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Login failed'}), 500

print("Authentication routes are ready! 🔐")