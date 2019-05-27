#!/usr/bin/env bash

cd /usr/share/webapps/ramais/backend/ramais

mkdir -p /usr/share/webapps/ramais/backend/ramais/var/run
rm -f /usr/share/webapps/ramais/backend/ramais/var/run/*

exec /usr/share/envs/ramais/bin/gunicorn config.wsgi -c deploy/production/gunicorn.conf.py  --env DJANGO_SETTINGS_MODULE=config.settings.production