#!/bin/sh
set -e

[ ! -f "$SSH_KEYS_DIR" ] && ssh-keygen -f "$SSH_KEYS_DIR/ssh_host_rsa_key" -N '' -t rsa
[ ! -f "$SSH_KEYS_DIR" ] && ssh-keygen -f "$SSH_KEYS_DIR/ssh_host_ecdsa_key" -N '' -t ecdsa
[ ! -f "$SSH_KEYS_DIR" ] && ssh-keygen -f "$SSH_KEYS_DIR/ssh_host_ed25519_key" -N '' -t ed25519

[ -z "$GITHUB_USERS" ] && echo "Missing environment variable GITHUB_USERS." &&  exit 1 ;
echo "$GITHUB_USERS" | sed "s/,/\n/g" | while read github_user; do
	echo "$ACCESS_USER" | sed "s/,/\n/g" | while read access_user; do
		homedir=$(getent passwd "$access_user" | cut -d':' -f 6)
    curl "https://github.com/$github_user.keys" -s >> "$homedir/.ssh/authorized_keys";
  done
done;

exec $@;