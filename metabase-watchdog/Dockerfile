FROM openjdk:8-jre

WORKDIR /opt

RUN wget --no-verbose http://downloads.metabase.com/v0.31.2/metabase.jar -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

