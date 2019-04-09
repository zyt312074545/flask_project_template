import logging
import os
from logging.handlers import RotatingFileHandler

import click
from flask import Flask, request, jsonify
from flask_sqlalchemy import get_debug_queries

from app.settings import config
from app.extensions import db, migrate
from app.apis.test import api_test
from app.models.test_model import TestModel
from app.utils.exceptions import NewError


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask("app")
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    register_logging(app)
    register_errors(app)
    register_request_handlers(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(api_test)


def register_commands(app):
    @app.cli.command()
    @click.option("--drop", is_flag=True, help="Create after drop.")
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm(
                "This operation will delete the database, do you want to continue?",
                abort=True,
            )
            db.drop_all()
            click.echo("Drop tables.")
        db.create_all()
        click.echo("Initialized database.")


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, TestModel=TestModel)


def register_logging(app):
    class RequestFormatter(logging.Formatter):
        def format(self, record):
            record.url = request.url
            record.remote_addr = request.remote_addr
            return super(RequestFormatter, self).format(record)

    request_formatter = RequestFormatter(
        "[%(asctime)s] %(remote_addr)s requested %(url)s\n"
        "%(levelname)s in %(module)s: %(message)s"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    info_file_handler = RotatingFileHandler(
        os.path.join(basedir, "logs/info.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=10,
    )
    info_file_handler.setFormatter(formatter)
    info_file_handler.setLevel(logging.INFO)

    error_file_handler = RotatingFileHandler(
        os.path.join(basedir, "logs/info.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=10,
    )
    error_file_handler.setFormatter(formatter)
    error_file_handler.setLevel(logging.ERROR)

    # mail_handler = SMTPHandler(
    #     mailhost=app.config['MAIL_SERVER'],
    #     fromaddr=app.config['MAIL_USERNAME'],
    #     toaddrs=['ADMIN_EMAIL'],
    #     subject='Application Error',
    #     credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))
    # mail_handler.setLevel(logging.ERROR)
    # mail_handler.setFormatter(request_formatter)

    app.logger.addHandler(info_file_handler)
    if not app.debug:
        app.logger.addHandler(error_file_handler)
        # app.logger.addHandler(mail_handler)


def register_errors(app):
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify("internal server error"), 500

    @app.errorhandler(NewError)
    def new_error(e):
        return jsonify("new error"), 400


def register_request_handlers(app):
    @app.after_request
    def query_profiler(response):
        for q in get_debug_queries():
            if q.duration >= app.config['BLUELOG_SLOW_QUERY_THRESHOLD']:
                app.logger.warning(
                    'Slow query: Duration: %fs\n Context: %s\nQuery: %s\n '
                    % (q.duration, q.context, q.statement)
                )
        return response
