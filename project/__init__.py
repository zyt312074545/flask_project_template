import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    # register the database commands
    from project.models import init_db, init_db_command
    init_db(app)
    init_db_command(app)

    # apply the blueprints to the app
    # from project.controller import auth, blog
    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    # app.add_url_rule('/', endpoint='index')
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
