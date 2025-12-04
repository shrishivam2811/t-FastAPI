"""
Tests for the Query Parameters example
"""

from fastapi.testclient import TestClient
from examples.basic.query_parameters import app

client = TestClient(app)


def test_read_items_default():
    """Test reading items with default parameters"""
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert data["skip"] == 0
    assert data["limit"] == 10


def test_read_items_custom():
    """Test reading items with custom parameters"""
    response = client.get("/items/?skip=5&limit=20")
    assert response.status_code == 200
    data = response.json()
    assert data["skip"] == 5
    assert data["limit"] == 20


def test_search_items_no_query():
    """Test search without query"""
    response = client.get("/search/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_search_items_with_query():
    """Test search with query"""
    response = client.get("/search/?q=laptop")
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "laptop"


def test_filter_products():
    """Test filtering products"""
    response = client.get("/products/?category=electronics&min_price=100")
    assert response.status_code == 200
    data = response.json()
    assert data["filters_applied"]["category"] == "electronics"
    assert data["filters_applied"]["min_price"] == 100


def test_validate_query():
    """Test query validation"""
    response = client.get("/validate/?name=John&age=30")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["age"] == 30


def test_validate_query_invalid():
    """Test query validation with invalid data"""
    response = client.get("/validate/?name=Jo&age=30")  # Name too short
    assert response.status_code == 422
