# build-in package

# third-package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Custom module
from log import logger

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/")
def index():
    logger.info("test")
    return "test"
