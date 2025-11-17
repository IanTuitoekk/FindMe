import pytest
from datetime import datetime, timedelta
from flask import Flask

from app import create_app
from models.missing_person import db
from flask_jwt_extended import create_access_token


@pytest.fixture(scope="function")
def app():
    app = create_app('development')
    # Override config for testing
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app: Flask):
    return app.test_client()


@pytest.fixture()
def auth_header(app: Flask):
    # Ensure JWTManager is initialized in the app factory
    with app.app_context():
        token = create_access_token(identity="test-user")
    return {"Authorization": f"Bearer {token}"}


def build_payload(**overrides):
    base = {
        "full_name": "John Doe",
        "age": 30,
        "gender": "Male",
        "height": "180 cm",
        "weight": "75 kg",
        "hair_color": "Brown",
        "eye_color": "Blue",
        "distinguishing_features": "Scar on left cheek",
        "last_seen_date": datetime.utcnow().isoformat(),
        "last_seen_location": "Central Park, NY",
        "last_seen_wearing": "Blue jacket",
        "contact_name": "Jane Doe",
        "contact_phone": "+1234567890",
        "contact_email": "jane@example.com",
        "status": "missing",
        "case_number": f"CASE-{int(datetime.utcnow().timestamp()*1000000)}",
        "additional_info": "N/A",
    }
    base.update(overrides)
    return base


# 1) Should create a missing person with valid data

def test_create_missing_person_success(client):
    payload = build_payload()

    res = client.post("/api/missing-persons", json=payload)

    assert res.status_code == 201
    body = res.get_json()
    assert body["success"] is True
    assert body["data"]["full_name"] == payload["full_name"]
    assert body["data"]["case_number"] == payload["case_number"]


# 2) Should return validation errors when required fields are missing

def test_create_missing_person_validation_error(client):
    payload = build_payload()
    # Remove required fields
    del payload["full_name"]
    del payload["age"]

    res = client.post("/api/missing-persons", json=payload)

    assert res.status_code == 400
    body = res.get_json()
    assert body["success"] is False
    assert "full_name" in body["error"]
    assert "age" in body["error"]


# 3) Should list all missing persons and include the created one

def test_list_missing_persons_includes_created(client):
    payload = build_payload()
    res_create = client.post("/api/missing-persons", json=payload)
    assert res_create.status_code == 201

    res = client.get("/api/missing-persons")
    assert res.status_code == 200
    body = res.get_json()
    assert body["success"] is True
    assert isinstance(body["data"], list)
    assert any(item["case_number"] == payload["case_number"] for item in body["data"])


# 4) Should get a missing person by ID

def test_get_missing_person_by_id(client):
    payload = build_payload()
    res_create = client.post("/api/missing-persons", json=payload)
    person_id = res_create.get_json()["data"]["id"]

    res = client.get(f"/api/missing-persons/{person_id}")
    assert res.status_code == 200
    body = res.get_json()
    assert body["success"] is True
    assert body["data"]["id"] == person_id
    # date in ISO format
    assert "T" in body["data"]["last_seen_date"]


# 5) Should return 404 when getting a non-existent person

def test_get_missing_person_not_found(client):
    res = client.get("/api/missing-persons/999999")
    assert res.status_code == 404
    body = res.get_json()
    assert body["success"] is False


# 6) Should require JWT for update/delete when no token is provided

def test_protected_endpoints_require_jwt(client):
    res_put = client.put("/api/missing-persons/1", json={"status": "found"})
    assert res_put.status_code in (401, 422)  # Depending on JWT config, could be 401 Unauthorized or 422 Missing header

    res_del = client.delete("/api/missing-persons/1")
    assert res_del.status_code in (401, 422)


# 7) Should update allowed fields with valid data

def test_update_missing_person_success(client, auth_header):
    create = client.post("/api/missing-persons", json=build_payload())
    person_id = create.get_json()["data"]["id"]

    res = client.put(
        f"/api/missing-persons/{person_id}",
        json={"status": "found", "full_name": "Johnathan Doe"},
        headers=auth_header,
    )

    assert res.status_code == 200
    body = res.get_json()
    assert body["success"] is True
    assert body["data"]["status"] == "found"
    assert body["data"]["full_name"] == "Johnathan Doe"


# 8) Should validate updates and return 400 for invalid data

def test_update_missing_person_validation_error(client, auth_header):
    create = client.post("/api/missing-persons", json=build_payload())
    person_id = create.get_json()["data"]["id"]

    # Invalid age and gender value
    res = client.put(
        f"/api/missing-persons/{person_id}",
        json={"age": -5, "gender": "Unknown"},
        headers=auth_header,
    )

    assert res.status_code == 400
    body = res.get_json()
    assert body["success"] is False
    assert "age" in body["error"] or "gender" in body["error"]


# 9) Should delete a missing person

def test_delete_missing_person_success(client, auth_header):
    create = client.post("/api/missing-persons", json=build_payload())
    person_id = create.get_json()["data"]["id"]

    res = client.delete(f"/api/missing-persons/{person_id}", headers=auth_header)
    assert res.status_code == 200
    body = res.get_json()
    assert body["success"] is True

    # Confirm it no longer exists
    res_get = client.get(f"/api/missing-persons/{person_id}")
    assert res_get.status_code == 404


# 10) Should return 404 when deleting a non-existent person

def test_delete_missing_person_not_found(client, auth_header):
    res = client.delete("/api/missing-persons/999999", headers=auth_header)
    assert res.status_code == 404
    body = res.get_json()
    assert body["success"] is False
