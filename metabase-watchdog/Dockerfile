FROM openjdk:8-jre@sha256:60983e6fcb0f888cbd1edde0b9f5b2f77a4da004f3417496e38703353f645be1

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

