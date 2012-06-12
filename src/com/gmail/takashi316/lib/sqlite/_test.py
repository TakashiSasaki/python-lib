from __future__ import unicode_literals, print_function
from unittest import TestCase, main
from com.gmail.takashi316.lib.sqlite import *

class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
    
    def tearDown(self):
        TestCase.tearDown(self)
    
    def test(self):
        self.assertIsInstance("abc", unicode)
        sqlite_url = SqliteUrl("abc", "xyz")
        self.assertIsInstance(sqlite_url(), unicode)

if __name__ == "__main__":
    main()
