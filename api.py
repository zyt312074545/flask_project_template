from flask import Flask

# import controller
from controllers.test_controller import api_test
from controllers.blue_controller import api_blue

app = Flask(__name__)

app.register_blueprint(api_test)
app.register_blueprint(api_blue)
