FROM alpine:3.12@sha256:3c7497bf0c7af93428242d6176e8f7905f2201d8fc5861f45be7a346b5f23436
RUN apk add rsyslog
ADD ./remote.conf /etc/rsyslog.d/remote.conf
RUN sed '/.*module(load="imklog").*/d' -i /etc/rsyslog.conf
VOLUME /var/lib/rsyslog
VOLUME /var/syslog/hosts
EXPOSE 514
ENV TZ="Europe/Warsaw"
RUN rsyslogd -N 1 -n
CMD ["rsyslogd", "-n"]