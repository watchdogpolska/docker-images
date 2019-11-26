import requests
from icalendar import Calendar
import os
import sys
import random
from jinja2 import Template
from html5print import HTMLBeautifier
import json
import datetime
from email.message import EmailMessage
from smtplib import SMTP
from urllib.parse import urlparse

ETR_WARSZAWA = "https://raw.githubusercontent.com/ad-m/etr-warszawa-ical/master/648.ics"

SUBJECT_LIST = [
    "Plany, plany, plany (na przyszły tydzień)" "Ciekawy tydzień Stowarzyszenia",
    "Tygodniowy plan pracy Stowarzyszenia",
    "Tydzień Stowarzyszenia",
    "Okazje od Stowarzyszenia w tym tygodniu"
    "Okazje dla członków w tym tygodniu"
    "Okazje dla członkiń w tym tygodniu",
]


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
                "start_format": start.strftime("%Y-%m-%d"),
                "end_format": end.strftime("%Y-%m-%d"),
                "days": (end - start).days,
                "summary": str(v["SUMMARY"]),
                "description": str(v["DESCRIPTION"]),
            }
        )
    return sorted(events, key=lambda x: x["start"])


def main():
    etr_events = parse_ical(requests.get(ETR_WARSZAWA).content)
    etr_events = [events for events in etr_events if "[J]" in events["summary"]]

    wd_events = parse_ical(requests.get(os.environ["CALENDAR_URL"]).content)

    template = Template(open("template.htm", "r").read())
    html = template.render(events=wd_events, etr_events=etr_events)
    pretty_html = HTMLBeautifier.beautify(html, 4)

    if "SMTP_URL" not in os.environ:
        print("Skipping sending email", file=sys.stderr)
        print(pretty_html)
        return
    config = urlparse(os.environ["SMTP_URL"])
    email = EmailMessage()
    email["Subject"] = random.choice(SUBJECT_LIST)
    email["From"] = os.environ["SMTP_FROM"]
    email["To"] = os.environ["SMTP_TO"]
    email.set_content(pretty_html, subtype="html")

    with SMTP(config.hostname, config.port or 587) as s:
        s.login(config.username, config.password)
        s.send_message(email)


if __name__ == "__main__":
    main()
