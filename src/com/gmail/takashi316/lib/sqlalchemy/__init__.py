from __future__ import unicode_literals, print_function 
from com.gmail.takashi316.lib.sqlite import getSqliteUrl

from sqlalchemy import create_engine as _create_engine
from sqlalchemy.exc import SQLAlchemyError
_engine = None
def getEngine(subdirectory, file_stem):
    if _engine is not None:
        return _engine
    _engine = _create_engine(getSqliteUrl(subdirectory, file_stem), echo=False)
    return _engine
    
from sqlalchemy.orm.session import sessionmaker as _sessionmaker

_SessionClass = None
_subdirectory = None
_file_stem = None
def _getSessionClass(subdirectory, file_stem):
    if _SessionClass is not None:
        if _subdirectory != subdirectory and _file_stem != file_stem:
            raise SQLAlchemyError("subdirecory and file_stem is not identical that given for the first time.")
        return _SessionClass
    _subdirectory = subdirectory
    _file_stem = file_stem
    _SessionClass = _sessionmaker(bind=getEngine(subdirectory, file_stem), autocommit=False)
    return _SessionClass 

def getSession(subdirectory, file_stem):
    _getSessionClass(subdirectory, file_stem)
    return _SessionClass()

from unittest import TestCase, main
if __name__ == "__main__":
    main()
