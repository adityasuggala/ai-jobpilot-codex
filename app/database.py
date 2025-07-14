"""Tiny SQLite database for tracking job applications."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable, Tuple

DB_PATH = Path("applications.db")


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT,
                job_title TEXT,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def add_application(company: str, job_title: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO applications (company, job_title) VALUES (?, ?)",
            (company, job_title),
        )
        conn.commit()


def list_applications() -> Iterable[Tuple[int, str, str, str]]:
    with sqlite3.connect(DB_PATH) as conn:
        return list(conn.execute("SELECT * FROM applications"))


__all__ = ["init_db", "add_application", "list_applications"]
