FROM chialab/php:7.2-apache
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Poland /etc/localtime
ENV WP_CLI_VERSION="2.1.0"
RUN curl -s -L "https://github.com/wp-cli/wp-cli/releases/download/v${WP_CLI_VERSION}/wp-cli-${WP_CLI_VERSION}.phar" -o /usr/local/bin/wp \
&& chmod +x /usr/local/bin/wp