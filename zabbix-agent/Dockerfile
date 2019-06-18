FROM zabbix/zabbix-agent:ubuntu-4.2.2
RUN apt-get update \
&& apt-get install -y --no-install-recommends python-minimal \
&& rm -rf /var/lib/apt/lists/* \
COPY ./lld-disks.py /usr/local/bin/lld-disks.py
COPY ./userparameter_diskperformance.conf /etc/zabbix/zabbix_agentd.d
