#!/bin/sh
set -eux

PGPASSWORD="$BACKUP_POSTGRESQL_PASSWORD" pg_dumpall --host="$BACKUP_POSTGRESQL_HOST" --user="$BACKUP_POSTGRESQL_USER" > /output/postgres-$(date +"%F_%H:%M:%S").sql