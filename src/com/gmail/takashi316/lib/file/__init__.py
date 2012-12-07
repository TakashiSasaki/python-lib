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

from unittest import TestCase, main

class Test(TestCase):
    def setUp(self):
        TestCase.setUp(self)
    
    def tearDown(self):
        TestCase.tearDown(self)

if __name__ == "__main__":
    main()
