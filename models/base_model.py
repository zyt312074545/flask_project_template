from sqlalchemy import Column, BigInteger
from sqlalchemy.ext.declarative import declarative_base

from utils.snowflake import Snowflake

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    _id = Column(BigInteger, primary_key=True, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = Snowflake(0).generate()
