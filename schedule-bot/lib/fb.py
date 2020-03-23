import os
import requests
from datetime import datetime, timedelta


def get_facebook_posts(resource_id):
    FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']

    base_url = 'https://graph.facebook.com/v6.0/{}?fields={}&access_token={}'
    fields = "posts"
    url = base_url.format(page_id, fields, FACEBOOK_ACCESS_TOKEN)
    result = requests.get(url)
    return result.json()['posts']['data']


def filter_facebook_posts(posts, max_days=7):
    min_time = datetime.today() - timedelta(days=max_days)
    return [p for p in posts if datetime.strptime(p['created_time'], "%Y-%m-%dT%H:%M:%S%z").date() >= min_time.date()]


page_id = "SiecObywatelskaWatchdogPolska"
posts = get_facebook_posts(page_id)
filtered_posts = filter_facebook_posts(posts)
print(filtered_posts)
