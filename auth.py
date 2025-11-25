from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)

# Temporary storage (replace with database later)
users = []
SECRET_KEY = "findme-secret-key-2024"

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Name, email and password are required'}), 400
        
        # Check if user already exists
        for user in users:
            if user['email'] == data['email']:
                return jsonify({'error': 'User already exists'}), 400
        
        # Create new user
        new_user = {
            'id': len(users) + 1,
            'name': data['name'],
            'email': data['email'],
            'password': generate_password_hash(data['password']),
            'created_at': datetime.datetime.now().isoformat()
        }
        
        users.append(new_user)
        
        # Generate JWT token
        token = jwt.encode({
            'user_id': new_user['id'],
            'email': new_user['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'message': 'Account created successfully!',
            'user_id': new_user['id'],
            'token': token
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
        
        # Find user
        user = next((u for u in users if u['email'] == data['email']), None)
        
        if not user or not check_password_hash(user['password'], data['password']):
            return jsonify({'error': 'Invalid email or password'}), 401
        
        # Generate JWT token
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

print("Authentication routes loaded successfully!")
