#!/bin/bash


if [ -z "${1}" ]; then
    echo "please provide your function name"
    echo "ex: ./deploy.sh <func_name>"
    echo "maybe: `cat *.py | grep def`"
	exit 1
fi

echo "your function name: $1"
functions-framework --target=$1 --port 5555 --debug
