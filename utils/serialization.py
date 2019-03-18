try:
    import simplejson as json
except ImportError:
    import json
import uuid
from datetime import date, datetime
from decimal import Decimal

from .exceptions import SerializationError


class JSONSerializer(object):

    def default(self, data):
        if isinstance(data, (date, datetime)):
            return data.isoformat()
        elif isinstance(data, Decimal):
            return float(data)
        elif isinstance(data, uuid.UUID):
            return str(data)
        raise TypeError("Unable to serialize %r (type: %s)" % (data, type(data)))

    def loads(self, s):
        try:
            return json.loads(s)
        except (ValueError, TypeError) as e:
            raise SerializationError(s, e)

    def dumps(self, data):
        if isinstance(data, (str, bytes)):
            return data

        try:
            return json.dumps(
                data,
                default=self.default,
                ensure_ascii=False,
                separators=(',', ':'),
            )
        except (ValueError, TypeError) as e:
            raise SerializationError(data, e)
