# FastAPI Tutorial Repository

Welcome to the FastAPI Tutorial Repository! This repository contains comprehensive examples and tutorials for learning FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## 📚 What is FastAPI?

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It's built on top of Starlette for the web parts and Pydantic for the data parts.

### Key Features:
- **Fast**: Very high performance, on par with NodeJS and Go
- **Fast to code**: Increase the speed to develop features by about 200% to 300%
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors
- **Intuitive**: Great editor support with completion everywhere
- **Easy**: Designed to be easy to use and learn
- **Short**: Minimize code duplication
- **Robust**: Get production-ready code with automatic interactive documentation
- **Standards-based**: Based on the open standards for APIs: OpenAPI and JSON Schema

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/shrishivam2811/t-FastAPI.git
cd t-FastAPI
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Tutorial Structure

This repository is organized into progressive examples, from basic to advanced:

### 1. Basic Examples (`examples/basic/`)
- Simple "Hello World" API
- Path parameters
- Query parameters
- Request body with Pydantic models

### 2. Intermediate Examples (`examples/intermediate/`)
- Response models
- Status codes and headers
- Form data and file uploads
- Dependencies and dependency injection
- Error handling

### 3. Advanced Examples (`examples/advanced/`)
- Database integration with SQLAlchemy
- Authentication and authorization (JWT tokens)
- Background tasks
- WebSockets
- Testing with pytest

## 🏃 Running the Examples

Each example can be run independently. Navigate to the example directory and run:

```bash
# For the basic hello world example
uvicorn examples.basic.hello_world:app --reload

# For any other example
uvicorn examples.<folder>.<file_name>:app --reload
```

The `--reload` flag enables auto-reload on code changes (useful for development).

### Accessing the API Documentation

Once the server is running, you can access:
- **Swagger UI** (Interactive API docs): http://127.0.0.1:8000/docs
- **ReDoc** (Alternative API docs): http://127.0.0.1:8000/redoc
- **OpenAPI Schema**: http://127.0.0.1:8000/openapi.json

## 🧪 Running Tests

To run the test suite:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=examples --cov-report=html
```

## 📝 Examples Overview

### Basic Examples

#### 1. Hello World
A simple API that returns a greeting message.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

#### 2. Path Parameters
Learn how to capture values from the URL path.

#### 3. Query Parameters
Learn how to handle query parameters in your API.

#### 4. Request Body
Learn how to accept JSON data in request bodies using Pydantic models.

### Intermediate Examples

#### 5. Response Models
Learn how to define response models and validate output data.

#### 6. Form Data and File Uploads
Learn how to handle form data and file uploads.

#### 7. Dependencies
Learn about FastAPI's powerful dependency injection system.

### Advanced Examples

#### 8. Database Integration
Learn how to integrate a database using SQLAlchemy.

#### 9. Authentication
Learn how to implement JWT-based authentication.

#### 10. Testing
Learn how to write tests for your FastAPI applications.

## 📚 Learning Resources

### Official Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Starlette Documentation](https://www.starlette.io/)

### Additional Resources
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi)
- [FastAPI Tutorial Video Series](https://www.youtube.com/results?search_query=fastapi+tutorial)

## 🤝 Contributing

Contributions are welcome! If you'd like to add more examples or improve existing ones:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-example`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing example'`)
5. Push to the branch (`git push origin feature/amazing-example`)
6. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Thanks to [Sebastián Ramírez](https://github.com/tiangolo) for creating FastAPI
- Thanks to the FastAPI community for their excellent documentation and support

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

---

Happy Learning! 🎉