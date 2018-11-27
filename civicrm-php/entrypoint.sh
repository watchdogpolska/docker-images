#!/bin/sh
set -eux;

# required_env="Required OIDCClientID, OIDCClientSecret, OIDCCryptoPassphrase and OIDCClaimHD.";

# [ -z "$OIDCClientID" ] && echo "Missing environment variable $OIDCClientID. $required_env" &&  exit 1 ;
# [ -z "$OIDCClientSecret" ] && echo "Missing environment variable $OIDCClientSecret. $required_env" &&  exit 1 ;
# [ -z "$OIDCCryptoPassphrase" ] && echo "Missing environment variable $OIDCCryptoPassphrase. $required_env" &&  exit 1 ;
# [ -z "$OIDCClaimHD" ] && echo "Missing environment variable $OIDCClaimHD. $required_env" &&  exit 1 ;

# sed -e "s/{{OIDCClientID}}/$OIDCClientID/g" \
#     -e "s/{{OIDCClientSecret}}/$OIDCClientSecret/g" \
#     -e "s/{{OIDCCryptoPassphrase}}/$OIDCCryptoPassphrase/g" \
#     -e "s/{{OIDCClaimHD}}/$OIDCClaimHD/g" \
#     -i /etc/apache2/conf-enabled/mod_auth_openidc.conf;

# cat /etc/apache2/conf-enabled/mod_auth_openidc.conf

apachectl configtest;

exec docker-php-entrypoint $@
