"""
Path Parameters Example

Learn how to work with path parameters in FastAPI.
Run with: uvicorn examples.basic.path_parameters:app --reload
"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI(title="Path Parameters API")


class ModelName(str, Enum):
    """Enum for predefined model names"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Get an item by its ID.
    
    Args:
        item_id: The ID of the item (must be an integer)
    """
    return {"item_id": item_id, "type": "integer"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    """
    Get a user by their ID.
    
    Args:
        user_id: The ID of the user (can be any string)
    """
    return {"user_id": user_id, "type": "string"}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """
    Get information about a specific model.
    Uses an Enum to restrict allowed values.
    
    Args:
        model_name: The name of the model (must be one of the predefined values)
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    """
    Read a file path. The :path converter allows the parameter to contain slashes.
    
    Args:
        file_path: The path to the file (can contain slashes)
    """
    return {"file_path": file_path}
