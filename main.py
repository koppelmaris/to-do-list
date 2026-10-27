from fastapi import FastAPI
from models import ToDo, ToDoCreate

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/todos")
async def get_todos():
    pass


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    pass

@app.post("/todos")
async def create_todo(todo_create: ToDoCreate):
    pass

@app.put("/todos/{todo_id}")
async def create_todo(todo_create: ToDoCreate):
    pass

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    pass