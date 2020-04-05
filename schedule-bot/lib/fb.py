import os
import requests
from datetime import datetime, timedelta
from textutils import put_links_in_anchors


def get_facebook_posts(resource_id):
    FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']

    base_url = 'https://graph.facebook.com/v6.0/{}?fields={}&access_token={}'
    fields = "posts{permalink_url,created_time,message}"
    url = base_url.format(resource_id, fields, FACEBOOK_ACCESS_TOKEN)

    result = requests.get(url)
    json = result.json()['posts']['data']
    for post in json:
        yield {
            'id': post['id'],
            'message': put_links_in_anchors(post.get('message', '-')),
            'created_time':  datetime.strptime(post['created_time'], "%Y-%m-%dT%H:%M:%S%z").date(),
            'permalink_url': post['permalink_url']
        }


def filter_facebook_posts(posts, max_days=7):
    min_time = datetime.today() - timedelta(days=max_days)
    for p in posts:
        result = p['created_time'] >= min_time.date()
        if p['created_time'] >= min_time.date():
            yield p
