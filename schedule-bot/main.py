import requests
from icalendar import Calendar
import os
from jinja2 import Template
from html5print import HTMLBeautifier
import json
import datetime
from email.message import EmailMessage
from smtplib import SMTP
from urllib.parse import urlparse

def to_date(x):
    if isinstance(x, datetime.datetime):
        return x.date()
    return x
def main():

    events = []
    with requests.get(os.environ['CALENDAR_URL']) as r:
        cal = Calendar.from_ical(r.content)
        maximum_time = datetime.date.today() + datetime.timedelta(days=7)
        minimum_time = datetime.date.today()
        for v in cal.subcomponents:
            start = to_date((v['DTSTART'] or v['DTSTAMP']).dt)
            end = to_date((v['DTEND'] or v['DTSTAMP']).dt)
            if start < minimum_time: # to early
                continue
            if start > maximum_time: # to late
                continue
            if end < start: # invalid time
                continue
            events.append({
                "start": start,
                "end": end,
                "start_format": start.strftime("%Y-%m-%d"),
                "end_format": end.strftime("%Y-%m-%d"),
                "days": (end - start).days,
                "summary": str(v['SUMMARY']),
                "description": str(v['DESCRIPTION']),
                "category": str(v['CATEGORIES'].cats[0])
            })
        events = sorted(events, key=lambda x: x['start'])
    template = Template(open('template.htm', 'r').read())
    html = template.render(name='John Doe', events=events)
    pretty_html = HTMLBeautifier.beautify(html, 4)
    print(pretty_html)

    if 'SMTP_URL' not in os.environ:
        print("Skipping sending email")
        return
    config = urlparse(os.environ['SMTP_URL'])
    email = EmailMessage()
    email['Subject'] = 'Plany, plany, plany (na przyszły tydzień)'
    email['From'] = os.environ['SMTP_FROM']
    email['To'] = os.environ['SMTP_TO']
    email.set_content(pretty_html, subtype='html')

    with SMTP(config.hostname, config.port or 587) as s:
        s.login(config.username, config.password)
        s.send_message(email)
if __name__== "__main__" :
    main()