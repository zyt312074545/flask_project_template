from flask import Flask

# import controller
from apis.test import api_test
from apis.blue import api_blue

app = Flask(__name__)

app.register_blueprint(api_test)
app.register_blueprint(api_blue)
