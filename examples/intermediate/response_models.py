"""
Response Models Example

Learn how to use response models to validate and document API responses.
Run with: uvicorn examples.intermediate.response_models:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Response Models API")


class UserIn(BaseModel):
    """Model for user input (includes password)"""
    username: str
    email: str
    full_name: Optional[str] = None
    password: str


class UserOut(BaseModel):
    """Model for user output (excludes password)"""
    username: str
    email: str
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    """Model for user in database (includes hashed password)"""
    username: str
    email: str
    full_name: Optional[str] = None
    hashed_password: str


class Item(BaseModel):
    """Model for an item"""
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ItemResponse(BaseModel):
    """Enhanced response model for items"""
    name: str
    price: float
    price_with_tax: float
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop",
                "price": 999.99,
                "price_with_tax": 1099.99
            }
        }


# Fake database
fake_users_db = {}


def fake_password_hasher(password: str):
    """Fake password hasher"""
    return f"hashed_{password}"


@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    """
    Create a user. Returns user data without the password.
    
    Args:
        user: User input with password
    
    Returns:
        UserOut: User data without password
    """
    hashed_password = fake_password_hasher(user.password)
    user_in_db = UserInDB(**user.model_dump(), hashed_password=hashed_password)
    fake_users_db[user.username] = user_in_db
    return user_in_db


@app.get("/users/{username}", response_model=UserOut)
def read_user(username: str):
    """
    Get a user by username. Returns user data without the password.
    
    Args:
        username: The username to look up
    
    Returns:
        UserOut: User data without password
    """
    if username not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users_db[username]


@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    """
    Create an item. Returns a modified response with calculated price_with_tax.
    
    Args:
        item: The item to create
    
    Returns:
        ItemResponse: Item with calculated total price
    """
    price_with_tax = item.price + (item.tax or 0)
    return ItemResponse(
        name=item.name,
        price=item.price,
        price_with_tax=price_with_tax
    )


@app.get("/items/", response_model=list[Item])
def read_items():
    """
    Get a list of items.
    
    Returns:
        list[Item]: List of items
    """
    return [
        Item(name="Laptop", description="High-performance laptop", price=999.99, tax=99.99),
        Item(name="Mouse", description="Wireless mouse", price=29.99, tax=3.00),
        Item(name="Keyboard", description="Mechanical keyboard", price=149.99),
    ]
