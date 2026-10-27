from pydantic import BaseModel


class ToDoCreate(BaseModel):
    title: str
    done: bool

class ToDo(BaseModel):
    id: int
    title: str
    done: bool

toDos: list[ToDo]
nextId = 1