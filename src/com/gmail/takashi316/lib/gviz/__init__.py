from __future__ import unicode_literals, print_function
from _pydev_inspect import isclass
class GvizType(object):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    TIMEOFDAY = "timeofday"

def _getClass(class_or_instance):
    if isclass(class_or_instance):
        return class_or_instance
    else:
        return class_or_instance.__class__

def _iGvizString(class_or_instance, list_of_values =[]):
    class_ = _getClass(class_or_instance)
    try: 
        import sqlalchemy.types as sa
        if class_ in [sa.String, sa.Text, sa.Unicode, sa.UnicodeText, sa.CHAR, 
                      sa.NCHAR, sa.NVARCHAR, sa.TEXT, sa.VARCHAR]:
            return True
    except ImportError: pass
    return False

def _isGvizNumber(class_or_instance, list_of_values = []):
    class_ = _getClass(class_or_instance)
    try:
        import sqlalchemy.types as sa
        if class_ in [sa.BigInteger, sa.Float, sa.Integer, sa.Numeric, sa.SmallInteger, 
                      sa.BIGINT, sa.FLOAT, sa.INTEGER, sa.DECIMAL, sa.SMALLINT, sa.INT, 
                      sa.NUMERIC, sa.REAL,]:
            return True
    except ImportError: pass
    return False

def _isGvizBoolean(class_or_instance, list_of_values = []):
    class_ = _getClass(class_or_instance)
    if class_ in  [Boolean, BOOLEAN]:
        return True
    else: return False

def _isGvizDate(class_or_instance):
    [Date, DATE]
        
def _isGvizDateTime():
    [DateTime, DATETIME]

def _isGvizTimeOfDay():
     [Time, TIME]