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

```
# init database
$ pipenv run flask initdb

# delete datebase and init
$ pipenv run flask initdb --drop

# migrate database
$ pipenv run flask db init
$ pipenv run flask db migrate -m "init database"

$ pipenv run flask db upgrade
```

Run Project
------------------------------

```
$ pipenv run flask run
```

Run Project production
------------------------------

- `.env`: Set ENV Variables
- `.flaskenv`: Set FLASK_ENV Variables

```
# work = 2 x CPU + 1
$ gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
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

[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)

[authlib](https://github.com/lepture/authlib)

[GitHub-Flask](https://github.com/cenkalti/github-flask)

[Flask-Caching](https://github.com/sh4nks/flask-caching)
