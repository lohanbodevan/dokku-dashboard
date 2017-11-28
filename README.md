# Dokku Dashboard <a href="https://travis-ci.org/lohanbodevan/dokku-dashboard"><img alt="Travis Status" src="https://travis-ci.org/lohanbodevan/dokku-dashboard.svg?branch=master"></a> [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/lohanbodevan/dokku-dashboard/blob/master/LICENSE)


[Dokku](https://github.com/dokku/dokku) is a powerfull and lightweight [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) with `git push` deployment.  
The goal of this project is build a web application dashboard above `Dokku` command line tool to manage apps.


## OS Requirements
* Python 3.x
## Install
1. SSH into your `Dokku` server host

2. Login as dokku user
```bash
sudo su - dokku
```

3. Set dashboard environment variables
```bash
export SERVER_PROTOCOL=http
export SERVER_HOST=platform.domain.com
```

4. Clone this repository in `Dokku` home folder and exit dokku user
```bash
cd /home/dokku
git clone https://github.com/lohanbodevan/dokku-dashboard.git
exit
```

5. Login as root
```bash
sudo su
```

6. Go to application folder
```bash
cd /home/dokku/dokku-dashboard
```

7. Start APP
```bash
./start.sh
```

## Endpoints
Access `Dokku Dashboard` as `http://dashboard.<your_dokku_server_domain>/apps`

![Dashboard](docs/dashboard.png?raw=true "Dashboard")

## Install for development purpose
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
