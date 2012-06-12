from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.debug import *
from inspect import isclass

class SoftSingleton(type):
    """This code comes from http://code.activestate.com/recipes/412551/"""
    def __init__(self, *args, **kwargs):
        assert isclass(type)
        assert isclass(self)
        type.__init__(self, *args, **kwargs)
        self._instance = None

    def __call__(self, *args, **kwargs):
        assert isclass(self)
        if self._instance is None :
            self._instance = type.__call__(self, *args, **kwargs)
        return self._instance

class HardSingleton(type):
    def __init__(self, *args, **kwargs):
        assert isclass(type)
        assert isclass(self)
        type.__init__(self, *args, **kwargs)
        self._instance = None

    def __call__(self, *args, **kwargs):
        assert isclass(self)
        if self._instance is None :
            self._args = args
            self._kwargs = kwargs
            self._instance = type.__call__(self, *args, **kwargs)
        assert self._args == args
        assert self._kwargs == kwargs
        return self._instance

