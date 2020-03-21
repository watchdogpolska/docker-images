from icalendar import Calendar
import datetime
import requests

from dateutils import to_date


def get_start_date_from_ical(ical):
    return to_date((ical["DTSTART"] or ical["DTSTAMP"]).dt)


def get_end_date_from_ical(ical):
    return to_date((ical.get("DTEND", ical.get("DTSTAMP", ical["DTSTART"] or ical["DTSTAMP"]))).dt)


def fetch_ical(url):
    content = requests.get(url).content
    return Calendar.from_ical(content)


def filter_ical(ical, filter):
    filtered_components = []
    for component in ical.subcomponents:
        if filter(component):
            filtered_components.append(component)

    return filtered_components


def date_filter(component, max_days=7):
    maximum_time = datetime.date.today() + datetime.timedelta(days=max_days)
    minimum_time = datetime.date.today()
    start = get_start_date_from_ical(component)
    end = get_end_date_from_ical(component)

    if start < minimum_time:  # to early
        return False
    if start > maximum_time:  # to late
        return False
    if end < start:  # invalid time
        return False

    return True


def convert_ical_component(component):
    start = get_start_date_from_ical(component)
    end = get_end_date_from_ical(component)

    return {
        "start": start,
        "end": end,
        "days": (end - start).days,
        "summary": str(component["SUMMARY"]),
        "description": str(component["DESCRIPTION"]),
        "categories": [str(cat) for cat in component["CATEGORIES"].cats]
        if "CATEGORIES" in component
        else [],
    }


def fetch_filtered_events(url):
    ical = fetch_ical(url)
    filtered_components = filter_ical(ical, date_filter)
    events = [convert_ical_component(c) for c in filtered_components]
    return sorted(events, key=lambda x: x["start"])
