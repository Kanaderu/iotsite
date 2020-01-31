#!/bin/bash

pip install -r requirements.txt

cd dashboard
rm -r static
yarn
yarn build
cd ..

sudo service supervisor restart

python manage.py collectstatic
python manage.py makemigrations --settings=iotsite.settings.production
python manage.py migrate --settings=iotsite.settings.production
