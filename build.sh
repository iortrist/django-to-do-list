#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django

python manage.py collectstatic --no-input
python manage.py migrate
