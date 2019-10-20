# remote-archiver

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/remote-archiver/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/remote-archiver)

Docker image containing tool designed for archiving data from remote locations. It can be the basis for a backup system.

## Usage

```bash
docker run -e BACKUP_SRC="postgresql" \
    -e BACKUP_POSTGRESQL_HOST="postgres://xxx" \
    -e BACKUP_POSTGRESQL_USER="postgres://xxx" \
    -e BACKUP_POSTGRESQL_PASSWORD="postgres://xxx" \
    -v output:/output
    quay.io/watchdogpolska/remote-archiver
```

## Features

* Support multiple sources:
  * PostgreSQL - ```postgresql```
  * PostgreSQL - ```mysql```
* Support cleanup after retention time

## Settings

* ```BACKUP_SRC``` - Source of data eg. ```postgresql```
* PostgreSQL:

  * ```BACKUP_POSTGRESQL_HOST```
  * ```BACKUP_POSTGRESQL_USER```
  * ```BACKUP_POSTGRESQL_PASSWORD```
