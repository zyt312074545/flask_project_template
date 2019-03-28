from flask import Blueprint
from flask_restful import Api

from app.controllers.test_controller import TestListController, TestController

api_test = Blueprint("test", __name__)
api = Api(api_test)

api.add_resource(TestListController, "/")
api.add_resource(TestController, "/<string:_id>")
