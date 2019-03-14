from flask import Blueprint
from flask_restful import Api

from controllers.blue_controller import BlueController

api_blue = Blueprint("blue", __name__)
api = Api(api_blue)

api.add_resource(BlueController, "/")
