from __future__ import unicode_literals, print_function
isUnicode = None
try:
    unicode
    def _(u):
        """tests if given value references unicode string."""
        if isinstance(u, unicode):
            return True
        else:
            return False
    isUnicode = _
except:
    def _(u):
        """tests if given value references unicode string."""
        if isinstance(u, str):
            return True
        else:
            return False
    isUnicode = _

def isEmptyUnicode(u):
    assert isUnicode(u)
    assert len(u) == 0

def isNonEmptyUnicode(u):
    assert isUnicode(u)
    assert len(u) > 0
  
