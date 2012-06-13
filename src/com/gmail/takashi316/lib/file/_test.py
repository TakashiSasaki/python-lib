from __future__ import unicode_literals, print_function
from unittest import TestCase, main
from com.gmail.takashi316.lib.file import *
from com.gmail.takashi316.lib.string import isUnicode

class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def testHomeDirectory(self):
        home_directory = HomeDirectory()
        assert isUnicode(home_directory())
        assert isUnicode(home_directory.get())
    
    def testUserDirectory(self):
        user_directory = UserDirectory("test")
        self.assertTrue(isUnicode(user_directory.get()))
        self.assertTrue(isUnicode(user_directory.getSubdirectory()))
        self.assertEqual("test", user_directory.getSubdirectory())
        user_directory2 = UserDirectory()
        self.assertEqual("test", user_directory.getSubdirectory())

if __name__ == "__main__":
    main()
