FROM openjdk:8-jre@sha256:77d74373d9b126c1d13cb10e410936068b2c63bcf79c7ec24f0b3212053e833b

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

