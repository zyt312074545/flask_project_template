from sqlalchemy import Column, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    _id = Column(BigInteger, primary_key=True, autoincrement=True)
