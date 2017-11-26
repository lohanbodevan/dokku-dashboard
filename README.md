# Dokku Dashboard


## Install from source code
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
