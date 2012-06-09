from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.file import getUserDirectory as _getUserDirectory
from com.gmail.takashi316.lib.debug import *

def getSqliteUrl(subdirectory, file_stem):
    import os.path
    sqlite_path = os.path.join(_getUserDirectory(subdirectory), file_stem + ".sqlite")
    info(sqlite_path) 
    sqlite_path_slash = sqlite_path.replace(os.path.sep, '/')
    info(sqlite_path_slash)
    sqlite_url = "sqlite:///" + sqlite_path_slash
    info(sqlite_url)
    return sqlite_url

from unittest import TestCase, main
if __name__ == "__main__":
    main()
