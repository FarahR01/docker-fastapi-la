from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List

from . import db
from .schemas import TaskIn, Task

app = FastAPI()

# Serve static assets and UI
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
def startup_event():
    db.init_db()


@app.get("/", response_class=FileResponse)
def index():
    return FileResponse("app/static/index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return db.get_tasks()


@app.post("/tasks", response_model=Task)
def create_task(task: TaskIn):
    return db.create_task(task.title)


@app.put("/tasks/{task_id}/toggle", response_model=Task)
def toggle_task(task_id: int):
    existing = db.get_task(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = db.update_task(task_id, completed=not existing["completed"])
    return updated


@app.delete("/tasks/{task_id}")
def delete(task_id: int):
    ok = db.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
