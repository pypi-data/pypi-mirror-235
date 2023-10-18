import decimal
import json
from datetime import datetime, date


class DefaultEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o) if o % 1 == 0 else float(o)
        if isinstance(o, datetime):
            return o.__str__()
        if isinstance(o, date):
            return o.__str__()
        super(DefaultEncoder, self).default(o)
