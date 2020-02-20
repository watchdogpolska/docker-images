#!/bin/sh
set -eux
TOKEN="$RANDOM"
NAME="rsyslog-$TOKEN"
TEST_DIR=$(mktemp -d)
trap "rm -f $TEST_DIR" EXIT

# Given
docker build -t rsyslog .
docker run -it -v "$TEST_DIR:/var/syslog/hosts" -d -p 514:514/udp -p 514:514 --rm --name "$NAME" rsyslog 
trap "docker stop $NAME" EXIT
# When
echo "tcp-$TOKEN" | logger --server 127.0.0.1 -P 514 -T
echo "udp-$TOKEN" | logger --server 127.0.0.1 -P 514 -d
# Then
sleep 1
grep "tcp-$TOKEN" "$TEST_DIR" -r
grep "udp-$TOKEN" "$TEST_DIR" -r