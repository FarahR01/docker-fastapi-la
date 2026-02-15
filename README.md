# Docker FastAPI Lab 🐳⚡

A minimal yet extensible FastAPI application designed as a **learning playground for Docker and containerization concepts**.

This project is intentionally simple at first, but structured in a way that allows progressive enhancements such as:
- Docker & Dockerfile optimization
- Multi-stage builds
- Docker Compose
- Databases (MySQL / PostgreSQL)
- Environment variables
- CI/CD pipelines
- Production vs development setups

---

## 🎯 Purpose

This repository is used to:
- Understand how Docker images and layers work
- Practice writing efficient Dockerfiles
- Learn how FastAPI apps are containerized
- Experiment safely by creating and deleting containers, volumes, and networks

---

## 🚀 Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Docker
- Docker Desktop

---

## 📁 Project Structure
```
task-tracker/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ db.py
│  ├─ schemas.py
│  └─ static/
│     ├─ index.html
│     ├─ app.css
│     └─ app.js
├─ requirements.txt
├─ Dockerfile
└─ README.md
```

## 🧭 Quick start

1. Create and activate a virtualenv (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies and run the app:

```powershell
pip install -r requirements.txt
python -m uvicorn app:app --reload
# or
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/ for the UI and http://127.0.0.1:8000/docs for API docs.

## ♻️ Persistence

This project uses a simple SQLite DB file `app/tasks.db` created automatically on startup.

## 🧩 Next steps

- Add tests
- Add CI pipeline
- Add migrations (alembic)
- Improve UI (SPA, auth)

