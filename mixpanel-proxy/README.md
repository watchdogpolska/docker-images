# mixpanel-proxy

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/mixpanel-proxy/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/mixpanel-proxy)

Docker image containing proxy to [Mixpanel](https://mixpanel.com/) API.

## Usage

```.bash
docker run -p 3000:3000 quay.io/watchdogpolska/mixpanel-proxy
```

# Features

* set ```ip``` property of Mixpanel payloads according to ```x-forwarded-for``` header
* truncate URL to remove specified prefix
* Sentry exception-handler

# Settings

* ```MIXPANEL_API_URL``` - URL of mixpanel proxy server. Default: ```https://api.mixpanel.com```
* ```PORT``` - Port for listing of proxy server. Default: ```3000```
* ```TRUNCATE_URL``` - Regexp of truncated elements from URL. Default: ```/mpanel/```
* ```SENTRY_DSN``` - DSN of Sentry exception-handler: Disabled by default
