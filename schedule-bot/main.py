import os
import sys
import json
import datetime
from time import mktime

from ical import fetch_filtered_events
from mailer import send_mail, render_html, random_email_subject
from feed import parse_feed

ETR_WARSZAWA_URL = "https://raw.githubusercontent.com/ad-m/etr-warszawa-ical/master/648.ics"


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

    it_days = (datetime.date(2020, 7, 1) - datetime.datetime.now().date()).days

    html = render_html(wd_events, etr_events, feed_events, it_days)
    subject = random_email_subject()

    return send_mail(subject, html)


if __name__ == "__main__":
    main()
