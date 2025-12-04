"""
Basic Hello World Example

This is the simplest FastAPI application.
Run with: uvicorn examples.basic.hello_world:app --reload
"""

from fastapi import FastAPI

app = FastAPI(
    title="Hello World API",
    description="A simple Hello World API built with FastAPI",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello World from FastAPI!"}


@app.get("/hello/{name}")
def greet_name(name: str):
    """
    Greet a specific person by name.
    
    Args:
        name: The name of the person to greet
    """
    return {"message": f"Hello {name}!"}


@app.get("/info")
def get_info():
    """
    Get information about this API.
    """
    return {
        "app_name": "Hello World API",
        "version": "1.0.0",
        "framework": "FastAPI",
        "description": "This is a simple tutorial API"
    }
