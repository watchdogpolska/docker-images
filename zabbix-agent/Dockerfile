FROM zabbix/zabbix-agent:ubuntu-4.0.2@sha256:096f870409b38f4fc22e7f730821a35a0d7401bfad5b9f6dd2c422a1bd3253ce
RUN apt-get update \
&& apt-get install -y --no-install-recommends python \
&& rm -rf /var/lib/apt/lists/*
COPY ./userparameter_diskperformance.conf /etc/zabbix/zabbix_agentd.d
COPY ./lld-disks.py /usr/local/bin/lld-disks.py
