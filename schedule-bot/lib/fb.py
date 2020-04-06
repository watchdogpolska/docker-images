import os
import requests
from datetime import datetime, timedelta
from textutils import put_links_in_anchors


def get_facebook_data(resource_id):
    FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']

    base_url = 'https://graph.facebook.com/v6.0/{}?fields={}&access_token={}'
    fields = "posts{permalink_url,created_time,message},videos{id,permalink_url,description,title}"
    url = base_url.format(resource_id, fields, FACEBOOK_ACCESS_TOKEN)

    result = requests.get(url)
    postsJson = result.json()['posts']['data']
    videosJson = result.json()['videos']['data']

    posts = format_facebook_posts(postsJson)
    videos = format_facebook_videos(videosJson)

    return {posts: posts, videos: videos}


def format_facebook_posts(postsData):
    for post in postsData:
        yield {
            'id': post['id'],
            'message': put_links_in_anchors(post.get('message', '-')),
            'created_time':  format_date(post['date']),
            'permalink_url': post['permalink_url']
        }


def format_facebook_videos(videosData):
    for video in videosData:
        yield {
            'id': video['id'],
            'permalink_url': video['permalink_url'],
            'description': put_links_in_anchors(video['description']),
            'title': video['title'],
            'created_time': video['created_time']
        }


def filter_facebook_posts(posts, max_days=7):
    min_time = datetime.today() - timedelta(days=max_days)
    for p in posts:
        if p['created_time'] >= min_time.date():
            yield p


def format_date(date):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z").date()
