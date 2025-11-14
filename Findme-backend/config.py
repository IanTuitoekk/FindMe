import os

class Config:
    # Secret key for sessions and JWT
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'findme-secret-key-2024'
    
    # PostgreSQL database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://findme_user:grouptwo@localhost:5432/findme_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CORS settings
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    # Development configuration
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    # Production configuration
    DEBUG = False
    TESTING = False
    # Require DATABASE_URL in production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}