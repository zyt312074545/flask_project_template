from flask import Blueprint
from flask_restful import Api

from .base_controller import BaseController


class BlueController(BaseController):
    def __init__(self):
        super().__init__()

    def get(self):
        return "blue"


api_blue = Blueprint("blue", __name__)
api = Api(api_blue)

api.add_resource(BlueController, "/blue")
