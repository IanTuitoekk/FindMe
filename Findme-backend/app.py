from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
import os

# Import configuration and database
from config import config
from models.missing_person import db
from auth import auth_bp  # Your authentication routes

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    CORS(app)  # Enable CORS for React frontend
    db.init_app(app)  # Initialize SQLAlchemy
    migrate = Migrate(app, db)  # Initialize flask-migrate
    
    # Register your authentication routes
    app.register_blueprint(auth_bp)

    # Create all database tables
    with app.app_context():
        db.create_all()

    # Routes
    @app.route('/')
    def home():
        return jsonify({
            "message": "FindMe- Missing Persons Reporting API",
            "description": "Community-driven platform for reporting and tracking missing persons",
            "endpoints": {
                "health": "/api/health",
                "authentication": "/api/auth/register & /api/auth/login",
                "missing_persons": "/api/missing",
                "specific_person": "/api/missing/<id>"
            }
        })

    @app.route('/api/health')
    def health_check():
        # Test database connection
        try:
            db.session.execute(db.text('SELECT 1'))
            db_status = "connected"
        except Exception as e:
            db_status = f"error: {str(e)}"

        return jsonify({
            "status": "healthy",
            "database": db_status,
            "authentication": "JWT system active",
            "message": "API is running with authentication"
        })

    return app

if __name__ == '__main__':
    app = create_app('development')
    print("Starting FindMe server with authentication...")
    app.run(debug=True, port=5000)