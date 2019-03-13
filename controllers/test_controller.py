from flask import Blueprint
from flask_restful import Api

from .base_controller import BaseController


class TestController(BaseController):
    def __init__(self):
        super().__init__()

    def get(self):
        return "test"


api_test = Blueprint('test', __name__)
api = Api(api_test)

api.add_resource(TestController, "/test")
