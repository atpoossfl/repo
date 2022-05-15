#!/bin/sh

export ELECTRON_FORCE_IS_PACKAGED=true
exec electron16 /usr/share/fluent-reader/app.asar "$@"
