# schedule-bot

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/schedule-bot/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/schedule-bot)

Docker image containing tool designed for periodically send iCal via e-mail.

## Usage

```bash
docker run \
    -e CALENDAR_URL="..." \
    -e SMTP_URL="smtp://xxx" \
    -e SMTP_TO="example@example.com" \
    -e SMTP_FROM="example@example.com" \
    quay.io/watchdogpolska/schedule-bot
```

## Settings

* ```CALENDAR_URL```
* ```SMTP_URL```
* ```SMTP_FROM```
* ```SMTP_TO```
