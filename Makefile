flake8:
	flake8 dokku_dashboard

test:
	pytest tests

setup:
	pip install -r requirements-local.txt

run:
	gunicorn -c gunicorn.cfg dokku_dashboard.app:app
