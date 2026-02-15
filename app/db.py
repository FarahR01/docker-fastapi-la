import os
import sqlite3
from typing import List, Dict, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "tasks.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_conn()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


def get_tasks() -> List[Dict]:
    conn = get_conn()
    cur = conn.execute("SELECT id, title, completed FROM tasks ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": row["id"], "title": row["title"], "completed": bool(row["completed"]) }
        for row in rows
    ]


def get_task(task_id: int) -> Optional[Dict]:
    conn = get_conn()
    cur = conn.execute("SELECT id, title, completed FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    return {"id": row["id"], "title": row["title"], "completed": bool(row["completed"]) }


def create_task(title: str) -> Dict:
    conn = get_conn()
    cur = conn.execute("INSERT INTO tasks (title, completed) VALUES (?, 0)", (title,))
    conn.commit()
    task_id = cur.lastrowid
    conn.close()
    return {"id": task_id, "title": title, "completed": False}


def update_task(task_id: int, title: str = None, completed: bool = None) -> Optional[Dict]:
    conn = get_conn()
    existing = get_task(task_id)
    if not existing:
        return None
    new_title = title if title is not None else existing["title"]
    new_completed = int(completed) if completed is not None else int(existing["completed"])
    conn.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (new_title, new_completed, task_id),
    )
    conn.commit()
    conn.close()
    return {"id": task_id, "title": new_title, "completed": bool(new_completed)}


def delete_task(task_id: int) -> bool:
    conn = get_conn()
    cur = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    affected = cur.rowcount
    conn.close()
    return affected > 0
