import os
import sys

from urllib.parse import urlparse
from email.message import EmailMessage
from smtplib import SMTP


def send_mail(subject, html):
    if "SMTP_URL" not in os.environ:
        print("Skipping sending email", file=sys.stderr)
        print(html)
        return
    config = urlparse(os.environ["SMTP_URL"])
    email = EmailMessage()
    email["Subject"] = subject
    email["From"] = os.environ["SMTP_FROM"]
    email["To"] = os.environ["SMTP_TO"]
    email.set_content(html, subtype="html")

    with SMTP(config.hostname, config.port or 587) as s:
        s.login(config.username, config.password)
        s.send_message(email)
