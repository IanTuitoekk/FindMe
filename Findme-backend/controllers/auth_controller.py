# authentication business logic and validation functions

def validate_user_data(name, email, password):
    """validate user registration data before creating account"""
    errors = []
    
    # check if name meets minimum requirements
    if not name or len(name.strip()) < 2:
        errors.append("name must be at least 2 characters long")
    
    # validate email format
    if not email or '@' not in email:
        errors.append("please provide a valid email address")
    
    # ensure password meets security requirements
    if not password or len(password) < 6:
        errors.append("password must be at least 6 characters long for security")
    
    return errors

def generate_token(user_id, email):
    """generate jwt token for authenticated users"""
    import jwt
    import datetime
    
    SECRET_KEY = "findme-secret-key-2024"
    
    # create token with user information and expiration
    return jwt.encode({
        'user_id': user_id,
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')
