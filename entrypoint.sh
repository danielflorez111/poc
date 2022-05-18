#!/bin/sh

#echo "Collect static files"
# python manage.py collectstatic --noinput

# Migrate
#python manage.py migrate || exit

python manage.py runserver 0.0.0.0:8000

exec "$@"
