"""Logging utilities using GitPython."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from git import Repo
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
LOG_REPO_PATH = Path(os.getenv("LOG_REPO_PATH", "codex"))


def log_application(company: str, job_title: str) -> Optional[str]:
    """Commit an application log entry to the Git repository."""
    LOG_REPO_PATH.mkdir(exist_ok=True)
    repo = Repo.init(LOG_REPO_PATH)

    log_file = LOG_REPO_PATH / "applications.log"
    with open(log_file, "a", encoding="utf-8") as fh:
        fh.write(f"{company} - {job_title}\n")

    repo.index.add([str(log_file)])
    repo.index.commit(f"Add application for {company} - {job_title}")

    return repo.head.commit.hexsha


__all__ = ["log_application"]
