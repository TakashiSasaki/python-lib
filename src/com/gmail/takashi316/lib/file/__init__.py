from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.singleton import *
import os, os.path
from com.gmail.takashi316.lib.string import isUnicode, isEmptyUnicode
from inspect import ismodule

def getModuleName(application_module):
    assert ismodule(application_module)
    assert application_module.__name__ != "__main__"
    return application_module.__name__

def getHomeDirectory():
    home_directory = os.path.expanduser("~") 
    if home_directory is None:
        raise IOError("can't get home directory")
    return home_directory

from unittest import TestCase, main

class Test(TestCase):
    def setUp(self):
        TestCase.setUp(self)
#        file = open("./hello.py", "a+")
#        file.write("\"\"\"this is a hello module\"\"\"")
#        file.close()
    
    def tearDown(self):
        TestCase.tearDown(self)
#        os.remove("./hello.py")
        
    def testGetModuleName(self):
        from com.gmail.takashi316.lib.file import hello
        x = getModuleName(hello)
        self.assertIsInstance(x, str)
    
    def testGetHomeDirectory(self):
        x = getHomeDirectory()
        self.assertIsInstance(x, unicode)

if __name__ == "__main__":
    main()
