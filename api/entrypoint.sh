#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

python manage.py loaddata fixtures/users.json --app auth.User
python manage.py loaddata fixtures/brands.json --app brands.Brand
python manage.py loaddata fixtures/products.json --app products.Product

exec "$@"
