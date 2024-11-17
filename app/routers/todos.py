from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import Todo, TodoCreate
from app.crud import create_todo, get_todos, get_todo_by_id, update_todo, delete_todo

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=Todo, status_code=201)
def add_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)

@router.get("/", response_model=list[Todo])
def list_todos(db: Session = Depends(get_db)):
    return get_todos(db)

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo_by_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=Todo)
def update_existing_todo(todo_id: int, updated_todo: TodoCreate, db: Session = Depends(get_db)):
    todo = update_todo(db, todo_id, updated_todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/{todo_id}", response_model=dict)
def remove_existing_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = delete_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
