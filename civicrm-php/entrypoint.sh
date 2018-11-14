#!/bin/bash
if [ -z "$OIDCClientID" -o -z "$OIDCClientSecret" -o -z "$OIDCCryptoPassphrase" -o -z "$OIDCClaimHD" ]; then
    echo "Missing environment variables. Required OIDCClientID, OIDCClientSecret, OIDCCryptoPassphrase and OIDCClaimHD.";
    exit;
fi;

sed -e "s/{{OIDCClientID}}/$OIDCClientID/g" \
    -e "s/{{OIDCClientSecret}}/$OIDCClientSecret/g" \
    -e "s/{{OIDCCryptoPassphrase}}/$OIDCCryptoPassphrase/g" \
    -e "s/{{OIDCClaimHD}}/$OIDCClaimHD/g" \
    -i /etc/apache2/conf-enabled/mod_auth_openidc.conf && \
cat /etc/apache2/conf-enabled/mod_auth_openidc.conf && \
apachectl configtest && \
exec docker-php-entrypoint $@