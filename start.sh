#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
