"""
Status Codes and Headers Example

Learn how to work with HTTP status codes and headers.
Run with: uvicorn examples.intermediate.status_codes:app --reload
"""

from fastapi import FastAPI, status, Response, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Status Codes API")


class Item(BaseModel):
    name: str
    description: Optional[str] = None


# Fake database
items_db = {}
item_counter = 0


@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    """
    Create an item with 201 Created status code.
    
    Args:
        item: The item to create
    """
    global item_counter
    item_counter += 1
    items_db[item_counter] = item
    return {"id": item_counter, "item": item, "message": "Item created"}


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def read_item(item_id: int):
    """
    Get an item by ID with 200 OK status code.
    
    Args:
        item_id: The ID of the item
    """
    if item_id not in items_db:
        return Response(
            content='{"detail": "Item not found"}',
            status_code=status.HTTP_404_NOT_FOUND,
            media_type="application/json"
        )
    return {"id": item_id, "item": items_db[item_id]}


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """
    Delete an item with 204 No Content status code.
    
    Args:
        item_id: The ID of the item to delete
    """
    if item_id in items_db:
        del items_db[item_id]
    return None


@app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    """
    Update an item. Returns 201 if created, 200 if updated.
    
    Args:
        item_id: The ID of the item
        item: The updated item data
    """
    if item_id in items_db:
        items_db[item_id] = item
        return {"id": item_id, "item": item, "message": "Item updated"}
    else:
        items_db[item_id] = item
        return Response(
            content=f'{{"id": {item_id}, "item": {item.json()}, "message": "Item created"}}',
            status_code=status.HTTP_201_CREATED,
            media_type="application/json"
        )


@app.get("/headers/")
def read_headers(
    user_agent: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    x_custom_header: Optional[str] = Header(None)
):
    """
    Read headers from the request.
    
    Args:
        user_agent: User-Agent header
        accept_language: Accept-Language header
        x_custom_header: Custom header (note: automatically converts X-Custom-Header)
    """
    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language,
        "X-Custom-Header": x_custom_header
    }


@app.get("/custom-headers/")
def send_custom_headers(response: Response):
    """
    Send custom headers in the response.
    """
    response.headers["X-Custom-Header"] = "Custom Value"
    response.headers["X-Another-Header"] = "Another Value"
    return {"message": "Check the response headers!"}
