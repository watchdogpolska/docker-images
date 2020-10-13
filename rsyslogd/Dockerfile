FROM alpine:3.12@sha256:a15790640a6690aa1730c38cf0a440e2aa44aaca9b0e8931a9f2b0d7cc90fd65
RUN apk add rsyslog
ADD ./remote.conf /etc/rsyslog.d/remote.conf
RUN sed '/.*module(load="imklog").*/d' -i /etc/rsyslog.conf
VOLUME /var/lib/rsyslog
VOLUME /var/syslog/hosts
EXPOSE 514
ENV TZ="Europe/Warsaw"
RUN rsyslogd -N 1 -n
CMD ["rsyslogd", "-n"]