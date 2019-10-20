#!/bin/bash
set -eux
echo "$(date -R): Started backup";
./sources/${BACKUP_SRC}.sh;
echo "$(date -R): Finished backup";
find /output -mtime +3 -mindepth 1 -print -delete;
find /output -print