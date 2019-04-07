FROM quay.io/watchdogpolska/civicrm-php:latest
MAINTAINER Adam Dobrawy "http://github.com/ad-m/"
# Setup SSHD server
RUN apt-get update \
&& apt-get install -y openssh-server curl wget git less \
&& rm -rf /var/lib/apt/lists/* \
RUN mkdir /run/sshd && mkdir /var/run/sshd && mkdir /root/.ssh
COPY ./entrypoint.sh ./entrypoint.sh
# Add wp-cli
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
&& php wp-cli.phar --info \
&& chmod +x wp-cli.phar \
&& mv wp-cli.phar /usr/local/bin/wp \
&& wp --allow-root
EXPOSE 22
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
