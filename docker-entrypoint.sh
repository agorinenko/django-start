#!/bin/bash
set -e

./wait-for-it.sh "$DB_HOST":"$DB_PORT"
./wait-for-it.sh "$REDIS_HOST":"$REDIS_PORT"

case "$1" in
    web)
        python manage.py migrate --noinput
        python manage.py collectstatic --noinput
        exec supervisord -c /opt/app/supervisord.conf
        ;;
    *)
        exec "$@"
esac
