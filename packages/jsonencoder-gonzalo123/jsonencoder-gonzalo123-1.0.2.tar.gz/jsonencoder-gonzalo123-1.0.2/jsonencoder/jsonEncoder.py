import decimal
import json
import numbers
from datetime import datetime, date


class DefaultEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, numbers.Integral):
            return int(o)
        if isinstance(o, (decimal.Decimal, numbers.Real)):
            return float(o)
        if isinstance(o, datetime):
            return o.__str__()
        if isinstance(o, date):
            return o.__str__()
        super(DefaultEncoder, self).default(o)
