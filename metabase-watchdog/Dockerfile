FROM openjdk:8-jre@sha256:6a53b55da7eec7418451cfd373328e3d8c893bf566cb9f5e30188606b693e72b

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

