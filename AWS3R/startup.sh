#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 AWS3R.wsgi