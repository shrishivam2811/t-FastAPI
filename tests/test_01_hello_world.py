"""
Tests for the Hello World example
"""

from fastapi.testclient import TestClient
from examples.basic.hello_world import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from FastAPI!"}


def test_greet_name():
    """Test the greeting endpoint with a name"""
    response = client.get("/hello/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John!"}


def test_get_info():
    """Test the info endpoint"""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert data["framework"] == "FastAPI"
    assert data["version"] == "1.0.0"
