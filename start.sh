#!/usr/bin/env bash
python3 manage.py migrate
python3 manage.py makemigrations red
python3 manage.py migrate
python3 manage.py createsuperuser