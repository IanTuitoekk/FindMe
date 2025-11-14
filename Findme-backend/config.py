import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # use postgresql for team development
    SQLALCHEMY_DATABASE_URI = 'postgresql://findme_user:grouptwo@localhost:5432/findme_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}