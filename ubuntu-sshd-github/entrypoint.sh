#!/bin/sh
set -e

[ -z "$GITHUB_USERS" ] && echo "Missing environment variable GITHUB_USERS." &&  exit 1 ;

ls -lah /root/;

echo "" > /root/.ssh/authorized_keys;
echo "$GITHUB_USERS" | sed "s/,/\n/g" | while read username; do
    curl "https://github.com/$username.keys" -s >> /root/.ssh/authorized_keys;
done;

exec $@