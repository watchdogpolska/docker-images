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
    -e TWITTER_API_KEY="..." \
    -e TWITTER_API_SECRET="..."\
    -e TWITTER_ACCESS_TOKEN="..."\
    -e TWITTER_ACCESS_SECRET="..." \
    -e FACEBOOK_ACCESS_TOKEN="..." \
    quay.io/watchdogpolska/schedule-bot
```

## Settings

- `CALENDAR_URL`
- `SMTP_URL`
- `SMTP_FROM`
- `SMTP_TO`
- `TWITTER_API_KEY`
- `TWITTER_API_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_SECRET`
- `FACEBOOK_ACCESS_TOKEN`

## Acquiring Twitter API keys

To acquire Twitter API keys you have to go to [https://developer.twitter.com/en/apps](developer.twitter.com/en/apps),
and register new application. After it's done, go to your app, `Keys and tokens` section and copy your credentials.

## Obtaining Facebook Access Token

To obtain Facebook Access Token go to [https://developers.facebook.com](developers.facebook.com),
register new application, then go to `Tools` -> `Graph API Explorer` and click generate new token.
For this application to work you must provide `manage_pages` permission, or enable
[Page Public Content Access feature](https://developers.facebook.com/docs/apps/review/feature/).
