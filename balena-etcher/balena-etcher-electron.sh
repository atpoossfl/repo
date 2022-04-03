#!/bin/bash
if [[ $EUID -ne 0 ]] || [[ $ELECTRON_RUN_AS_NODE ]]; then
    exec electron12 /usr/share/balena-etcher "$@"
else
    exec electron12 --no-sandbox /usr/share/balena-etcher "$@"
fi
