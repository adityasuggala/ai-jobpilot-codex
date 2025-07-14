"""Resume tailoring utilities using OpenAI."""

from __future__ import annotations

import os
from typing import Any

import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def tailor_resume(resume_text: str, job_description: str) -> str:
    """Return a tailored resume using OpenAI's completion API.

    Parameters
    ----------
    resume_text: str
        The original resume text.
    job_description: str
        The target job description.
    """
    if not openai.api_key:
        raise RuntimeError("OpenAI API key not configured")

    prompt = (
        "Tailor the following resume to better match the given job description. "
        "Return the improved resume text only.\n\n"
        f"Resume:\n{resume_text}\n\n"
        f"Job Description:\n{job_description}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.get("content", "").strip()


__all__ = ["tailor_resume"]
