#!/bin/bash
set -e

./wait-for-it.sh "$DB_HOST":"$DB_PORT"
./wait-for-it.sh "$REDIS_HOST":"$REDIS_PORT"

case "$1" in
    web)
        python manage.py migrate --noinput
        python manage.py collectstatic --noinput
        exec gunicorn web_app.wsgi:application \
              -b 0.0.0.0:8000 \
              -w "$WORKERS_COUNT"
        ;;
    *)
        exec "$@"
esac
