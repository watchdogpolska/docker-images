FROM openjdk:8-jre@sha256:7ee341dd70298e4ad59e1c0c1b00648aaaa097a9e6f1ae1c66af1e4b9c473737

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

