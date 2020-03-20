from icalendar import Calendar
import datetime


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
