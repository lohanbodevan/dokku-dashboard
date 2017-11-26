# Dokku Dashboard

[Dokku](https://github.com/dokku/dokku) is a powerfull and lightweight [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) with `git push` deployment.  
The goal of this project is build a web application dashboard above `Dokku` command line tool to manage apps.


## Install
1. SSH into your `Dokku` server host

2. Login as dokku user
```bash
sudo su - dokku
```

3. Clone this repository in `Dokku` home folder and exit dokku user
```bash
cd /home/dokku/dokku-dashboard
git clone https://github.com/lohanbodevan/dokku-dashboard.git
exit
```

4. Login as root
```bash
sudo su
```

5. Start APP
```bash
./start.sh
```

## Install from source code for development propose
### OS Requirements
* Python 3.x

### Setup
1. Install OS dependencies
```bash
make setup-os
```

2. Create virtualenv
```bash
virtualenv --python=python3 venv
```

3. Activate virtualenv
```bash
source venv/bin/activate
```

4. Install app dependencies
```bash
make setup
```

5. Run
```bash
make run
```

### Run tests
```
make test
```

### Run Flake8
```
make flake8
```
