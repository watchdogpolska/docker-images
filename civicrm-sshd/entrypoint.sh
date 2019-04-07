#!/bin/sh
set -e

[ -z "$GITHUB_USERS" ] && echo "Missing environment variable GITHUB_USERS." &&  exit 1 ;
echo "$GITHUB_USERS" | sed "s/,/\n/g" | while read username; do
    curl "https://github.com/$username.keys" -s >> ~/.ssh/authorized_keys;
done;

exec $@