"""Simple SMTP email notifications."""

from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", 25))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


def send_confirmation(to_address: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = SMTP_USERNAME or "noreply@example.com"
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        if SMTP_USERNAME and SMTP_PASSWORD:
            smtp.starttls()
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)


__all__ = ["send_confirmation"]
