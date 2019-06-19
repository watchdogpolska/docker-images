FROM zabbix/zabbix-agent:ubuntu-4.2.2
RUN apt-get update \
&& apt-get install -y --no-install-recommends python \
&& rm -rf /var/lib/apt/lists/*
COPY ./userparameter_diskperformance.conf /etc/zabbix/zabbix_agentd.d
COPY ./lld-disks.py /usr/local/bin/lld-disks.py
