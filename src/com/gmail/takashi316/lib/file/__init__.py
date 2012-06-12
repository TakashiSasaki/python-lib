from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.singleton import *
import os,os.path
from com.gmail.takashi316.lib.string import isUnicode, isEmptyUnicode

class HomeDirectory(object):
    __metaclass__ = SoftSingleton
    _homeDirectory = None

    def __init__(self):
        if self._homeDirectory is None:
            self._homeDirectory = os.path.expanduser("~") 
            if self._homeDirectory is None:
                raise IOError("can't get home directory")

    def __call__(self):
        return self._homeDirectory

    def get(self):
        return self()
    
class UserDirectory(object):
    __metaclass__ = SoftSingleton
    _userDirectory = None
    _subDirectory = None

    def __init__(self, subdirectory_ = None):
        if self._userDirectory is None:
            assert self._subDirectory is None
            assert isUnicode(subdirectory_)
            home_directory = HomeDirectory()()
            assert isUnicode(home_directory)
            self._subDirectory = subdirectory_
            self._userDirectory = os.path.join(home_directory, subdirectory_)
            assert isUnicode(self._userDirectory)
        if subdirectory_ is None:
            if self._subDirectory is None:
                raise IOError("subdirectory is mandatory if UserDirectory is not instantiated.")
            assert isUnicode(self._subDirectory)
            assert isUnicode(self._userDirectory)
        assert isUnicode(self._subDirectory)
        if not os.path.exists(self._userDirectory):
            os.mkdir(self._userDirectory)
            if not os.path.exists(self._userDirectory):
                raise IOError("User directory '" + self._userDirectory + "' cannot be created.")

    def get(self):
        assert isUnicode(self._userDirectory)
        return self()

    def __call__(self):
        assert isUnicode(self._userDirectory)
        return self._userDirectory
    
    def getSubdirectory(self):
        assert isUnicode(self._subDirectory)
        return self._subDirectory
