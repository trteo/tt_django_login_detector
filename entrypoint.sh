#!/bin/sh

cd admin_panel_login_detector_project

python manage.py migrate
echo "migrations done"

python fill_db.py
echo "DB filled"


python manage.py runserver 0.0.0.0:8000
