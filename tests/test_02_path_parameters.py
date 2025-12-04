"""
Tests for the Path Parameters example
"""

from fastapi.testclient import TestClient
from examples.basic.path_parameters import app

client = TestClient(app)


def test_read_item():
    """Test reading an item with integer ID"""
    response = client.get("/items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert data["type"] == "integer"


def test_read_item_invalid():
    """Test reading an item with invalid ID"""
    response = client.get("/items/not-a-number")
    assert response.status_code == 422  # Validation error


def test_read_user():
    """Test reading a user"""
    response = client.get("/users/john123")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "john123"
    assert data["type"] == "string"


def test_get_model():
    """Test getting a model with enum validation"""
    response = client.get("/models/alexnet")
    assert response.status_code == 200
    data = response.json()
    assert data["model_name"] == "alexnet"
    assert "message" in data


def test_get_model_invalid():
    """Test getting a model with invalid name"""
    response = client.get("/models/invalid-model")
    assert response.status_code == 422  # Validation error


def test_read_file():
    """Test reading a file path"""
    response = client.get("/files/home/user/documents/file.txt")
    assert response.status_code == 200
    data = response.json()
    assert data["file_path"] == "home/user/documents/file.txt"
