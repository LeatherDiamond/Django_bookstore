#!/bin/bash
python src/manage.py migrate
python src/create_default_db_data.py
python src/manage.py runserver 0.0.0.0:8000