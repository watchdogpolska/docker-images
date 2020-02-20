# rsyslogd

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/rsyslogd/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/rsyslogd)

Docker image containing [Rsyslog](https://www.rsyslog.com/) with configuration to accept any logs on TCP&UDP port 514.

The slogan of Rsyslog is:

> The rocket-fast system for log processing

Use ```/var/syslog/hosts``` as volume for stored logs.

## Example usage

```bash
docker run -p 514:514/udp -p 514:514 "./logs/:/var/syslog/hosts" quay.io/watchdogpolska/rsyslogd
```

## Testing

Use ```test.sh``` to validate flow.