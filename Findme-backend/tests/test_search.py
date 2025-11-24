import pytest
import json
from app import create_app, db
from models.missing_person import MissingPerson
from datetime import datetime, timedelta

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app('development')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def seed_data(app):
    """Seed test data"""
    with app.app_context():
        MissingPerson.query.delete()
        
        test_people = [
            MissingPerson(
                full_name="John Doe", age=25, gender="Male",
                last_seen_date=datetime.utcnow() - timedelta(days=2),
                last_seen_location="Nairobi CBD, Kenya",
                contact_name="Jane Doe", contact_phone="+254712345678",
                status="missing", case_number="MP001"
            ),
            MissingPerson(
                full_name="Mary Smith", age=30, gender="Female",
                last_seen_date=datetime.utcnow() - timedelta(days=5),
                last_seen_location="Mombasa, Kenya",
                contact_name="Peter Smith", contact_phone="+254723456789",
                status="missing", case_number="MP002"
            ),
            MissingPerson(
                full_name="David Johnson", age=45, gender="Male",
                last_seen_date=datetime.utcnow() - timedelta(days=10),
                last_seen_location="Kisumu, Kenya",
                contact_name="Sarah Johnson", contact_phone="+254734567890",
                status="found", case_number="MP003"
            ),
            MissingPerson(
                full_name="Alice Brown", age=22, gender="Female",
                last_seen_date=datetime.utcnow() - timedelta(days=1),
                last_seen_location="Nairobi, Westlands",
                contact_name="Bob Brown", contact_phone="+254745678901",
                status="missing", case_number="MP004"
            )
        ]
        
        db.session.add_all(test_people)
        db.session.commit()

# ==================== SEARCH TESTS ====================

def test_search_all(client, seed_data):
    """Test retrieving all missing persons"""
    response = client.get('/api/search')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['total'] == 4

def test_search_by_name(client, seed_data):
    """Test search by name"""
    response = client.get('/api/search?name=John')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['total'] >= 1
    assert 'John' in data['results'][0]['full_name']

def test_search_by_location(client, seed_data):
    """Test search by location"""
    response = client.get('/api/search?location=Nairobi')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['total'] >= 1

def test_search_by_age_range(client, seed_data):
    """Test search by age range"""
    response = client.get('/api/search?age_min=20&age_max=30')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert all(20 <= r['age'] <= 30 for r in data['results'])

def test_search_by_gender(client, seed_data):
    """Test search by gender"""
    response = client.get('/api/search?gender=Female')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert all(r['gender'] == 'Female' for r in data['results'])

def test_search_by_status(client, seed_data):
    """Test search by status"""
    response = client.get('/api/search?status=missing')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert all(r['status'] == 'missing' for r in data['results'])

def test_search_multiple_filters(client, seed_data):
    """Test multiple filters combined"""
    response = client.get('/api/search?location=Nairobi&status=missing')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['total'] >= 1

# ==================== PAGINATION TESTS ====================

def test_pagination(client, seed_data):
    """Test pagination"""
    response = client.get('/api/search?per_page=2')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['per_page'] == 2
    assert len(data['results']) <= 2
    assert 'page' in data
    assert 'total_pages' in data

# ==================== LOCATION FILTER TESTS ====================

def test_filter_by_location_endpoint(client, seed_data):
    """Test location filter endpoint"""
    response = client.get('/api/missing-persons/location/Nairobi')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['location'] == 'Nairobi'
    assert data['count'] >= 1
    assert 'results' in data

# ==================== RECENT REPORTS TESTS ====================

def test_recent_reports_default(client, seed_data):
    """Test recent reports (default 7 days)"""
    response = client.get('/api/missing-persons/recent')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['days'] == 7
    assert 'count' in data
    assert 'results' in data

def test_recent_reports_custom(client, seed_data):
    """Test recent reports with custom days"""
    response = client.get('/api/missing-persons/recent?days=30')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['days'] == 30

# ==================== STATISTICS TESTS ====================

def test_statistics(client, seed_data):
    """Test platform statistics"""
    response = client.get('/api/missing-persons/stats')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['total_cases'] == 4
    assert data['missing'] == 3
    assert data['found'] == 1
    assert 'closed' in data

def test_statistics_sum(client, seed_data):
    """Test statistics sum equals total"""
    response = client.get('/api/missing-persons/stats')
    data = json.loads(response.data)
    total = data['missing'] + data['found'] + data['closed']
    assert total == data['total_cases']