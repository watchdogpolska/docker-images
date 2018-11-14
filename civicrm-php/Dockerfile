FROM php:5.6-apache
RUN a2enmod rewrite
# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng16-16 libpng-dev && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-install mysqli pdo_mysql gd
RUN cp /usr/local/etc/php/php.ini-development $PHP_INI_DIR/conf.d/php.ini
RUN apt-get update \
&&  apt-get install -y libcjose0 libhiredis0.13 libjansson4 \
&&  rm -rf /var/lib/apt/lists/* \
&&  curl http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u9_amd64.deb -L -s -o libssl1.0.0.deb \
&&  curl https://github.com/zmartzone/mod_auth_openidc/releases/download/v2.3.8/libapache2-mod-auth-openidc_2.3.8-1.stretch+1_amd64.deb -L -s -o libapache2-mod-auth-openidc_2.3.8.deb \
&&  dpkg -i libssl1.0.0.deb libapache2-mod-auth-openidc_2.3.8.deb \
&&  rm libssl1.0.0.deb libapache2-mod-auth-openidc_2.3.8.deb
RUN a2enmod auth_openidc
COPY ./mod_auth_openidc.conf /etc/apache2/conf-enabled/mod_auth_openidc.conf
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD apache2-foreground