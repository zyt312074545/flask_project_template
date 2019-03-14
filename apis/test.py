from flask import Blueprint
from flask_restful import Api

from controllers.test_controller import TestListController, TestController

api_test = Blueprint("test", __name__)
api = Api(api_test)

api.add_resource(TestListController, "/test")
api.add_resource(TestController, "/test/<string:_id>")
