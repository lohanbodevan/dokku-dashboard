# Dokku Dashboard


## Install from source code
### Requirements
* Python 3.x
* Virtualenv

### Setup
1. Create virtualenv
```bash
virtualenv --python=python3 venv
```

2. Activate virtualenv
```bash
. venv/bin/activate
```

3. Install dependencies
```bash
make setup
```

4. Run
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
