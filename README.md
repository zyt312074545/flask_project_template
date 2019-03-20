# Flask Project Template for development.

Managing Dependencies
---------------------

```
$ pipenv install
```

Managing Environment Variables
------------------------------

- `.env`: Manage Environment Variables (Which is important, so don't push)
- `.flaskenv`: Manage Flask Environment Variables
- `.gitignore`: Manage Git Ignore Variables
- `.dockerignore`: Manage Docker Ignore Variables

Init Database
------------------------------

Before initialization database, you need decide the database type in 
`alembic/env.py`. 

```
$ pipenv run alembic init alembic

$ pipenv run alembic revision --autogenerate -m "initdb"

$ pipenv run alembic upgrade head
```

When add new model, model need write in `models/__init__.py` file.

Run Project
------------------------------

```
$ pipenv run flask run
```

Test Project
------------------------------

```
$ cd /tests

$ pipenv run pytest
```

View Project All Routes
------------------------------
```
$ pipenv run flask routes
```

Flask Extensions
------------------------------
[Flask Extensions](http://flask.pocoo.org/extensions/)

[flask-apispec](https://github.com/jmcarp/flask-apispec)

