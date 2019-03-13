from sqlalchemy import Column, String

from models.base_model import BaseModel


class TestModel(BaseModel):
    __tablename__ = "test"

    username = Column(String(64), server_default="", comment="用户名称")
    password = Column(String(64), server_default="", comment="密码")
