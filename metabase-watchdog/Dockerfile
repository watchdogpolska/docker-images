FROM openjdk:8-jre@sha256:ad86f17cfe68e8ae9073795c3121698f27f16013ce72aadb244c4991197fac27

WORKDIR /opt
ENV METABASE_VERSION="0.31.2"
RUN wget --no-verbose "http://downloads.metabase.com/v${METABASE_VERSION}/metabase.jar" -O ./metabase.jar

ADD startup.sh /
ADD env_secrets_expand.sh /

CMD ["/startup.sh"]

