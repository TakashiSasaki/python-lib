# -*- coding: utf8 -*-
from __future__ import unicode_literals, print_function
from inspect import ismodule
import os.path
import re
from time import sleep

class ApplicationDirectory(object):
    __slots__ = ["applicationDirectory", "applicationName"]
    
    def __init__(self, application_module):
        """application should be a class and its __name__ is used as the name of session file.""" 
        assert ismodule(application_module)
        assert application_module.__name__ != "__main__"
        self.applicationName = application_module.__name__
        self.applicationDirectory = os.getenv("AppData", os.getenv("HOME", ".")) + os.sep + self.applicationName
        assert isinstance(self.applicationDirectory, str)
        if not os.path.exists(self.applicationDirectory):
            os.mkdir(self.applicationDirectory)
        elif not os.path.isdir(self.applicationDirectory):
            raise RuntimeError("%s already exists and is not a directory" % self.applicationDirectory)
        
    def getApplicationDirectoryPath(self):
        assert isinstance(self.applicationDirectory, str)
        return self.applicationDirectory

    def __unicode__(self):
        assert isinstance(self.applicationDirectory, str)
        return self.applicationDirectory.decode()
    
    def __str__(self):
        assert isinstance(self.applicationDirectory, str)
        return self.applicationDirectory


from unittest import TestCase, main

class TestApplicationDirectory(TestCase):
    __slots__ = ["applicationDirectory"]

    def setUp(self):
        TestCase.setUp(self)
        from com.gmail.takashi316.lib.file import hello
        self.applicationDirectory = ApplicationDirectory(hello)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test(self):
        self.assertRegexpMatches(self.applicationDirectory.getApplicationDirectoryPath(),
                                 "C:\\\\Users\\\\Takashi\\\\AppData\\\\Roaming\\\\com.gmail.takashi316.lib.file.hello")

if __name__ == "__main__":
    main()
