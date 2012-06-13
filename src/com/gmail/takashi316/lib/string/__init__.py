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
    if not isUnicode(u): return False
    if len(u) == 0: return True
    return False

def isNonEmptyUnicode(u):
    if not  isUnicode(u): return False
    if len(u) > 0: return True
    return False
  
def isBytes(bs):
    return True if isinstance(bs, bytes) else False

def isEmptyBytes(bs):
    if not isBytes(bs): return False
    if len(bs) == 0: return True
    return False
