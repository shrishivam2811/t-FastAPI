"""
Form Data and File Uploads Example

Learn how to handle form data and file uploads.
Run with: uvicorn examples.intermediate.form_and_files:app --reload
"""

from fastapi import FastAPI, Form, File, UploadFile
from typing import Optional

app = FastAPI(title="Form and File Upload API")


@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    """
    Handle login form submission.
    
    Args:
        username: Username from form
        password: Password from form
    """
    return {
        "message": "Login successful",
        "username": username,
        "note": "This is a demo - password should never be returned in real apps!"
    }


@app.post("/register/")
def register(
    username: str = Form(...),
    email: str = Form(...),
    full_name: Optional[str] = Form(None),
    age: Optional[int] = Form(None)
):
    """
    Handle user registration form.
    
    Args:
        username: Username from form
        email: Email from form
        full_name: Optional full name
        age: Optional age
    """
    return {
        "message": "Registration successful",
        "user": {
            "username": username,
            "email": email,
            "full_name": full_name,
            "age": age
        }
    }


@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a single file.
    
    Args:
        file: The file to upload
    """
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "message": "File uploaded successfully"
    }


@app.post("/upload-files/")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    """
    Upload multiple files.
    
    Args:
        files: List of files to upload
    """
    file_info = []
    for file in files:
        contents = await file.read()
        file_info.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(contents)
        })
    return {
        "message": f"Uploaded {len(files)} files",
        "files": file_info
    }


@app.post("/upload-with-form/")
async def upload_file_with_metadata(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    file: UploadFile = File(...)
):
    """
    Upload a file with additional form metadata.
    
    Args:
        title: Title from form
        description: Optional description from form
        file: The file to upload
    """
    contents = await file.read()
    return {
        "title": title,
        "description": description,
        "file": {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(contents)
        },
        "message": "File and metadata uploaded successfully"
    }


@app.post("/upload-optional/")
async def upload_optional_file(file: Optional[UploadFile] = File(None)):
    """
    Upload an optional file.
    
    Args:
        file: Optional file to upload
    """
    if file is None:
        return {"message": "No file uploaded"}
    
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "message": "File uploaded successfully"
    }
