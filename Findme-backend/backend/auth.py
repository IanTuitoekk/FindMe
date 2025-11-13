from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)

# Temporary in-memory storage (you'll replace with database later)
users = []

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if user already exists
    for user in users:
        if user['email'] == data.get('email'):
            return jsonify({'message': 'User already exists'}), 400
    
    # Create new user
    new_user = {
        'id': len(users) + 1,
        'name': data.get('name'),
        'email': data.get('email'),
        'password': generate_password_hash(data.get('password'))
    }
    
    users.append(new_user)
    return jsonify({'message': 'User registered successfully', 'user_id': new_user['id']}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({'message': 'Login endpoint - work in progress'}), 200

print("Auth routes loaded successfully!")