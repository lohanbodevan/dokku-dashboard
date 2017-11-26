flake8:
	flake8 dokku_dashboard

test:
	pytest tests

setup-os:
	apt-get update
	grep -v '^#\s*' requirements.apt |  xargs -r -- apt-get install -y

setup:
	pip install -r requirements-local.txt

run:
	gunicorn -c gunicorn.cfg dokku_dashboard.app:app
