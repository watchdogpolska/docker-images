FROM quay.io/watchdogpolska/ubuntu-sshd-github:latest
MAINTAINER Adam Dobrawy "http://github.com/ad-m/"
RUN wp --allow-root
&& curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
&& php wp-cli.phar --info \
&& chmod +x wp-cli.phar \
&& mv wp-cli.phar /usr/local/bin/wp
EXPOSE 22
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
