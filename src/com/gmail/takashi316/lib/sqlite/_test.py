from __future__ import unicode_literals, print_function
from unittest import TestCase, main
from com.gmail.takashi316.lib.sqlite import *

class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
    
    def tearDown(self):
        TestCase.tearDown(self)
    
    def testSqliteUrl(self):
        sqlite_url = SqliteUrl("python-lib", "python-lib")
        self.assertTrue(isNonEmptyUnicode(sqlite_url()))

if __name__ == "__main__":
    main()
