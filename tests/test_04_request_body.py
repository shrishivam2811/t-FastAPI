"""
Tests for the Request Body example
"""

from fastapi.testclient import TestClient
from examples.basic.request_body import app

client = TestClient(app)


def test_create_item():
    """Test creating an item"""
    item_data = {
        "name": "Laptop",
        "description": "A high-performance laptop",
        "price": 999.99,
        "tax": 99.99
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Item created successfully"
    assert data["item"]["name"] == "Laptop"
    assert "price_with_tax" in data["item"]


def test_create_item_without_tax():
    """Test creating an item without tax"""
    item_data = {
        "name": "Mouse",
        "price": 29.99
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == "Mouse"


def test_create_item_invalid():
    """Test creating an item with invalid data"""
    item_data = {
        "name": "Invalid",
        "price": -10  # Invalid: price must be > 0
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422


def test_update_item():
    """Test updating an item"""
    item_data = {
        "name": "Updated Laptop",
        "price": 1099.99
    }
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert data["item"]["name"] == "Updated Laptop"


def test_create_user():
    """Test creating a user"""
    user_data = {
        "username": "johndoe",
        "email": "john@example.com",
        "full_name": "John Doe"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["user"]["username"] == "johndoe"


def test_create_product():
    """Test creating a product"""
    product_data = {
        "name": "Widget",
        "price": 19.99,
        "quantity": 10,
        "tags": ["electronics", "gadget"]
    }
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert data["product"]["name"] == "Widget"
    assert abs(data["total_value"] - 199.9) < 0.01  # Handle floating point precision
