#!/bin/sh
set -eux
cat > ~/mysql.cnf << EOF 
[mysqldump]
host=$BACKUP_MYSQL_HOST
user=$BACKUP_MYSQL_USER
password=$BACKUP_MYSQL_PASSWORD
EOF
mysqldump --defaults-file=~/mysql.cnf --all-databases  --single-transaction > /output/mysql-$(date +"%F_%H:%M:%S").sql;