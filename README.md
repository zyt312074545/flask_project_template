# My flask templet for development.

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

View Project All Routes
------------------------------
```
$ pipenv run flask routes
```
