#!/bin/bash

find . -name "*.py" ! \( -wholename "./node_modules/*" -o -wholename "./.tox/*" -o -wholename "./bower_components/*" \) | xargs pyupgrade $@