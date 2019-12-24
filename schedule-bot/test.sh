#!/bin/bash 
docker build -t app . >&2
docker run -e CALENDAR_URL app