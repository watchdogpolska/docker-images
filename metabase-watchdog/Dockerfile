FROM openjdk:8-jre@sha256:43be4571e9c8f8b91f56a46151f715abb990664d3625ce098184018d9b2065cf

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

