FROM alpine:3.14@sha256:234cb88d3020898631af0ccbbcca9a66ae7306ecd30c9720690858c1b007d2a0
RUN apk add rsyslog
ADD ./remote.conf /etc/rsyslog.d/remote.conf
RUN sed '/.*module(load="imklog").*/d' -i /etc/rsyslog.conf
VOLUME /var/lib/rsyslog
VOLUME /var/syslog/hosts
EXPOSE 514
ENV TZ="Europe/Warsaw"
RUN rsyslogd -N 1 -n
CMD ["rsyslogd", "-n"]