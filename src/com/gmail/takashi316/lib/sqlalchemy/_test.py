from __future__ import unicode_literals, print_function
from unittest import TestCase, main
from com.gmail.takashi316.lib.debug import *
from com.gmail.takashi316.lib.sqlalchemy import *
from com.gmail.takashi316.lib.string import *
class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        
    def test(self):
        assert isUnicode("obomb")
        session_factory = SqlAlchemySessionFactory("obomb", "obomb")
        session = session_factory.createSqlAlchemySession()
        
if __name__ == "__main__":
    main()
