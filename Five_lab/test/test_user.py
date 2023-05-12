from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# def test_create_user():
#     response = client.post( 
#         "/users/",
#         json={
#             "email": "test@ugrasu.ru",
#             "password": "test123", 
#             "user_name": "tester1", 
#             "passport": 123456, 
#             "address": "test sity", 
#             "phone": 7951}
#         )
    
#     assert response.status_code == 200, response.text
#     data = response.json() 
#     assert data["email"] == "test@ugrasu.ru"

def test_create_exist_user():
    response = client.post( 
        "/users/",
        json={
            "email": "test@ugrasu.ru",
            "password": "test123", 
            "user_name": "tester1", 
            "passport": 123456, 
            "address": "test sity", 
            "phone": 79519}
        )

    assert response.status_code == 400, response.text
    data = response.json() 
    assert data["detail"] == "Email already registered"

def test_create_exist_user_number():
    response = client.post( 
        "/users/",
        json={
            "email": "test1@ugrasu.ru",
            "password": "test123", 
            "user_name": "tester2", 
            "passport": 654321, 
            "address": "test sity", 
            "phone": 79519}
        )
        
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Номер телефона уже используется"


def test_create_exist_user_passport():
    response = client.post( 
        "/users/",
        json={
            "email": "test2@ugrasu.ru",
            "password": "test123", 
            "user_name": "tester3", 
            "passport": 123456, 
            "address": "test sity", 
            "phone": 795198160}
        )
        
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Номер пасспорта уже используется"


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["email"] == "test@ugrasu.ru"

def test_read_user_by_id():
    response = client.get(f"/user/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "test@ugrasu.ru"


def test_user_not_found():
    response = client.get(f"/user/41")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"
