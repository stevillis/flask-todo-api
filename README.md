# Flask Todo REST API
A Todo REST API app made with Flask.

## Running the API
```shell
$ python run.py
```

## Running migrations

### Add api to PATH
```shell
$ set FLASK_APP=api.py
```

### Start db migration
```shell
$ flask db init
```

### Migrate models
```shell
$ flask db migrate
```

### Apply migrations to DB
```shell
$ flask db upgrade
```
