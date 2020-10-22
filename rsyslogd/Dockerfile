FROM alpine:3.12@sha256:d7342993700f8cd7aba8496c2d0e57be0666e80b4c441925fc6f9361fa81d10e
RUN apk add rsyslog
ADD ./remote.conf /etc/rsyslog.d/remote.conf
RUN sed '/.*module(load="imklog").*/d' -i /etc/rsyslog.conf
VOLUME /var/lib/rsyslog
VOLUME /var/syslog/hosts
EXPOSE 514
ENV TZ="Europe/Warsaw"
RUN rsyslogd -N 1 -n
CMD ["rsyslogd", "-n"]