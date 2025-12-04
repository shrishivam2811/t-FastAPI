"""
Dependencies Example

Learn about FastAPI's powerful dependency injection system.
Run with: uvicorn examples.intermediate.dependencies:app --reload
"""

from fastapi import FastAPI, Depends, HTTPException, status, Header
from typing import Optional

app = FastAPI(title="Dependencies API")


# Simple dependency functions
def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    """
    Common query parameters used across multiple endpoints.
    """
    return {"q": q, "skip": skip, "limit": limit}


def verify_token(x_token: str = Header(...)):
    """
    Verify an authentication token from headers.
    """
    if x_token != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
    return x_token


def verify_key(x_key: str = Header(...)):
    """
    Verify an API key from headers.
    """
    if x_key != "api-key-123":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )
    return x_key


# Class-based dependency
class QueryParams:
    """
    Class-based dependency for query parameters.
    """
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    """
    Get items using common query parameters.
    
    Args:
        commons: Common parameters injected via dependency
    """
    return {
        "message": "Items retrieved",
        "params": commons,
        "items": [f"Item {i}" for i in range(commons["skip"], commons["skip"] + commons["limit"])]
    }


@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    """
    Get users using common query parameters.
    
    Args:
        commons: Common parameters injected via dependency
    """
    return {
        "message": "Users retrieved",
        "params": commons,
        "users": [f"User {i}" for i in range(commons["skip"], commons["skip"] + commons["limit"])]
    }


@app.get("/protected/items/")
def read_protected_items(
    commons: dict = Depends(common_parameters),
    token: str = Depends(verify_token)
):
    """
    Get items from a protected endpoint (requires authentication).
    
    Args:
        commons: Common parameters injected via dependency
        token: Verified token from header
    """
    return {
        "message": "Protected items retrieved",
        "params": commons,
        "token": token,
        "items": ["Protected Item 1", "Protected Item 2"]
    }


@app.get("/secure/data/")
def read_secure_data(
    token: str = Depends(verify_token),
    key: str = Depends(verify_key)
):
    """
    Get data from a secure endpoint (requires both token and API key).
    
    Args:
        token: Verified token from header
        key: Verified API key from header
    """
    return {
        "message": "Secure data retrieved",
        "token": token,
        "key": key,
        "data": "Very secure data"
    }


@app.get("/products/")
def read_products(params: QueryParams = Depends()):
    """
    Get products using class-based dependency.
    
    Args:
        params: Query parameters injected via class-based dependency
    """
    return {
        "message": "Products retrieved",
        "query": params.q,
        "skip": params.skip,
        "limit": params.limit,
        "products": [f"Product {i}" for i in range(params.skip, params.skip + params.limit)]
    }


# Dependency with sub-dependencies
def get_current_user(token: str = Depends(verify_token)):
    """
    Get current user based on token. This dependency uses another dependency.
    """
    # In a real app, you would decode the token and fetch the user from database
    return {"user_id": 1, "username": "testuser", "token": token}


@app.get("/me/")
def read_user_me(current_user: dict = Depends(get_current_user)):
    """
    Get current user information. Uses nested dependencies.
    
    Args:
        current_user: Current user injected via dependency with sub-dependencies
    """
    return current_user
