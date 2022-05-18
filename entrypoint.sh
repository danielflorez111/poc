#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate || exit
python manage.py runserver 0.0.0.0:8000

exec "$@"
