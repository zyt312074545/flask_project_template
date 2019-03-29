from flask import current_app, jsonify

from app.services.base_service import BaseService
from app.extensions import db
from app.models.test_model import TestModel


class TestService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self, username, password):
        test = TestModel(username=username)
        test.set_password(password)
        _id = test._id
        db.session.add(test)
        db.session.commit()
        current_app.logger.info("success")
        return jsonify({"_id": _id})

    def update(self, _id, username):
        q = TestModel.query.filter_by(_id=_id).first()
        q.username = username
        db.session.commit()
        return jsonify({"status": True})

    def get(self, _id):
        q = TestModel.query.filter_by(_id=_id).first()
        return jsonify({"username": q.username})

    def delete(self, _id):
        q = TestModel.query.filter_by(_id=_id).first()
        db.session.delete(q)
        db.session.commit()
        return jsonify({"status": True})
