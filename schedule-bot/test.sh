#!/bin/bash 
docker build -t app . >&2
docker run \
    -e CALENDAR_URL \
    -e TWITTER_API_KEY \
    -e TWITTER_API_SECRET \
    -e TWITTER_ACCESS_TOKEN \
    -e TWITTER_ACCESS_SECRET \
    -e FACEBOOK_ACCESS_TOKEN \
    app