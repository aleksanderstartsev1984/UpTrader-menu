#!bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
cd show_menu

python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py create_menu
python manage.py runserver
