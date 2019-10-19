# azure-export

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/azure-export/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/azure-export)

Docker image containing tools for archiving Azure metrics of Azure storage accounts to relation-databases.

## Usage

```.bash
docker run -e AZURE_APP_PASSWORD="xxx" -e DATABASE_URL="postgres://xxx" app
```

## Features

* set ```ip``` property of Mixpanel payloads according to ```x-forwarded-for``` header
* truncate URL to remove specified prefix
* Sentry exception-handler

## Settings

* ```AZURE_APP_PASSWORD``` - Password for Azure Service Principal
* ```DATABASE_URL``` - URL of database server eg. sqlite, mysql, postgresql
