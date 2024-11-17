""" from fastapi import FastAPI, HTTPException
from models import Todo

app = FastAPI()

#In-memory storage
todos = []

@app.post("/todos/", status_code=201)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos/")
def read_todos():
    return todos

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Tpdo not found")

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
 """

from fastapi import FastAPI
from app.routers import todos
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(todos.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI To-Do List!"}
