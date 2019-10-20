# azure-export

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/azure-export/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/azure-export)

Docker image containing tools for archiving Azure metrics of Azure storage accounts to relation-databases.

## Usage

```.bash
docker run -e AZURE_APP_PASSWORD="xxx" -e DATABASE_URL="postgres://xxx" quay.io/watchdogpolska/azure-export
```

## Features

* Support multiple databases eg. PostgreSQL, SQLite

## Settings

* ```AZURE_APP_PASSWORD``` - Password for Azure Service Principal
* ```DATABASE_URL``` - URL of database server eg. PostgreSQL, SQLite
