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

1. Prerequisites

- Install Python 3.9+ (recommend 3.10+). Verify versions:

```bash
python --version
pip --version
```

- Install Git and Docker (optional, for container builds).

2. Create & activate a virtual environment

PowerShell (Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Web server / run the app

This project is an ASGI app served with Uvicorn. From the project root run:

```bash
# development (auto-reload)
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
# alternative import path
python -m uvicorn app:app --reload
```

For production use a dedicated server process (example):

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

If running inside Docker, bind to `0.0.0.0` so the container port is reachable from the host.

5. Test the app in a browser

- Open the UI: http://127.0.0.1:8000/
- API docs: http://127.0.0.1:8000/docs
- Health check: GET http://127.0.0.1:8000/health

6. Notes

- The SQLite DB file `app/tasks.db` is created automatically by [app/db.py](app/db.py) on startup.
- Always run commands from the repository root so static file and DB paths resolve correctly.
- No environment variables are required for the basic local run.
- Consider persisting `app/tasks.db` with a host volume when running in Docker so data survives container recreation.

## ♻️ Persistence

This project uses a simple SQLite DB file `app/tasks.db` created automatically on startup.

## 🧩 Next steps

- Add tests
- Add CI pipeline
- Add migrations (alembic)
- Improve UI (SPA, auth)

