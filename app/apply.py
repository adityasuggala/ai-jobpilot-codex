"""Automated job application via Selenium."""

from __future__ import annotations

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def apply_to_job(job_url: str, resume_path: str) -> None:
    """Open a browser and attempt to upload the resume to the given job URL."""
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(job_url)
        # Placeholder: logic to locate buttons/fields for Indeed would go here
        time.sleep(2)
        print(f"Would upload {resume_path} to {job_url}")
    finally:
        driver.quit()


__all__ = ["apply_to_job"]
