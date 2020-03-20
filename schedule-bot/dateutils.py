import datetime
from time import mktime


def struct_to_datetime(value):
    return datetime.datetime.fromtimestamp(mktime(value))


def datetimeformat(value, format="%Y-%m-%d"):
    return value.strftime(format)


def structformat(value, format="%Y-%m-%d"):
    return datetimeformat(struct_to_datetime(value), format)


def to_date(x):
    if isinstance(x, datetime.datetime):
        return x.date()
    return x
