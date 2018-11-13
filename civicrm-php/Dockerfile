FROM php:7-apache
RUN a2enmod rewrite
# install the PHP extensions we need
RUN docker-php-ext-install mysqli
RUN cp /usr/local/etc/php/php.ini-development $PHP_INI_DIR/conf.d/php.ini