import pytest
from app import create_app
from models.user import db, User

@pytest.fixture
def app():
    """create a test application instance"""
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """create a test client for making requests"""
    return app.test_client()

def test_user_registration(client):
    """test that users can register with valid information"""
    response = client.post('/api/auth/register', json={
        'name': 'Test User',
        'email': 'test@test.com',
        'password': 'test123'
    })
    
    # verify registration was successful
    assert response.status_code == 201
    assert 'token' in response.json
    assert response.json['user_id'] == 1

def test_user_login(client):
    """test that registered users can login successfully"""
    # first register a test user in postgresql
    client.post('/api/auth/register', json={
        'name': 'Test User',
        'email': 'test@test.com',
        'password': 'test123'
    })
    
    # then attempt to login with the same credentials
    response = client.post('/api/auth/login', json={
        'email': 'test@test.com',
        'password': 'test123'
    })
    
    # verify login was successful
    assert response.status_code == 200
    assert 'token' in response.json
    assert response.json['name'] == 'Test User'