import os
import tweepy
from datetime import datetime, timedelta


def authorize_twitter_api():
    API_KEY = os.environ["TWITTER_API_KEY"]
    API_SECRET = os.environ["TWITTER_API_SECRET"]
    ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_SECRET"]

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    api.verify_credentials()  # will throw error if wrong credentials

    return api


def get_user_tweets(api, id='SiecObywatelska', limit=30, expiration_time=7):
    tweets = []
    min_time = datetime.today() - timedelta(days=expiration_time)

    for tweet in tweepy.Cursor(api.user_timeline, id=id).items():
        if tweet.created_at < min_time:
            break

        tweets.append({
            "id": tweet.id,
            "text": tweet.text,
            "created_at": tweet.created_at
        })

        if len(tweets) == limit:
            break

    return tweets
