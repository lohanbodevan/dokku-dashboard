#!/usr/bin/env bash

echo 'Stopping dokku_dashboard...'
pkill -f 'dokku_dashboard.app:app'
echo 'dokku_dashboard Stoped'

echo 'Instaling OS dependencies...'
make setup-os
echo 'OS depenencies installed'

echo 'Installing APP dependencies ...'
virtualenv --python=python3 venv
source "/home/dokku/dokku-dashboard/venv/bin/activate"
/home/dokku/dokku-dashboard/venv/bin/pip install -r requirements.txt
echo 'APP dependencies installed'

echo 'Starting APP ...'
/home/dokku/dokku-dashboard/venv/bin/python /home/dokku/dokku-dashboard/venv/bin/gunicorn -c gunicorn.cfg dokku_dashboard.app:app  &> /dev/null &

echo 'Restarting Nginx ...'
/etc/init.d/nginx restart

echo 'APP and Nginx running'
