from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List

from . import db
from .schemas import TaskIn, Task

app = FastAPI()

# Serve static assets and UI
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def startup_event():
    db.init_db()


@app.get("/")
def index(request: Request, color: str = "#333"):
    """Render the UI template. Pass `color` (query param) into the template.

    Example: GET /?color=%23ff0000
    """
    return templates.TemplateResponse("index.html", {"request": request, "color": color})


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
