# mycli

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/pyupgrade/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/pyupgrade)

Docker image containing [pyupgrade](https://github.com/asottile/pyupgrade) - Python application.

## Features

* ignored following directories:

  * ```./node_modules/*```
  * ```./.tox/*```
  * ```./bower_components/*```

## Usage

```.bash
docker run -it -v $PWD:/data quay.io/watchdogpolska/pyupgrade
```