from flask import Blueprint
from flask import request
from flask_restful import Api

from .base_controller import BaseController
from services.test_service import TestService


class TestListController(BaseController):
    def __init__(self):
        super().__init__()

    def post(self):
        data = request.json
        service = TestService()
        response = service.create(data["username"], data["password"])
        return response


class TestController(BaseController):
    def __init__(self):
        super().__init__()

    def put(self, _id):
        data = request.json
        service = TestService()
        response = service.update(_id, data["username"])
        return response

    def get(self, _id):
        service = TestService()
        response = service.get(_id)
        return response

    def delete(self, _id):
        service = TestService()
        response = service.delete(_id)
        return response


api_test = Blueprint("test", __name__)
api = Api(api_test)

api.add_resource(TestListController, "/test")
api.add_resource(TestController, "/test/<string:_id>")
