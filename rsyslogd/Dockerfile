FROM alpine:3.13@sha256:69e70a79f2d41ab5d637de98c1e0b055206ba40a8145e7bddb55ccc04e13cf8f
RUN apk add rsyslog
ADD ./remote.conf /etc/rsyslog.d/remote.conf
RUN sed '/.*module(load="imklog").*/d' -i /etc/rsyslog.conf
VOLUME /var/lib/rsyslog
VOLUME /var/syslog/hosts
EXPOSE 514
ENV TZ="Europe/Warsaw"
RUN rsyslogd -N 1 -n
CMD ["rsyslogd", "-n"]