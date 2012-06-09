from __future__ import  print_function, unicode_literals

from datetime import datetime as _datetime
from dateutil.tz import tzutc
def utcnow():
    dt = _datetime.utcnow();
    assert isinstance(dt, _datetime)
    assert dt.tzinfo is None
    dt2 = dt.replace(tzinfo=tzutc())
    return dt2

