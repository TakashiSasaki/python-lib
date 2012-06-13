from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.debug import *
from com.gmail.takashi316.lib.sqlalchemy import *
from com.gmail.takashi316.lib.string import *

from unittest import TestCase, main
class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        
    def testSqlAlchemySession(self):
        assert isUnicode("python-lib")
        session_factory = SqlAlchemySessionFactory("python-lib")
        session = session_factory.createSqlAlchemySession()
        self.assertIsInstance(session.bind, sqlalchemy.engine.base.Engine)
        self.assertIsInstance(session.bind.dialect, sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite)

if __name__ == "__main__":
    main()
