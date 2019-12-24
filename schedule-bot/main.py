import os
import sys
import random
import json
import datetime
from email.message import EmailMessage
from smtplib import SMTP
from time import mktime

import feedparser
import requests
from urllib.parse import urlparse
from jinja2 import Template, Environment, FileSystemLoader
from html5print import HTMLBeautifier
from icalendar import Calendar

ETR_WARSZAWA = "https://raw.githubusercontent.com/ad-m/etr-warszawa-ical/master/648.ics"

SUBJECT_LIST = [
    "Plany, plany, plany (na przyszły tydzień)",
    "Ciekawy tydzień Stowarzyszenia",
    "Tygodniowy plan pracy Stowarzyszenia",
    "Tydzień Stowarzyszenia",
    "Okazje od Stowarzyszenia w tym tygodniu",
    "Okazje dla członków w tym tygodniu",
    "Okazje dla członkiń w tym tygodniu",
]


def struct_to_datetime(value):
    return datetime.datetime.fromtimestamp(mktime(value))


def to_date(x):
    if isinstance(x, datetime.datetime):
        return x.date()
    return x


def parse_ical(content, max_days=7):
    events = []
    cal = Calendar.from_ical(content)
    maximum_time = datetime.date.today() + datetime.timedelta(days=max_days)
    minimum_time = datetime.date.today()
    for v in cal.subcomponents:
        start = to_date((v["DTSTART"] or v["DTSTAMP"]).dt)
        end = to_date(
            (v.get("DTEND", v.get("DTSTAMP", v["DTSTART"] or v["DTSTAMP"]))).dt
        )
        if start < minimum_time:  # to early
            continue
        if start > maximum_time:  # to late
            continue
        if end < start:  # invalid time
            continue
        events.append(
            {
                "start": start,
                "end": end,
                "days": (end - start).days,
                "summary": str(v["SUMMARY"]),
                "description": str(v["DESCRIPTION"]),
                "categories": [str(x) for x in v["CATEGORIES"].cats]
                if "CATEGORIES" in v
                else [],
            }
        )
    return sorted(events, key=lambda x: x["start"])


def parse_feed(url, max_days=7):
    minimum_time = datetime.date.today() - datetime.timedelta(days=max_days)
    d = feedparser.parse(url)
    return [
        x
        for x in d["entries"]
        if minimum_time < struct_to_datetime(x["published_parsed"]).date()
    ]


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


def datetimeformat(value, format="%Y-%m-%d"):
    return value.strftime(format)


def structformat(value, format="%Y-%m-%d"):
    return datetimeformat(struct_to_datetime(value), format)


env = Environment(loader=FileSystemLoader("."))
env.filters["datetimeformat"] = datetimeformat
env.filters["structformat"] = structformat


def main():
    etr_events = parse_ical(requests.get(ETR_WARSZAWA).content)
    etr_events = [events for events in etr_events if "[J]" in events["summary"]]

    wd_events = (
        parse_ical(requests.get(os.environ["CALENDAR_URL"]).content)
        if "CALENDAR_URL" in os.environ
        else []
    )
    wd_events = [x for x in wd_events if "Nieobecności/urlopy" not in x["categories"]]

    feed_events = parse_feed("https://siecobywatelska.pl/feed/") + parse_feed(
        "https://informacjapubliczna.org/feed/"
    )

    template = env.get_template("template.htm")
    html = template.render(
        events=wd_events, etr_events=etr_events, feed_events=feed_events
    )
    pretty_html = HTMLBeautifier.beautify(html, 4)
    subject = random.choice(SUBJECT_LIST)
    return send_mail(subject, pretty_html)


if __name__ == "__main__":
    main()
