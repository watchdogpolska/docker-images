import datetime
import feedparser
from time import mktime


def struct_to_datetime(value):
    return datetime.datetime.fromtimestamp(mktime(value))


def parse_feed(url, max_days=7):
    minimum_time = datetime.date.today() - datetime.timedelta(days=max_days)
    d = feedparser.parse(url)
    return [
        {
            **x,
            **{
                "link_html": next(
                    (link.href for link in x["links"]
                     if link.type == "text/html"), None
                )
            },
        }
        for x in d["entries"]
        if minimum_time < struct_to_datetime(x["published_parsed"]).date()
    ]
