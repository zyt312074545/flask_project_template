from app.extensions import db

from app.utils.snowflake import Snowflake


class BaseModel(db.Model):
    __abstract__ = True

    _id = db.Column(db.BigInteger, primary_key=True, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = Snowflake(0).generate()
