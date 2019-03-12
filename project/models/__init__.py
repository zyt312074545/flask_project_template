"""
┌┬┐┌─┐┌┬┐┌─┐┬  ┌─┐
││││ │ ││├┤ │  └─┐
┴ ┴└─┘─┴┘└─┘┴─┘└─┘
"""

import click
from flask.cli import with_appcontext

from project import db


def init_db(app):
    db.init_app(app)


@click.command('init-db')
@with_appcontext
def init_db():
    db.create_all()
    click.echo('Initialized the database.')


def init_db_command(app):
    app.cli.add_command(init_db)
