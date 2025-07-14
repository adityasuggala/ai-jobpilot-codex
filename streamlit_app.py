"""Streamlit web UI for the job pilot."""

from __future__ import annotations

import streamlit as st

from app.tailor import tailor_resume
from app.apply import apply_to_job
from app.database import add_application, list_applications, init_db
from app.emailer import send_confirmation
from app.codex_logger import log_application


init_db()

st.title("AI Job Pilot")

resume_text = st.text_area("Resume")
job_description = st.text_area("Job Description")

if st.button("Tailor Resume"):
    if resume_text and job_description:
        tailored = tailor_resume(resume_text, job_description)
        st.text_area("Tailored Resume", value=tailored, height=300)

job_url = st.text_input("Job URL")
resume_path = st.text_input("Resume file path", value="resume.pdf")
email = st.text_input("Your email")

if st.button("Apply"):
    if job_url and resume_path:
        apply_to_job(job_url, resume_path)
        add_application(job_url, job_description[:50])
        log_application(job_url, job_description[:50])
        if email:
            send_confirmation(email, "Application Submitted", f"You applied to {job_url}")
        st.success("Application logged")

st.header("Previous Applications")
for row in list_applications():
    st.write(row)
