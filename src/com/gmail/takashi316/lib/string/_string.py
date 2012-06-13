from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.string import *

from unittest import TestCase, main

class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
    def tearDown(self):
        TestCase.tearDown(self)
    def testUnicode(self):
        isUnicode("abc")
        isEmptyUnicode("")
        isNonEmptyUnicode("xyz")
        
if __name__ == "__main__":
    main()