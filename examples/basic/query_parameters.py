"""
Query Parameters Example

Learn how to work with query parameters in FastAPI.
Run with: uvicorn examples.basic.query_parameters:app --reload
"""

from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(title="Query Parameters API")


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    """
    Get a list of items with pagination.
    
    Args:
        skip: Number of items to skip (default: 0)
        limit: Maximum number of items to return (default: 10)
    """
    return {
        "skip": skip,
        "limit": limit,
        "items": [f"Item {i}" for i in range(skip, skip + limit)]
    }


@app.get("/search/")
def search_items(q: Optional[str] = None, max_results: int = 10):
    """
    Search for items with an optional query string.
    
    Args:
        q: Optional search query
        max_results: Maximum number of results to return (default: 10)
    """
    if q:
        return {
            "query": q,
            "max_results": max_results,
            "results": [f"Result matching '{q}' #{i}" for i in range(1, max_results + 1)]
        }
    return {"message": "No query provided", "max_results": max_results}


@app.get("/products/")
def filter_products(
    category: Optional[str] = None,
    min_price: float = 0.0,
    max_price: Optional[float] = None,
    in_stock: bool = True
):
    """
    Filter products by various criteria.
    
    Args:
        category: Optional product category
        min_price: Minimum price (default: 0.0)
        max_price: Optional maximum price
        in_stock: Whether to show only in-stock items (default: True)
    """
    filters = {
        "category": category,
        "min_price": min_price,
        "max_price": max_price,
        "in_stock": in_stock
    }
    return {"filters_applied": filters, "sample_products": ["Product A", "Product B"]}


@app.get("/validate/")
def validate_query(
    name: str = Query(..., min_length=3, max_length=50, description="Name must be 3-50 characters"),
    age: int = Query(..., ge=0, le=120, description="Age must be between 0 and 120"),
    email: Optional[str] = Query(None, regex=r"^[\w\.-]+@[\w\.-]+\.\w+$", description="Valid email address")
):
    """
    Validate query parameters with constraints.
    
    Args:
        name: Name with length constraints
        age: Age with range constraints
        email: Optional email with regex validation
    """
    return {
        "name": name,
        "age": age,
        "email": email,
        "message": "All validations passed!"
    }
