from __future__ import unicode_literals, print_function 
from com.gmail.takashi316.lib.sqlite import *
from com.gmail.takashi316.lib.string import *
from com.gmail.takashi316.lib.singleton import *

from sqlalchemy import create_engine as _create_engine
from sqlalchemy.exc import SQLAlchemyError

class SqlAlchemyEngine(object):
    __metaclass__ = SoftSingleton
    _engine = None
    
    def __init__(self, subdirectory_ = None, file_stem = None):
        if self._engine is None:
            sqlite_url = SqliteUrl(subdirectory_, file_stem)
            assert isUnicode(sqlite_url())
            self._engine = _create_engine(sqlite_url(), echo=False)
        
    def __call__(self):
        return self._engine
    
    def getEngine(self):
        return self()

import sqlalchemy.engine.base
import sqlalchemy.orm.session
from sqlalchemy.orm.session import sessionmaker as _sessionmaker
class SqlAlchemySessionFactory(object):
    __metaclass__ = SoftSingleton
    _sessionClass = None
    
    def __init__(self, subdirectory_=None, file_stem=None):
        engine = SqlAlchemyEngine(subdirectory_, file_stem)()
        assert isinstance(engine, sqlalchemy.engine.base.Engine)
        #info (engine.__class__)
        if self._sessionClass is None:
            self._sessionClass = _sessionmaker(bind=engine, autocommit=False)
        #assert isinstance(self._sessionClass, sqlalchemy.orm.session.SessionMaker)
    
    def createSqlAlchemySession(self):
        return self._sessionClass()
