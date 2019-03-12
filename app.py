# build-in package

# third-package
from flask import Flask

# Custom module
from log import logger

app = Flask(__name__)


@app.route("/")
def index():
    logger.info("test")
    return "test"
