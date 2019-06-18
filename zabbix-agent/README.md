# zabbix-agent

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/zabbix-agent/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/zabbix-agent)

Docker image containing Zabbix-Agent enriched with additional functionalities.

## Usage

```.bash
docker run -p 3000:3000 quay.io/watchdogpolska/zabbix-agent
```

For details, see [upstream](https://hub.docker.com/r/zabbix/zabbix-agent) ```zabbix-agent/zabbix``` image.

# Features

* ```UserParameter``` for detailed metrics about disk performance based on [watchdogpolska.zabbix.diskperformance](https://github.com/watchdogpolska/infra/tree/master/ansible/roles/watchdogpolska.zabbix.diskperformance)

# Settings

No custom settings.

For common settings, see [upstream](https://hub.docker.com/r/zabbix/zabbix-agent) ```zabbix-agent/zabbix``` image.
