#!/usr/bin/env bash

# Postgres позволяет подключиться к удаленной базе указав ссылку на нее после флага -d
# ссылка подгрузится из переменной окружения, которую нам нужно будет указать на сервисе деплоя
# дальше мы загружаем в поключенную базу наш sql-файл с таблицами
# Exit on error
set -o errexit

source .env
make install && psql -a -d $DATABASE_URL

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
make migrate