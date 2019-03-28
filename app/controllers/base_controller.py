from flask_restful import Resource

from app.utils.serialization import JSONSerializer


class BaseController(Resource):
    def __init__(self, serializer=JSONSerializer(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = serializer
