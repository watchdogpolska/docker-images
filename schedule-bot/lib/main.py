import os
import datetime

from ical import fetch_filtered_events
from mailer import send_mail, render_html, random_email_subject
from feed import parse_feed
from twitter import authorize_twitter_api, get_user_tweets
from fb import get_facebook_posts, filter_facebook_posts

ETR_WARSZAWA_URL = "https://raw.githubusercontent.com/ad-m/etr-warszawa-ical/master/648.ics"
FACEBOOK_ID = "SiecObywatelskaWatchdogPolska"


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

    twitter_api = (
        authorize_twitter_api()
        if "TWITTER_API_KEY" in os.environ
        else False
    )

    tweets = (
        get_user_tweets(twitter_api)
        if twitter_api
        else []
    )

    fb_posts = (
        list(filter_facebook_posts(get_facebook_posts(FACEBOOK_ID)))
        if "FACEBOOK_ACCESS_TOKEN" in os.environ
        else []
    )

    it_days = (datetime.date(2020, 7, 1) - datetime.datetime.now().date()).days

    html = render_html(wd_events, etr_events, feed_events,
                       it_days, tweets, fb_posts)
    subject = random_email_subject()

    return send_mail(subject, html)


if __name__ == "__main__":
    main()
