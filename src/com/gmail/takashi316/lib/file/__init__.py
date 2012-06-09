from __future__ import unicode_literals, print_function

_homeDirectory = None
def getHomeDirectory():
    if _homeDirectory is not None:
        return _homeDirectory
    import os.path
    _homeDirectory = os.path.expanduser("~")
    return _homeDirectory
    
_userDirectory = None
def getUserDirectory(subdirectory):
    if _userDirectory is not None:
        return _userDirectory
    import os.path
    _userDirectory = os.path.join(getHomeDirectory(), subdirectory)
    if not os.path.exists(_userDirectory):
        import os
        os.mkdir(_userDirectory)
        if not os.path.exists(_userDirectory):
            raise IOError("User directory '" + _userDirectory + "' cannot be created.")
    return _userDirectory

from unittest import TestCase, main
if __name__ == "__main__":
    main()
