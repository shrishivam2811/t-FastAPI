"""
Request Body Example

Learn how to work with request bodies using Pydantic models.
Run with: uvicorn examples.basic.request_body:app --reload
"""

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI(title="Request Body API")


class Item(BaseModel):
    """Pydantic model for an Item"""
    name: str = Field(..., min_length=1, max_length=100, description="Name of the item")
    description: Optional[str] = Field(None, max_length=500, description="Optional description")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    tax: Optional[float] = Field(None, ge=0, description="Optional tax (must be non-negative)")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "A high-performance laptop",
                "price": 999.99,
                "tax": 99.99
            }
        }


class User(BaseModel):
    """Pydantic model for a User"""
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., description="User's email address")
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=120)


class Product(BaseModel):
    """Pydantic model for a Product with nested models"""
    name: str
    price: float
    quantity: int = Field(..., ge=0)
    tags: list[str] = []


@app.post("/items/")
def create_item(item: Item):
    """
    Create a new item.
    
    Args:
        item: The item to create
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return {
        "message": "Item created successfully",
        "item": item_dict
    }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Update an existing item.
    
    Args:
        item_id: The ID of the item to update
        item: The updated item data
    """
    return {
        "message": f"Item {item_id} updated successfully",
        "item_id": item_id,
        "item": item.dict()
    }


@app.post("/users/")
def create_user(user: User):
    """
    Create a new user.
    
    Args:
        user: The user to create
    """
    return {
        "message": "User created successfully",
        "user": user.dict()
    }


@app.post("/products/")
def create_product(product: Product):
    """
    Create a new product.
    
    Args:
        product: The product to create
    """
    return {
        "message": "Product created successfully",
        "product": product.dict(),
        "total_value": product.price * product.quantity
    }


@app.put("/items/{item_id}/details")
def update_item_details(
    item_id: int,
    item: Item,
    q: Optional[str] = None,
    importance: int = Body(..., ge=1, le=5)
):
    """
    Update item with a combination of path, query, and body parameters.
    
    Args:
        item_id: The ID of the item to update
        item: The updated item data
        q: Optional query parameter
        importance: Importance level (1-5) sent in the body
    """
    result = {
        "item_id": item_id,
        "item": item.dict(),
        "importance": importance
    }
    if q:
        result.update({"q": q})
    return result
