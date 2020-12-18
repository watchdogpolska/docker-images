FROM openjdk:8-jre@sha256:1b7083c5b2fa87ab7b8e87b4a761945267fc8fe5ae42252e592f083cd5674d76

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

