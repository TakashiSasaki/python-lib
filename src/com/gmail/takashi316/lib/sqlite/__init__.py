from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.file import *
from com.gmail.takashi316.lib.debug import *
from com.gmail.takashi316.lib.string import *
from com.gmail.takashi316.lib.singleton import *

class SqliteUrl(object):
    __metaclass__ = SoftSingleton
    _sqlitePath = None
    _sqliteUrl = None
    
    def __init__(self, subdirectory_ = None, file_stem = None):
        if isUnicode(self._sqliteUrl): return self._sqliteUrl
        user_directory = UserDirectory(subdirectory_)
        if subdirectory_ is None:
            subdirectory_ = user_directory.getSubdirectory()
        if file_stem is None:
            file_stem = subdirectory_
        self._sqlitePath = os.path.join(user_directory(), file_stem + ".sqlite")
        sqlite_path_slash = self._sqlitePath.replace(os.path.sep, '/')
        self._sqliteUrl = "sqlite:///" + sqlite_path_slash
         
    def __call__(self):
        assert isUnicode(self._sqliteUrl)
        return self._sqliteUrl
    
    def __str__(self):
        return self()
    
    def get(self):
        return self()
