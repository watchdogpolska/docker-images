#!/bin/sh
set -eux

if [ -z "$BACKUP_POSTGRESQL_DATABASE" ]; then
    PGPASSWORD="$BACKUP_POSTGRESQL_PASSWORD" pg_dumpall --host="$BACKUP_POSTGRESQL_HOST" --user="$BACKUP_POSTGRESQL_USER" > /output/postgres-$(date +"%F_%H:%M:%S").sql;
else
    PGPASSWORD="$BACKUP_POSTGRESQL_PASSWORD" pg_dump --dbname="$BACKUP_POSTGRESQL_DATABASE" --host="$BACKUP_POSTGRESQL_HOST" --user="$BACKUP_POSTGRESQL_USER" > /output/postgres-$(date +"%F_%H:%M:%S").sql;
fi;