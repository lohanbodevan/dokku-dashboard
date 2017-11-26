flake8:
	flake8 dokku_dashboard

test:
	pytest tests

setup:
	pip install -r requirements-local.txt

run:
	python dokku_dashboard/app.py
