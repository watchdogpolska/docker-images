FROM openjdk:8-jre@sha256:13a8385cc52863ab88e37508dc8fd7af27d265b1facd139051e1fbe3d63e2c65

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

