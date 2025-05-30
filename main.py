from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- model definition ---
class Todo(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

# --- in-memory "database" ---
todos_db: List[Todo] = []
next_id = 1

# --- FastAPI app ---
app = FastAPI()

# --- CRUD endpoints ---

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Todos API"}

# Create
@app.post("/todos/", response_model=Todo, status_code=201)
def create_todo(todo: Todo):
    global next_id
    todo.id = next_id
    next_id += 1
    todos_db.append(todo)
    return todo

# Read all
@app.get("/todos/", response_model=List[Todo])
def read_todos():
    return todos_db

# Read one
@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Update
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_in: Todo):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todo_in.id = todo_id
            todos_db[index] = todo_in
            return todo_in
    raise HTTPException(status_code=404, detail="Todo not found")

# Delete
@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Todo not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)