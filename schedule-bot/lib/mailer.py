import os
import sys
import random

from urllib.parse import urlparse
from email.message import EmailMessage
from smtplib import SMTP
from jinja2 import Environment, FileSystemLoader
from html5print import HTMLBeautifier

from dateutils import datetimeformat, structformat


def render_html(events, etr_events, feed_events, it_days, tweets, fb_posts, fb_videos):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(dir_path))
    env.filters["datetimeformat"] = datetimeformat
    env.filters["structformat"] = structformat

    template = env.get_template("template.htm")
    html = template.render(
        events=events, etr_events=etr_events, feed_events=feed_events,
        it_days=str(it_days), tweets=tweets, fb_posts=fb_posts, fb_videos=fb_videos
    )

    pretty_html = HTMLBeautifier.beautify(html, 4)

    return pretty_html


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


def random_email_subject():
    subject_list = [
        "Plany, plany, plany (na przyszły tydzień)",
        "Ciekawy tydzień Stowarzyszenia",
        "Tygodniowy plan pracy Stowarzyszenia",
        "Tydzień Stowarzyszenia",
        "Okazje od Stowarzyszenia w tym tygodniu",
        "Okazje dla członków w tym tygodniu",
        "Okazje dla członkiń w tym tygodniu",
    ]

    return random.choice(subject_list)
