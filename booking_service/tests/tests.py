import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from main import app

# Создаем тестовую базу данных 
SQLALCHEMY_DATABASE_URL = ""
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)



def test_create_user():
    response = client.post("/api/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"


def test_get_user():
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"


def test_create_duplicate_user():
    response = client.post("/api/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_delete_user():
    response = client.delete("/api/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"


def test_create_booking():
    client.post("/api/users/", json={"name": "Alice", "email": "alice@example.com"})
    
    response = client.post("/bookings/", json={
        "start_time": "2025-02-10T10:00:00",
        "end_time": "2025-02-10T12:00:00",
        "user_id": 2
    })
    assert response.status_code == 200
    assert response.json()["user_id"] == 2


def test_create_booking_with_invalid_time():
    response = client.post("/api/bookings/", json={
        "start_time": "2025-02-10T14:00:00",
        "end_time": "2025-02-10T13:00:00",
        "user_id": 2
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid time range"


def test_get_bookings():
    response = client.get("/api/bookings/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_delete_booking():
    response = client.delete("/api/bookings/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Booking deleted successfully"