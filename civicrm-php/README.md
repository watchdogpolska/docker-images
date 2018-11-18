# civicrm-php

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/civicrm-php/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/civicrm-php)

Docker image for runtime of [CiviCRM](https://civicrm.org/) - PHP application.

The slogan of CiviCRM is:

> Build, engage, and organize your constituents

See [CiviCRM homepage](https://civicrm.org/) for details.

Use ```DOCKER-SECRET:{{secret_name}}``` as environment variable value to access [docker secret](https://docs.docker.com/engine/reference/commandline/secret/).

## Environment 

| Name                 | Description
| -------------------- | -----------
| OIDCClientID         | Google Client ID (for OAuth 2.0 authentication)
| OIDCClientSecret     | Google Client Secret (for OAuth 2.0 authentication)
| OIDCCryptoPassphrase | Random password for cookie encryption of OAuth 2.0 authentication session
| OIDCClaimHD          | Google domain enforced during OAuth 2.0 authentication