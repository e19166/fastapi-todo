# FastAPI To-Do List API

Welcome to the FastAPI To-Do List project! 🚀 This project demonstrates how to build a modern, high-performance API using [FastAPI](https://fastapi.tiangolo.com/), Python's fastest web framework. This API allows users to manage a To-Do List, with endpoints to create, read, update, and delete tasks. It integrates seamlessly with a SQLite database for persistent storage and offers interactive API documentation for easy testing.

---

## 🚀 Features

- **FastAPI-based API**: Built using FastAPI for high performance and easy-to-use Pythonic syntax.
- **CRUD operations**: Create, read, update, and delete tasks in your To-Do list.
- **Database Integration**: SQLite as the database with SQLAlchemy ORM for easy querying.
- **Interactive API Docs**: Swagger UI and ReDoc auto-generated for real-time testing of API endpoints.
- **Asynchronous Support**: FastAPI’s asynchronous support ensures optimal performance for I/O-bound tasks.

---

## ⚡ Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.7+ (FastAPI works best with Python 3.7 or newer)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Docker](https://www.docker.com/) (optional for containerization)
- [Kubernetes](https://kubernetes.io/) (optional for deployment)

### 1. Clone the Repository

```bash
git clone https://github.com/e19166/fastapi-todo.git
cd fastapi-todo
```

### 2. Create and Activate a Virtual Environment

For macOS/Linux:

```bash
    python3 -m venv venv
    source venv/bin/activate                         
```

For Windows:

```bash
    python -m venv venv
    venv\Scripts\activate
```

### 3. Install Dependencies

```bash
    pip install -r requirements.txt
```

## 📦 Running the Application Locally

### 1. Start the FastAPI App

```bash
    uvicorn app.main:app --reload
```
This will start the server at http://127.0.0.1:8000.

### 2. Access the API Documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🛠️ Project Structure

```bash
fastapi-todo/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # SQLAlchemy models
│   ├── database.py           # Database connection
│   ├── schemas.py            # Pydantic schemas
│   ├── crud.py               # CRUD operations
│   ├── routers/
│   │   ├── todos.py          # Routes for To-Do operations
│   └── utils/
│       ├── dependencies.py   # Dependency injections
├── migrations/               # Database migrations (if using Alembic)
├── tests/                    # Unit tests for the API
├── .env                      # Environment variables (e.g., DB URL)
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚡ API Endpoints

* GET /todos/: Retrieve a list of all tasks.
* GET /todos/{todo_id}: Get a specific task by ID.
* POST /todos/: Create a new task.
* PUT /todos/{todo_id}: Update an existing task by ID.
* DELETE /todos/{todo_id}: Delete a task by ID.

### Example Requests:

* Create Task: POST /todos/

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

* Update Task: PUT /todos/1

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread, butter",
  "completed": true
}
```

## 🐳 Dockerization

### 1. Build the Docker Image

```bash
docker build -t fastapi-todo .
```

### 2. Run the Docker Container

```bash
docker run -d -p 80:80 fastapi-todo
```

### 3. Push to Docker Hub

```bash
docker tag fastapi-todo your-dockerhub-username/fastapi-todo
docker push your-dockerhub-username/fastapi-todo
```

## 📦 Deployment

### Deploy with Kubernetes:

#### 1. Create Kubernetes Configurations:

* Deployment (deployment.yaml): Defines how the application will be deployed.
* Service: Exposes the app to external traffic.

#### 2. Apply Kubernetes Configurations:

```bash
kubectl apply -f deployment.yaml
```

#### 3. Verify Deployment:

```bash
kubectl get pods
kubectl get svc
```

#### 4. Port Forwarding (if no external IP):

```bash
kubectl port-forward svc/fastapi-todo-service 8080:80
```

## 🧪 Testing

### Run the tests with pytest:

```bash 
pytest tests/
```

## 🔧 Enhancements and Future Work

* Add user authentication (JWT tokens).
* Implement task due dates and priority levels.
* Introduce task categories or tags for better organization.
* Support other databases (e.g., PostgreSQL, MySQL).

## 👨‍💻 Contributing

I welcome contributions! If you have suggestions or want to fix an issue, please feel free to fork the repo and submit a pull request.

## 📑 License

This project is licensed under the MIT License - see the LICENSE file for details.

### Enjoy building your FastAPI-powered To-Do List API! 🎉



