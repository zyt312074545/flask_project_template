from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.env_info import get_database_uri


class MySQL(object):
    def __init__(self):
        self.engine = None
        self.Session = None
        self.init_session()

    def init_session(self):
        database_uri = get_database_uri('MYSQL')
        self.engine = create_engine(database_uri)
        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)

    @contextmanager
    def session_scope(self):
        session = self.Session()
        try:
            yield session
        except Exception as error:
            session.rollback()
            raise error
        finally:
            session.close()
