import os
import requests
from datetime import datetime, timedelta
from textutils import put_links_in_anchors


def get_facebook_data(resource_id):
    FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']

    base_url = 'https://graph.facebook.com/v6.0/{}?fields={}&access_token={}'
    fields = "posts{permalink_url,created_time,message},videos{id,permalink_url,description,title,created_time}"
    url = base_url.format(resource_id, fields, FACEBOOK_ACCESS_TOKEN)

    result = requests.get(url)
    postsJson = result.json()['posts']['data']
    videosJson = result.json()['videos']['data']

    posts = list(format_facebook_posts(postsJson))
    videos = list(format_facebook_videos(videosJson))

    return {'posts': posts, 'videos': videos}


def format_facebook_posts(postsData):
    posts = []
    for post in postsData:
        yield {
            'id': post['id'],
            'message': put_links_in_anchors(post.get('message', '-')),
            'created_time':  format_date(post['created_time']),
            'permalink_url': post['permalink_url']
        }
    return posts


def format_facebook_videos(videosData):
    for video in videosData:
        yield {
            'id': video['id'],
            # video permalinks does not contain full uri
            'permalink_url': 'https://www.facebook.com/{}'.format(video['permalink_url']),
            'description': put_links_in_anchors(video['description']),
            'title': video['title'],
            'created_time': format_date(video['created_time'])
        }


def filter_facebook_resources(resources, max_days=7):
    min_time = datetime.today() - timedelta(days=max_days)
    for r in resources:
        if r['created_time'] >= min_time.date():
            yield r


def format_date(date_to_format):
    return datetime.strptime(date_to_format, "%Y-%m-%dT%H:%M:%S%z").date()
