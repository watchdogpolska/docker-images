import os
import sys
import random
import json
import datetime
from time import mktime

from jinja2 import Template, Environment, FileSystemLoader
from html5print import HTMLBeautifier

from dateutils import datetimeformat, structformat, struct_to_datetime
from ical import fetch_filtered_events
from mailer import send_mail
from feed import parse_feed

ETR_WARSZAWA_URL = "https://raw.githubusercontent.com/ad-m/etr-warszawa-ical/master/648.ics"

SUBJECT_LIST = [
    "Plany, plany, plany (na przyszły tydzień)",
    "Ciekawy tydzień Stowarzyszenia",
    "Tygodniowy plan pracy Stowarzyszenia",
    "Tydzień Stowarzyszenia",
    "Okazje od Stowarzyszenia w tym tygodniu",
    "Okazje dla członków w tym tygodniu",
    "Okazje dla członkiń w tym tygodniu",
]

dir_path = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(dir_path))
env.filters["datetimeformat"] = datetimeformat
env.filters["structformat"] = structformat


def main():
    etr_events = fetch_filtered_events(ETR_WARSZAWA_URL)
    etr_events = [
        events for events in etr_events if "[J]" in events["summary"]]

    wd_events = (
        fetch_filtered_events(os.environ["CALENDAR_URL"])
        if "CALENDAR_URL" in os.environ
        else []
    )
    wd_events = [
        x for x in wd_events if "Nieobecności/urlopy" not in x["categories"]]

    feed_events = parse_feed("https://siecobywatelska.pl/feed/") + parse_feed(
        "https://informacjapubliczna.org/feed/"
    )
    template = env.get_template("template.htm")

    it_days = (datetime.date(2020, 7, 1) - datetime.datetime.now().date()).days

    html = template.render(
        events=wd_events, etr_events=etr_events, feed_events=feed_events,
        it_days=str(it_days)
    )
    pretty_html = HTMLBeautifier.beautify(html, 4)
    subject = random.choice(SUBJECT_LIST)
    return send_mail(subject, pretty_html)


if __name__ == "__main__":
    main()
