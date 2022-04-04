#!/bin/sh

exec @ELECTRON@ /usr/share/element/app.asar --disable-dev-mode "$@"
