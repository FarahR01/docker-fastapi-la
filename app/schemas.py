from pydantic import BaseModel


class TaskIn(BaseModel):
    title: str


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
