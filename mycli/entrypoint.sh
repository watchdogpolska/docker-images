#!/bin/bash
echo $@
exec mycli "$@"
