FROM php:5.6-apache
RUN a2enmod rewrite
# install the PHP extensions we need
RUN apt-get update \
&& apt-get install -y libpng16-16 libpng-dev \
&& rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-install mysqli pdo_mysql gd
RUN cp /usr/local/etc/php/php.ini-development $PHP_INI_DIR/conf.d/php.ini
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD apache2-foreground