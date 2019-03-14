from services.base_service import BaseService
from databases.sqlite import SQLite
from models.test_model import TestModel
from log import logger


class TestService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self, username, password):
        with SQLite().session_scope() as session:
            test = TestModel(
                username=username,
                password=password
            )
            session.add(test)
            session.commit()
        logger.info("Success create data.")
        return True

    def update(self, _id, username):
        with SQLite().session_scope() as session:
            q = session.query(TestModel).filter(TestModel._id==_id).first()
            q.username = username
            session.commit()
        logger.info("Success update data.")
        return True

    def get(self, _id):
        with SQLite().session_scope() as session:
            q = session.query(TestModel).filter(TestModel._id==_id).first()
        logger.info("Success get data.")
        return {"username": q.username}

    def delete(self, _id):
        with SQLite().session_scope() as session:
            q = session.query(TestModel).filter(TestModel._id==_id).first()
            session.delete(q)
            session.commit()
        logger.info("Success delete data.")
        return True
